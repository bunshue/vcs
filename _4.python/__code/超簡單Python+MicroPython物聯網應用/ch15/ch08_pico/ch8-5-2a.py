from machine import ADC, Pin, PWM
import utime 

adc = ADC(Pin(26))  # ADC0 GPIO26
pwm = PWM(Pin(15))
pwm.freq(1000)
while True:
    value = adc.read_u16()
    print(value)
    pwm.duty_u16(65535-value)
    utime.sleep(0.5)
    