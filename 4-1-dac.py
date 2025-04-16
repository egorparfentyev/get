import RPi.GPIO as GPIO

def dvoich(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def calc_voltage(value):
    return 3.3 * value / 255

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        user_input = input("Введите число от 0 до 255 для последующего представления числа в двочиной системе (или нажмите 'q' для выхода из программы): ")
        if user_input.lower() == 'q':
            break
            
        try:
            number = float(user_input)
        except ValueError:
            print("Error: Введено не числовое значение")
        else:

            if number < 0:
                print("Error: Число < 0")
                continue

            if number > 255:
                print("Error: Число превышает допустимое значение")
                continue

            if int(number) != number:
                print("Error: Введено не целое число")
                continue
            
           
            GPIO.output(dac, dvoich(int(number)))

            voltage = calc_voltage(number)
            print(f'Напряжение на выходе: {voltage:.2f} В')


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("Программа завершена")