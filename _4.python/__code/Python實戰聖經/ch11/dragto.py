import pyautogui
import time

print('請打開 https://canvas.apps.chrome/，並挑選你喜歡的畫筆顏色及粗細')
time.sleep(10)
pyautogui.moveTo(x=570, y=552)
pyautogui.dragTo(x=1152, y=354, duration=3, button='left')
pyautogui.dragTo(x=1114, y=795, duration=3, button='left')
pyautogui.dragTo(x=570, y=552, duration=3, button='left')
