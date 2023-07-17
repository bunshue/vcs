import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)

# 0 degree
p.start(2.5)
time.sleep(0.4)
# 180 degree
p.ChangeDutyCycle(12)
time.sleep(0.4)
# 90 degree
p.ChangeDutyCycle(7.25)
time.sleep(0.4)

p.stop()
GPIO.cleanup()