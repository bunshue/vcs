from machine import ADC, Pin
import utime

adc = ADC(0)
led = Pin(15, Pin.OUT)

def blink_led():
    for _ in range(5):
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(0.5)

while True:
    value = adc.read()
    print(value)
    if value < 100:  # 光線不足
        blink_led()  # 呼叫blink_led函式
    else:  # 否則
        led.value(0)  # 熄滅LED
        utime.sleep(0.5)
