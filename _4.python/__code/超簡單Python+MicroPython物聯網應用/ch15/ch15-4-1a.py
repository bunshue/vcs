from machine import Pin, PWM, ADC
import time

adc = ADC(Pin(26))
servo = PWM(Pin(12))
servo.freq(50)

def getServoDuty(degrees, maxDuty=9000, minDuty=1000):
    if degrees > 180: degrees = 180
    if degrees < 0: degrees = 0
    servoDuty = minDuty+(maxDuty-minDuty)*(degrees/180)
    return int(servoDuty)

while True:
    value = adc.read_u16()
    pot_degrees = int(180 * value / 65536)
    servo_duty = getServoDuty(pot_degrees)
    print(value, pot_degrees, servo_duty)
    servo.duty_u16(servo_duty)
    time.sleep(0.01)
