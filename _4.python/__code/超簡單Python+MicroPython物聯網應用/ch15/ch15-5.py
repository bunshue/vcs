from machine import Pin, PWM
from hcsr04 import HCSR04
import xtools as xtools
import utime

sensor = HCSR04(trigger_pin=11, echo_pin=10)
tempo = 8
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523
}
beeper = PWM(Pin(13, Pin.OUT))
beeper.freq(1000)
beeper.duty_u16(32768)
melody = 'cdefgabC'

while True: 
    distance = sensor.distance_cm()
    print('%scm' % distance)
    if distance >= 5 and distance <= 50:
        index = xtools.map_range(distance, 5, 50, 0, 8)
        if index > 7:
            index = 7
        if index < 0:
            index = 0
        print(index)    
        beeper.freq(tones[melody[index]])
    utime.sleep(tempo/8)
    