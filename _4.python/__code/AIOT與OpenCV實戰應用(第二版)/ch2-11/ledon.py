#!/usr/bin/python3
import RPi.GPIO as GPIO

pinLED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.output(pinLED, 1)

# CGI 規定在標準輸出之前必須先輸出這兩行
print('content-type: text/html')
print()

# 網頁上看到的內容
print('led on')