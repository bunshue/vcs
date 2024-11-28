from time import sleep
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
DHT11Pin = 18  
buttonPin = 25
LEDPin = 16
debounce = 0
maxDebounce = 500
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDPin, GPIO.OUT, initial=False)
count = 0
try:
    print('Temperature and humidity are measuring...')
    while True:
        if GPIO.input(buttonPin) == 0:
            if debounce > maxDebounce:
                debounce = 0
                GPIO.output(LEDPin, True)
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT11Pin)
                if humidity is not None and temperature is not None:
                    print(time.asctime())
                    print('Temperature={0:0.0f}C Humidity={1:0.0f}%'.format(temperature, humidity))
                    while GPIO.input(buttonPin) == 0:
                        pass
                else:
                    print('Wait a moment and psuh button again!')
            else:
                debounce += 1
        else:
            GPIO.output(LEDPin, False)
except KeyboardInterrupt:
    print('Exit!')
finally:
    GPIO.cleanup()
