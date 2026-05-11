from machine import Pin, PWM
import utime

# 定義PWM
red_led_pwm = PWM(Pin(15))
green_led_pwm = PWM(Pin(12))

def breathe_led(led_pwm):
    # LED 亮度漸增
    for i in range(0, 1024, 10):
        led_pwm.duty(i)
        utime.sleep(0.01)
    # LED 亮度漸減
    for i in range(1023, -1, -10):
        led_pwm.duty(i)
        utime.sleep(0.01)

while True:
    # 顯示紅色LED的呼吸燈效果
    breathe_led(red_led_pwm)
    # 顯示綠色LED的呼吸燈效果
    breathe_led(green_led_pwm)
