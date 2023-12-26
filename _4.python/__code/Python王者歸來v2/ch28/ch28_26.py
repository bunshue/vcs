# ch28_26.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)
# 以下輸出*
pyautogui.keyDown('shift')
pyautogui.press('8')
pyautogui.keyUp('shift')
# 以下開啟說明功能表
pyautogui.keyDown('alt')
pyautogui.press('H')
pyautogui.keyUp('alt')




