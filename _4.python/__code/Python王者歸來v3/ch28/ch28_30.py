# ch28_30.py
import pyautogui

# 截取屏幕的一部分
screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))  # x, y, 寬度, 高度
screenshot.save('screenshot.png')

