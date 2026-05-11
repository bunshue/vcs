import machine
import time

# 設置GPIO15為輸出引腳
led = machine.Pin(15, machine.Pin.OUT)

# 無限循環，讓LED每隔1秒鐘閃爍一次
while True:
    led.value(1)  # 打開LED
    time.sleep(1)  # 等待1秒鐘
    led.value(0)  # 關閉LED
    time.sleep(1)  # 再等待1秒鐘
