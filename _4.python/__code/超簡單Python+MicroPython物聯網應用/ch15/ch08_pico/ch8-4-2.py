from machine import Pin, PWM
import utime

pin = Pin(15, Pin.OUT)
# led_pwm = PWM(pin, freq=1000, duty=512)
led_pwm = PWM(pin)
led_pwm.freq(1000)
led_pwm.duty_u16(32768)
utime.sleep(1)
led_pwm.deinit()
