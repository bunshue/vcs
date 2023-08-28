import pyautogui
import time

pyautogui.PAUSE = 1
print('以記事本開啟新檔案，並將輸入線移到其中')
time.sleep(10)
pyautogui.typewrite(message='Welcome to PyAutoGUI!\n')
pyautogui.typewrite(message='Welcome to PyAutoGUI!', interval=0.3)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'v')
