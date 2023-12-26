# ch28_19.py
import pyautogui

screenImage = pyautogui.screenshot()
x, y = 200, 200
print(screenImage.getpixel((x,y)))


