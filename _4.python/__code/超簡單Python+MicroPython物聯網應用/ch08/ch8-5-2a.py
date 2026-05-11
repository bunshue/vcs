from machine import ADC, Pin, PWM
import utime 

adc = ADC(0)
pwm = PWM(Pin(15)) 
while True:
    value = adc.read()
    print(value)
    pwm.duty(1024-value)
    utime.sleep(0.5)
    