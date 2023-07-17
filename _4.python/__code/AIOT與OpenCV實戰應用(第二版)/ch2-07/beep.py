import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 1)
p.start(50)

# Do
p.ChangeFrequency(523)
time.sleep(1)
# Re
p.ChangeFrequency(587)
time.sleep(1)
# Mi
p.ChangeFrequency(659)
time.sleep(1)

p.stop()
GPIO.cleanup()
