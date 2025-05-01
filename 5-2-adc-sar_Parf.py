import RPi.GPIO as GPIO
import time

def binar(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    # value = 0
    # for i in range(7, -1,- 1):
    #     value += 2**i
    #     GPIO.output(dac, binar(value))
    #     time.sleep(0.001)
    #     if GPIO.input(comp) == 1:
    #         value -= 2**i
    # return value
    value = 0
    value += 128
    GPIO.output(dac, binar(value))
    time.sleep(0.0001)
    if GPIO.input(comp):
        value -= 128
    
    value += 64
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 64
    
    value += 32
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 32
    
    value += 16
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 16

    value += 8
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 8
    
    value += 4
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 4

    value += 2
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 2
    
    value += 1
    GPIO.output(dac, binar(value))
    time.sleep(0.001)
    if GPIO.input(comp):
        value -= 1
    return value


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