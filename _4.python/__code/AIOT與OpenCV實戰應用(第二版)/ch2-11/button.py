#!/usr/bin/python3
import RPi.GPIO as GPIO

pinBN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ret = GPIO.wait_for_edge(pinBN, GPIO.BOTH, timeout=15000)

print('content-type: text/html')
print()
print('0' if ret is None else '1')
