from machine import ADC, Pin

adc = ADC(Pin(26))  # ADC0 GPIO26
print(adc.read_u16())
