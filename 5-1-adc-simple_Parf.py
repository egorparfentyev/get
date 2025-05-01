import RPi.GPIO as GPIO
import time

def binar(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        GPIO.output(dac, binar(value))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            return value
    return 255
    

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        value = adc()
        voltage = 3.3 * value / 256
        print(f'Цифровое значение: {value}, Напряжение: {voltage:.2f}V')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("Программа завершена")