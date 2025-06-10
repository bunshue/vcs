from machine import Pin,Timer
import time 

led = Pin(2, Pin.OUT) # DPIO2(D4)內建Led
timer = Timer(1)
counter=0

def show(t):
    global counter
    counter+=1
    led.value(not led.value())   #燈閃爍
    if counter==10:
        t.deinit()    

timer.init(period=500, mode=Timer.PERIODIC, callback=show)    

try:
    while True:
        pass
except:
    timer.deinit()
    print('stopped')