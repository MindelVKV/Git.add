import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
state = 0
GPIO.setup(led, GPIO.OUT)
bot=13
GPIO.setup(bot, GPIO.IN)
while True:
    if GPIO.input(bot):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)