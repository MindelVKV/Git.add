import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        
        # Создаем ШИМ объект
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)  # Запускаем ШИМ с 0% заполнением
        
        if self.verbose:
            print(f"PWM DAC инициализирован на пине: {self.gpio_pin}")
            print(f"Частота ШИМ: {self.pwm_frequency} Гц")
            print(f"Динамический диапазон: {self.dynamic_range} В")

    def deinit(self):
        """Безопасное отключение ШИМ и очистка GPIO"""
        self.pwm.stop()
        GPIO.cleanup()
        if self.verbose:
            print("PWM DAC отключен, GPIO очищены")

    def set_voltage(self, voltage):
        """Устанавливает напряжение на ЦАП с помощью ШИМ"""
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
                print("Устанавливаем 0.0 В")
            self.pwm.ChangeDutyCycle(0)
            return
            
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В")
            print(f"Коэффициент заполнения ШИМ: {duty_cycle:.2f}%")

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()