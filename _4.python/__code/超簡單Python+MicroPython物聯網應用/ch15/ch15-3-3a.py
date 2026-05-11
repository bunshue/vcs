from machine import Pin, PWM
import time

pwm = PWM(Pin(15))

while True:
    for i in range(0, 65536, 100):
        pwm.duty_u16(i)
        time.sleep(0.01)
    for i in range(65535, -1, -100):
        pwm.duty_u16(i)
        time.sleep(0.01)
