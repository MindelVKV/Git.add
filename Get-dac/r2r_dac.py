import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
        
        if self.verbose:
            print(f"R2R DAC инициализирован на пинах: {self.gpio_bits}")
            print(f"Динамический диапазон: {self.dynamic_range} В")

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        if self.verbose:
            print("R2R DAC отключен, GPIO очищены")

    def set_number(self, number):
       
        if number < 0 or number > 255:
            if self.verbose:
                print(f"Число {number} выходит за диапазон 0-255")
            number = max(0, min(255, number))
            
        binary = bin(number)[2:].zfill(8)
        binary_array = [int(bit) for bit in binary]
        
        for i in range(len(self.gpio_bits)):
            GPIO.output(self.gpio_bits[i], binary_array[i])
            
        if self.verbose:
            print(f"Установлено число: {number}")
            print(f"Двоичное представление: {binary}")

    def set_voltage(self, voltage):
      
        if voltage < 0 or voltage > self.dynamic_range:
            if self.verbose:
                print(f"Напряжение {voltage:.2f} В выходит за динамический диапазон (0.00 - {self.dynamic_range:.2f} В)")
                print("Устанавливаем 0.0 В")
            self.set_number(0)
            return
            
        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В")

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()