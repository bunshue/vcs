from machine import Pin
from time import sleep

# 設定GPIO2為輸出模式，並設為初始狀態熄滅
led = Pin(2, Pin.OUT)
led.value(1)

while True:
    # LED點亮（輸出為0）
    led.value(0)
    sleep(1)  # 亮1秒鐘
    
    # LED熄滅（輸出為1）
    led.value(1)
    sleep(0.5)  # 暫停0.5秒鐘
