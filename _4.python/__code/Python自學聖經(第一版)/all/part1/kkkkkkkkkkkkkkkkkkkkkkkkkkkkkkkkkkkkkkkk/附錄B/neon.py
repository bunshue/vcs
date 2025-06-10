from machine import Pin,PWM
import time
import random
 
pwmR = PWM(Pin(13),freq=1000) #D7 紅燈
pwmG = PWM(Pin(14),freq=1000) #D5 綠燈
pwmB = PWM(Pin(12),freq=1000) #D6 藍燈

while True:
    R= random.randint(0,1023) # 產生 0~1023 的亂數
    G= random.randint(0,1023) # 產生 0~1023 的亂數
    B= random.randint(0,1023) # 產生 0~1023 的亂數

    pwmR.duty(R)
    time.sleep(0.1)
    pwmG.duty(G)
    time.sleep(0.1)
    pwmB.duty(B)
    time.sleep(0.1)    
    print(R,G,B)


