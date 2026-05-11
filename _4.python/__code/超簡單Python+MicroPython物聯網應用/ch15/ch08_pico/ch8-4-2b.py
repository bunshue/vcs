from machine import Pin, PWM
import utime 

led_pwm = PWM(Pin(15))
led_pwm.freq(1000)
while True:
    for i in range(0, 65536, 10):   #  從0至65536
        led_pwm.duty_u16(i)
        utime.sleep(0.01)
    for i in range(65535, -1, -10): #  從65536至0
        led_pwm.duty_u16(i)
        utime.sleep(0.01)
        