import RPi.GPIO as GPIO
from time import sleep
import random
stepAngle = 0.0879   # stepping angle of 28BYJ-48 stepping motor
speed = 0.0001
CW = False
CCW = True
# Pin number for phase A, B, C, D
phaseAPin = 18
phaseBPin = 23
phaseCPin = 24
phaseDPin = 25
buttonPin = 12
LEDPin = 16
phasePin = (phaseAPin, phaseBPin, phaseCPin, phaseDPin)
debounce = 0
maxDebounce = 500
phase = [[1,0,0,0] ,[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
def stepping(direction, steps):
    STEP = steps%8
    while steps > 0:
        sleep(speed)
        if direction == CCW:
            STEP = 7 - STEP
        stepPhase(STEP)
        steps = steps - 1
        STEP = steps%8
        sleep(0.001)
def stepPhase(STEP):
    for i in range(0,4):
        GPIO.output(phasePin[i],phase[STEP][i])  
def rotation(direction, angle):
    stepToGo = int(float(angle)/stepAngle)
    stepping(direction, stepToGo)    
GPIO.setmode(GPIO.BCM)
for i in range(0,4):
    GPIO.setup(phasePin[i], GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDPin, GPIO.OUT, initial=False)
randNo = [0, 0, 0]
try:
    while True:
        if GPIO.input(buttonPin) == 0:
            if debounce > maxDebounce:
                debounce = 0
                GPIO.output(LEDPin, True)
                msg = "3 random numbers = "
                for i in range(3):
                    randNo[i] = random.randint(0, 36)
                    msg = msg + str(randNo[i]) + " "
                print(msg)
                for i in range(3):
                    angleToGo=randNo[i]*10+5
                    rotation(CCW, angleToGo)
                    sleep(1)
                    rotation(CW, angleToGo)
                    sleep(1)
                while GPIO.input(buttonPin) == 0:
                    pass
            else:
                debounce += 1
        GPIO.output(LEDPin, False)
except KeyboardInterrupt:
    print("Exit!")
finally:
    GPIO.cleanup() 
