from machine import Pin
import time 
 
# DPIO2對應到D4 
led = Pin(2, Pin.OUT) #D4 內建 Led
 
while True:
    led.value(1)   #燈熄
    time.sleep(0.5)#暫停 0.5 秒

    led.value(0)   #燈亮
    time.sleep(0.5)#暫停 0.5 秒
    print("Hello")