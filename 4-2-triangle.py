import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def dvoich(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def calc_per(per):
    return per / (256 * 2)

try:
    per = float(input("Введите период треугольного сигнала: "))
    try:
        if per < 0:
            print("Error: Число < 0")

        sleep_time = calc_per(per)
        print("Формирование треугольного сигнала...")
        while True:
            for value in range(256):
                GPIO.output(dac, dvoich(int(value)))
                time.sleep(sleep_time)
            for value in range(254, 0, -1):
                GPIO.output(dac, dvoich(int(value)))
                time.sleep(sleep_time)
    except ValueError:
        print("Error")        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("Программа завершена")