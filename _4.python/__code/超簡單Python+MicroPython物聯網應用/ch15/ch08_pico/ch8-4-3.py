from machine import Pin 

leds = [Pin(15,Pin.OUT),Pin(12,Pin.OUT),Pin(13,Pin.OUT)]
button = Pin(4, Pin.IN, Pin.PULL_UP)

def leds_off():
   for led in leds:
       led.value(0)
   
leds_off()
idx = 0
while True:
    if not button():
        leds_off()
        leds[idx].value(1)   # 點亮Pin物件的LED
        idx = idx + 1
        if idx > 2:
            idx = 0
        while not button():  # 過濾多餘的按下按鍵
            pass
        