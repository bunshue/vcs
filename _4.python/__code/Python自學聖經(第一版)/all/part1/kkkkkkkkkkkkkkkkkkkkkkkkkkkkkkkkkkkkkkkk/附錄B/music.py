from machine import Pin, PWM
import time

pitches = {
    'C':261, # D0
    'D':294, # Re
    'E':329, # Mi
    'F':349, # Fa
    'G':392, # So
    'A':440, # La
    'B':493, # Si
    'S':0    # Stop
}

music = (
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',1)
)

speed=400 # 設定節拍速度
period=10 # 設定每拍停頓時間

buzzer = PWM(Pin(14, Pin.OUT), duty=1000) # D5
try:
    for tone,tempo in music:
        if (tone=="S"):
            buzzer.duty(0) # 靜音
        else:
            buzzer.duty(1000)
            buzzer.freq(pitches[tone])
        time.sleep_ms(tempo*speed)
        print(pitches[tone])
        #以靜音設定每拍間稍為停頓
        buzzer.duty(0)         # 靜音
        time.sleep_ms(period)  # 停頓時間
    buzzer.deinit()
except:  # CTRL + C 中斷
    buzzer.deinit()       
