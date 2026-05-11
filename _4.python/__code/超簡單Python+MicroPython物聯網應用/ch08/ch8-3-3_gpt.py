from machine import Pin
import time

# 計數器初始化
counter = 0

# 設置GPIO4為輸入引腳，並啟用內部上拉電阻
button = Pin(4, Pin.IN, Pin.PULL_UP)

# 上次按鍵狀態初始化
last_button_state = button.value()

while True:
    # 讀取當前按鍵狀態
    button_state = button.value()
    
    # 檢查按鍵狀態變化
    if last_button_state == 1 and button_state == 0:
        # 按鍵從未按下變為按下時，計數器加1
        counter += 1
        print("目前計數值:", counter)
    
    # 更新上次按鍵狀態
    last_button_state = button_state
    
    # 小延遲，避免過於頻繁檢查按鍵狀態
    time.sleep(0.05)
