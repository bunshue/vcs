# ch28_27.py
import pyautogui
import time

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
pyautogui.hotkey('shift', '8')     # 輸出 *
pyautogui.hotkey('alt', 'V')       # 開啟檢視功能表




