from machine import Pin, PWM
import time

buzzer = PWM(Pin(14, Pin.OUT), duty=900) # D5

def sound(): 
    buzzer.freq(400)
    time.sleep(0.5)
    buzzer.freq(700)
    time.sleep(0.5)

try:
    for i in range(5):
        sound()
    buzzer.deinit()
except:  # CTRL + C 中斷
    buzzer.deinit()
        
