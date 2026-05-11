from machine import Pin
import time

# 設置GPIO15為輸出引腳
led = Pin(15, Pin.OUT)

def blink(interval):
    while True:
        led.value(1)  # 打開LED
        time.sleep(interval)  # 等待指定的秒數
        led.value(0)  # 關閉LED
        time.sleep(interval)  # 再等待指定的秒數

# 調用blink函式，設置間隔時間為1秒
blink(1)
