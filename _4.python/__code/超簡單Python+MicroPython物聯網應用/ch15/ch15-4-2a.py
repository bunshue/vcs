from machine import Pin, PWM
from hcsr04 import HCSR04
import xtools as xtools
import utime

sensor = HCSR04(trigger_pin=11, echo_pin=10)
led = PWM(Pin(15, Pin.OUT))
led.freq(1000)

while True: 
    distance = sensor.distance_cm()
    if distance < 5:
        led.duty_u16(0)
    elif distance > 40:
        led.duty_u16(65535)
    else:
        pwm = xtools.map_range(distance, 5, 40, 0, 65535)
        print(distance, "cm ", pwm)
        led.duty_u16(pwm)
    utime.sleep(0.2)
    
