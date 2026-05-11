from machine import Pin 

led = Pin(25, Pin.OUT)  # Pico 內建LED是GPIO25, Pico W 是"LED"      
button = Pin(4, Pin.IN, Pin.PULL_UP)
led.value(0)

while True:
    if not button.value():
        led.value(not led.value()) # 執行動作
        while not button.value():  # 過濾多餘的按下按鍵
            pass
        