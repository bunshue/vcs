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
"""
import RPi.GPIO as GPIO
from time import sleep
BOARDPin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BOARDPin, GPIO.OUT)
for i in range(0,20):
 GPIO.output(BOARDPin, True)
 sleep(0.5)
 GPIO.output(BOARDPin, False)
 sleep(0.5)
GPIO.cleanup()
"""
