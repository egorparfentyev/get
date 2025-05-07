import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, binary(value))
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            value -= 2**i
    return value

GPIO.setmode(GPIO.BCM)

# dac = [8, 11, 7, 1, 0, 5, 12, 6]
# leds = [2, 3, 4, 17, 27, 22, 10, 9]
# comp = 14
# troyka = 13

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

try:
    izm = []
    start_time = time.time()
    GPIO.output(troyka, 0)
    print('Начало зарядки конденсатора')
    while True:
        vol = adc()
        print(f"Полученное значение напряжения1: {vol}")
        izm.append(vol)
        GPIO.output(leds, binary(vol))
        if vol >= 0.97 * 255:
            break
        time.sleep(0.001)
    
    GPIO.output(troyka, 1)
    print('Начало разрядки конденсатора')
    while True:
        vol = adc()
        print(f"Полученное значение напряжения: {vol}")
        izm.append(vol)
        GPIO.output(leds, binary(vol))
        if vol <= 50:
            break
        time.sleep(0.001)
    
    end_time = time.time()
    dur = end_time - start_time
    count = len(izm)
    per = dur / count
    freq = 1 / per
    volt_step = 3.3 / 255

    plt.plot(izm)
    plt.xlabel('Номер измерения')
    plt.ylabel('Значение АЦП, В')
    plt.title('Помргите')
    plt.show()

    with open("data.txt", "w") as znach:
        for voltage in izm:
            znach.write(f"Полученное значение напряжения: {voltage} В \n")

    with open("settings.txt", "w") as f:
        f.write(f"Частота дискретизации: {freq:.2f} Гц \n")
        f.write(f"Шаг квантования АЦП: {volt_step:.4f} В/n \n")
    
    print(f"Общая продолжительность эксперимента: {dur:.2f} с")
    print(f"Период одного измерения: {per:.4f} с")
    print(f"Частота дискретизации: {freq:.2f} Гц")
    print(f"Шаг квантования АЦП: {volt_step:.4f} В/n")


finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()