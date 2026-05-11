from machine import ADC, Pin
import utime 

adc = ADC(0)
led = Pin(15, Pin.OUT) 
led.value(0)
while True:
    value = adc.read()
    print(value)
    if value < 100:     # 光線不足
        led.value(1)    # 點亮LED
        utime.sleep(0.5) 
    else:               # 否則
        led.value(0)    # 熄滅LED
        utime.sleep(0.5)
        