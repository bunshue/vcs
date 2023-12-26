# ch28_4.py
import pyautogui

x, y = 300, 300
for i in range(5):
    pyautogui.moveTo(x, y, duration=0.5)              # 左上角
    pyautogui.moveTo(x+1200, y, duration=0.5)         # 右上角
    pyautogui.moveTo(x+1200, y+400, duration=0.5)     # 右下角
    pyautogui.moveTo(x, y+400, duration=0.5)          # 左下角


