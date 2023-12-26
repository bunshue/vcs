# ch28_16.py
import pyautogui
import time

for i in range(1,10):
    pyautogui.scroll(30)    # 往上捲動      
    time.sleep(1)
    pyautogui.scroll(-30)   # 往下捲動
    time.sleep(1)






