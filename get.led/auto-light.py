import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
bot=6

GPIO.setup(bot, GPIO.IN)
while True:
    state = GPIO.input(bot)
    GPIO.output(led, not state)
    time.sleep(0.2)