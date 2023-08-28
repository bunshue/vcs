import pyautogui
import time

print('請打開 https://canvas.apps.chrome/，並挑選你喜歡的畫筆顏色及粗細')
time.sleep(10)
pyautogui.moveTo(x=570, y=552)
pyautogui.dragRel(xOffset=582, yOffset=-198, duration=3, button='left')
pyautogui.dragRel(xOffset=-38, yOffset=441, duration=3, button='left')
pyautogui.dragRel(xOffset=-544, yOffset=-243, duration=3, button='left')