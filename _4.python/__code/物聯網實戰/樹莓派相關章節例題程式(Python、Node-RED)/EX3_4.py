import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trigPin = 23
echoPin = 24
buttonPin = 12
LEDPin = 21
debounce = 0
maxDebounce = 500
soundSpeed = 340.  # Based on 15 degrees of Celsius
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        if GPIO.input(buttonPin) == 0:
            if debounce > maxDebounce:
                GPIO.output(LEDPin, True)
                debounce = 0
                GPIO.output(trigPin, False)
                time.sleep(0.002)
                GPIO.output(trigPin, True)
                time.sleep(0.00001)
                GPIO.output(trigPin, False)
                while GPIO.input(echoPin) == 0:
                    pass
                emittingTime = time.time()
                while GPIO.input(echoPin) == 1:
                    pass
                echoTime = time.time()
                distance = (echoTime - emittingTime)*soundSpeed/2.*100
                print("Distance = {0:.2f} cm".format(distance))
                while GPIO.input(buttonPin) == 0:
                   pass
                GPIO.output(LEDPin, False)
            else:
                debounce += 1
except KeyboardInterrupt:
    print("Exit!")
finally:
    GPIO.cleanup()
