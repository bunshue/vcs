import RPi.GPIO as GPIO
import time

pinLED = 4
pinSR = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinSR, GPIO.IN)

try:
   while True:
       GPIO.output(pinLED, GPIO.input(pinSR))
       time.sleep(0.1)

except KeyboardInterrupt:
   pass

GPIO.cleanup()
