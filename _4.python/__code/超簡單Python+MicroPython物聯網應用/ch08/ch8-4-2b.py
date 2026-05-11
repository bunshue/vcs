from machine import Pin, PWM
import utime 

led_pwm = PWM(Pin(15))

while True:
    for i in range(0, 1024, 10):   #  從0至1023
        led_pwm.duty(i)
        utime.sleep(0.01)
    for i in range(1023, -1, -10): #  從1023至0
        led_pwm.duty(i)
        utime.sleep(0.01)
        