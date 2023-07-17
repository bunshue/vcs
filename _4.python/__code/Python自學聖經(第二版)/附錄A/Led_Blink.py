from machine import Pin
import time 
 
# DPIO16對應到D0 
led = Pin(16, Pin.OUT)
 
while True:
    led.value(1)   #燈亮
    time.sleep(0.5)#暫停 0.5 秒

    led.value(0)   #燈熄
    time.sleep(0.5)#暫停 0.5 秒
    print("Hello")