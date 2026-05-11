from machine import ADC, Pin
import utime 

adc = ADC(Pin(26))  # ADC0 GPIO26

while True:
    adc_value = adc.read_u16()
    print(adc_value)
    utime.sleep(0.5)
    