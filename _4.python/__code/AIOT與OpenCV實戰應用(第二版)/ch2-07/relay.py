import RPi.GPIO as GPIO
import time

pinRelay = 17
pinBn = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinRelay, GPIO.OUT)
GPIO.setup(pinBn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.add_event_detect(pinBn, GPIO.BOTH, bouncetime=500, callback=lambda:
       GPIO.output(pinRealy, not GPIO.input(pinBn))
    )
    while True:
        time.sleep(1000000)
except:
    GPIO.cleanup()
