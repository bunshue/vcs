from time import sleep
def toTarget(servo, current, target):
    toGo = current
    increment = 0.1
    if current < target:
        while toGo < target:
            toGo = toGo + increment
            servo.ChangeDutyCycle(toGo)
            sleep(0.02)
    else:
        while toGo > target:
            toGo = toGo - increment
            servo.ChangeDutyCycle(toGo)
            sleep(0.02)
