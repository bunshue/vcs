import pyautogui
import time

print('以記事本開啟新檔案，並將輸入線移到其中')
time.sleep(10)
pyautogui.press('g')
pyautogui.press('o', presses=2)
pyautogui.press('d')
pyautogui.press('enter')
time.sleep(1)
pyautogui.keyDown('shift')
pyautogui.press('g')
pyautogui.press('o', presses=2)
pyautogui.press('d')
pyautogui.keyUp('shift')
