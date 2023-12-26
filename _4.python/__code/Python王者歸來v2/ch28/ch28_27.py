# ch28_27.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)
pyautogui.hotkey('shift', '8')     # 輸出*
pyautogui.hotkey('alt', 'H')       # 開啟說明功能表




