import utime
from machine import Pin

# 設定LED引腳
led = Pin(2, Pin.OUT)

# 定義blink函式
def blink(times, interval):
    for _ in range(times):
        v = not led.value()
        print("狀態值", v)
        led.value(v)
        utime.sleep(interval)
    # 確保LED在結束後保持熄滅狀態
    led.value(1)

# 主迴圈
while True:
    blink(10, 0.5)
    blink(5, 1.5)

