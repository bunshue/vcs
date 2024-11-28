import RPi.GPIO as GPIO
from time import sleep
GPIOPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOPin, GPIO.OUT)
for i in range(0,20):
    GPIO.output(GPIOPin, True)
    sleep(0.5)
    GPIO.output(GPIOPin, False)
    sleep(0.5)
GPIO.cleanup()
