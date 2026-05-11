from machine import Pin

led = Pin(2, Pin.OUT)
btn = Pin(4, Pin.IN, Pin.PULL_UP)

state = 1
def toggleLED(pin):
    global state
    if btn.value() == 0:
        state = not state
        led.value(state)

led.value(1)
btn.irq(trigger=Pin.IRQ_FALLING, handler=toggleLED)
