from machine import Pin
import utime

# 初始化GPIO2的內建LED，並注意其1熄0亮的特性
builtin_led = Pin(2, Pin.OUT)

# 初始化其他3個LED
pin15 = Pin(15, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
pin12 = Pin(12, Pin.OUT)

# 將所有LED加入列表
leds = [builtin_led, pin15, pin13, pin12]

for i in range(10):
    for led in leds:
        if led == builtin_led:
            led.value(0)  # 內建LED，0點亮
        else:
            led.value(1)  # 其他LED，1點亮
        utime.sleep(0.3)
        led.value(1 if led == builtin_led else 0)  # 內建LED，1熄滅；其他LED，0熄滅
