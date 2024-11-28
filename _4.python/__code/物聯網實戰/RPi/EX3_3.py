import RPi.GPIO as GPIO
import time
import os
def fileName():
    t = time.localtime()
    fname = str(t.tm_mon) + str(t.tm_mday) + str(t.tm_hour)
    fname = fname + str(t.tm_min) + str(t.tm_sec)
    return fname + ".jpg"
sensorPin = 23
debounce = 0
maxDebounce = 500
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
doPress = False
try:
    while 1:
        press = GPIO.input(sensorPin)
        if GPIO.input(sensorPin) == 0:
            if debounce > maxDebounce:
                debounce = 0
                doPress = True
                while GPIO.input(sensorPin) == 0:
                    pass
            else:
                debounce += 1
        if doPress == True:
            f1 = fileName()
            snapshot = "fswebcam " + f1
            os.system(snapshot)
            time.sleep(1)
            doPress = False
except KeyboardInterrupt:
    print("Exit!")
finally:
    GPIO.cleanup() 
