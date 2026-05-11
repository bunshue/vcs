from machine import Pin, PWM
import time

pwm = PWM(Pin(12))
pwm.freq(50)

maxDuty = 9000
minDuty = 1000

def setServoDuty(duty):
    pwm.duty_u16(duty)
    time.sleep(0.01)

while True:
    for pos in range(minDuty, maxDuty, 50):
        setServoDuty(pos)
    for pos in range(maxDuty, minDuty, -50):
        setServoDuty(pos)
        