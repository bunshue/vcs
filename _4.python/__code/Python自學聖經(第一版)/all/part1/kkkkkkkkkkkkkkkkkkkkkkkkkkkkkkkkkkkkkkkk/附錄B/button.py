from machine import Pin
from time import sleep
 
# DPIO2對應到D4 
ledB = Pin(2, Pin.OUT)  #D4 內建 Led
button = Pin(0, Pin.IN) #GPIO0--D3

while True:
    if button.value()==0: #按下按鈕，燈亮
        ledB.value(0)
    else:  #放開按鈕，燈熄
        ledB.value(1)
    print(button.value())
    sleep(.1)    