from machine import Pin 

led = Pin(2, Pin.OUT)      
button = Pin(4, Pin.IN, Pin.PULL_UP)
led.value(1)

while True:
    if not button.value():
        led.value(not led.value()) # 執行動作
        while not button.value():  # 過濾多餘的按下按鍵
            pass
        