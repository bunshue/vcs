# ch28_20.py
import pyautogui

x, y = 200, 200
trueFalse = pyautogui.pixelMatchesColor(x,y,(255,255,255))
print(trueFalse)
trueFalse = pyautogui.pixelMatchesColor(x,y,(0,0,255))
print(trueFalse)





