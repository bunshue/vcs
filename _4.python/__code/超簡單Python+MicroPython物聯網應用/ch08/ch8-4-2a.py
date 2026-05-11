from machine import Pin, PWM
import utime 

pin = Pin(12, Pin.OUT)
led_pwm = PWM(pin, freq=1000, duty=0)
utime.sleep(1)
led_pwm.duty(255)  # 25%
utime.sleep(1)
led_pwm.duty(512)  # 50%
utime.sleep(1)
led_pwm.duty(768)  # 75%
utime.sleep(1)
led_pwm.duty(1023) # 100%
utime.sleep(1)
led_pwm.duty(0)    # 0%
