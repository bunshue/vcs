import RPi.GPIO as GPIO
from time import sleep
import moving
servoPin = 12
pressPin = [25, 16, 20]
LEDPin   = [18, 23, 24]
dutyCycle = [2.5, 7.5, 10.5]
debounce = 0
maxDebounce = 500
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
for Pin in pressPin:
    GPIO.setup(Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for Pin in LEDPin:
    GPIO.setup(Pin, GPIO.OUT, initial = False)
servo1 = GPIO.PWM(servoPin, 50)
servo1.start(0)
sleep(1)
doPress = False
currentDutyCycle = 0
previousDutyCycle = 0
try:
    while 1:
        for i in range(3):
            press = GPIO.input(pressPin[i])
            if press == 0:
                if debounce > maxDebounce:
                    debounce = 0
                    GPIO.output(LEDPin[i], True)
                    doPress = True
                    currentDutyCycle = i
                    while GPIO.input(pressPin[i]) == 0:
                        pass
                else:debounce += 1
            else:
                GPIO.output(LEDPin[i], False)
        if doPress == True:
            moving.toTarget(servo1, dutyCycle[previousDutyCycle], dutyCycle[currentDutyCycle])
            previousDutyCycle = currentDutyCycle
            servo1.ChangeDutyCycle(0)
            sleep(1)
            doPress = False
except KeyboardInterrupt:
    print("Exit!")
finally:
    GPIO.cleanup()
