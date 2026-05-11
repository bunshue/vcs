from machine import Pin, PWM
import utime 

ledR = PWM(Pin(15))
ledG = PWM(Pin(12))
ledB = PWM(Pin(13))

def map_range(x, in_min, in_max, out_min, out_max):
    return int((x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)

def rgb(r, g, b):
   ledR.duty(map_range(r, 0, 255, 0, 1023))
   ledG.duty(map_range(g, 0, 255, 0, 1023))
   ledB.duty(map_range(b, 0, 255, 0, 1023))

def led_off():
   ledR.duty(0)
   ledG.duty(0)
   ledB.duty(0)

led_off()
rgb(255, 0, 0)
utime.sleep(1)
led_off()
rgb(0, 255, 0)
utime.sleep(1)
led_off()
rgb(0, 0, 255)
utime.sleep(1)
led_off()
rgb(255, 255, 255)
utime.sleep(1)
led_off()
rgb(255, 255, 0)
utime.sleep(1)
led_off()
