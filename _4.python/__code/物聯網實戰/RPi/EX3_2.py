import RPi.GPIO as GPIO
from time import sleep
LEDPin = 18
buttonPin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
preState = False
debounce = 0
maxDebounce = 500
try:
    while True:
        if GPIO.input(buttonPin) == 0:
            if debounce > maxDebounce:
                GPIO.output(LEDPin, not preState)
                preState = not preState
                debounce = 0
                while GPIO.input(buttonPin) == 0:
                    pass
            else:
                debounce += 1
except KeyboardInterrupt:
	print('Exit')
finally:
	GPIO.cleanup()
