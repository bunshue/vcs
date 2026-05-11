from machine import ADC, Pin
import time

adc = ADC(Pin(27))
led = Pin(15, Pin.OUT) 
led.value(0)
while True:
    value = adc.read_u16()
    print(value)
    if value < 25000: 
        led.value(1)
        time.sleep(0.5) 
    else:
        led.value(0) 
        time.sleep(0.5)
