from machine import Pin, PWM
import time

beeper = PWM(Pin(13))
beeper.freq(440)
beeper.duty_u16(32768)
time.sleep(1)
beeper.freq(1047)
beeper.duty_u16(3200)
time.sleep(1)
beeper.freq(200)
beeper.duty_u16(6400)
time.sleep(1)
beeper.duty_u16(0)
beeper.deinit()
