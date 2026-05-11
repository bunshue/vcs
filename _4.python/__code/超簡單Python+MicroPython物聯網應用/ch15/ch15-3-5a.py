from machine import Pin, PWM
import time

tempo = 5
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
beeper = PWM(Pin(13))
beeper.freq(1000)
beeper.duty_u16(32768)
melody = 'cdefgabC'

for tone in melody:
    beeper.freq(tones[tone])
    time.sleep(tempo/8)
beeper.deinit()
