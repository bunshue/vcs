from machine import ADC
import utime 

adc = ADC(0)

while True:
    adc_value = adc.read()
    print(adc_value)
    utime.sleep(0.5)
    