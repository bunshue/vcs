from machine import Pin, Timer

ledR = Pin(15, Pin.OUT, 0)
ledG = Pin(12, Pin.OUT, 0)
ledB = Pin(13, Pin.OUT, 0)
leds = [ledR, ledG, ledB]

MAX = 3
index = 0

def marquee(t):
    global index, MAX
    if index == 0:
        pre_index = MAX-1
    else:
        pre_index = index-1
    leds[pre_index].value(0)    
    leds[index].value(1)    
    index = index + 1
    if index == MAX:
        index = 0
    
t = Timer(0)
t.init(period=1000, mode=Timer.PERIODIC, callback=marquee)
