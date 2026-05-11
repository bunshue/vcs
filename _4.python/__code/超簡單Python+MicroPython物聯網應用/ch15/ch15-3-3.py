from machine import Pin, PWM
import time

pwm = PWM(Pin(15))
pwm.freq(1000)
while True:
    duty = int(input("輸入亮度值(0~100):"))
    bright = int(duty*655.35)
    print("勤務循環值:", bright)
    pwm.duty_u16(bright)
    time.sleep(1)
