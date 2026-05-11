from machine import Pin

led = Pin(2, Pin.OUT)
btn = Pin(4, Pin.IN, Pin.PULL_UP)

state = 1
def toggleLED():
    global state
    state = not state
    led.value(state)

led.value(1)
while True:
    if btn.value() == 0:
        toggleLED()
        while not btn():  # 過濾多餘的按下按鍵
            pass
        