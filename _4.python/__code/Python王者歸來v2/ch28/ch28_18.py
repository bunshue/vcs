# ch28_18.py
import pyautogui

screenImage = pyautogui.screenshot()
cropPict = screenImage.crop((960,210,1900,480))
cropPict.save("out28_18.jpg")







