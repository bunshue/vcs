import RPi.GPIO as GPIO
import time

pinLED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)

try:
    while True:
        GPIO.output(pinLED, 1)  # LED On
        time.sleep(1)
        GPIO.output(pinLED, 0)  # LED Off
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()