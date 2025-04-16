import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

try:
    try:

        while True:
            duty_cycle = float(input("Введите коэффициент заполнения (0 - 100%: "))

            p.ChangeDutyCycle(duty_cycle)

            voltage = 3.3 * duty_cycle / 100
            print(f'Напряжение на R-C цепи: {voltage:.3f} В')

    except ValueError:
        print("Введите числовое значение: ")

except KeyboardInterrupt:
    print("Программа остановлена")

finally:
    GPIO.cleanup()
    print("Программа завершена")