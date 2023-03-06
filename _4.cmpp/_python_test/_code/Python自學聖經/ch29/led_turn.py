from machine import Pin
import time 

def show_led(led):
    led.value(1)    #燈亮
    time.sleep(0.5) # 停0.5秒
    led.value(0)    #燈熄
 
# GPIO16對應到D0，DPIO14對應到D5，GPIO12對應到D6 
ledR = Pin(16, Pin.OUT)  #D0 紅燈
ledG = Pin(14, Pin.OUT)  #D5 綠燈
ledB = Pin(12, Pin.OUT)  #D6 藍燈
 
while True:
    show_led(ledR) # 紅燈亮
    show_led(ledG) # 綠燈亮
    show_led(ledB) # 藍燈亮
    print("R,G,B")