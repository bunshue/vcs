#!/usr/bin/python3
import RPi.GPIO as GPIO
import cgi

form = cgi.FieldStorage()
isOn = int(form.getvalue('on'))

pinLED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.output(pinLED, isOn)

print(content-type:text/html')
print()

print('led is {}'.format('ON' if isOn else 'OFF'))
