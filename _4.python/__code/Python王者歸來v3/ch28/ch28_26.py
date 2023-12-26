# ch28_26.py
import pyautogui
import time

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
# 以下輸出*
pyautogui.keyDown('shift')
pyautogui.press('8')
pyautogui.keyUp('shift')
# 以下開啟檢視功能表
pyautogui.keyDown('alt')
pyautogui.press('V')
pyautogui.keyUp('alt')




