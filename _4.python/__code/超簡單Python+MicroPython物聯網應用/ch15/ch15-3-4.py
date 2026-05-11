from machine import Pin, PWM, ADC
import time

pwm = PWM(Pin(15))
pwm.freq(1000)
adc = ADC(Pin(26))

while True:
    bright = adc.read_u16()
    pwm.duty_u16(bright)
    time.sleep(0.5)
