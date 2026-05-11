from machine import Pin, PWM
import utime 

pin = Pin(12, Pin.OUT)
#led_pwm = PWM(pin, freq=1000, duty=0)
led_pwm = PWM(pin)
led_pwm.freq(1000)
led_pwm.duty_u16(0)
utime.sleep(1)
led_pwm.duty_u16(16384)  # 25%
utime.sleep(1)
led_pwm.duty_u16(32768)  # 50%
utime.sleep(1)
led_pwm.duty_u16(49152)  # 75%
utime.sleep(1)
led_pwm.duty_u16(65535) # 100%
utime.sleep(1)
led_pwm.duty_u16(0)    # 0%
