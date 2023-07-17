import RPi.GPIO as GPIO
import time

pinBN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN, GPIO.IN)

try:
    n = 1
    while True:
        if not GPIO.input(pinBN):
            print ("{}: 按鈕按下".format(n))
            n += 1
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
GPIO.cleanup()