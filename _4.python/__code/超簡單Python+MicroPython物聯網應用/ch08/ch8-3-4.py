from machine import Pin
import utime 

led = Pin(2, Pin.OUT)               
button = Pin(4, Pin.IN, Pin.PULL_UP)
led.value(1)
state = 1
while True:
    if button.value() == 0:
        utime.sleep_ms(10)  # 延遲時間是避免彈跳
        if button.value() == 0:
            state = not state
            led.value(state)
            while not button.value():
                pass
            