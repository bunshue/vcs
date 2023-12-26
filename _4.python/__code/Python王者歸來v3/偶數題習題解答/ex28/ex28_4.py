# ex28_4.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.typewrite('Ming-Chi Institute of Technology', 0.1)
pyautogui.typewrite(['enter'],0.1)
pyautogui.typewrite('Department of Artificial Intelligence', 0.1)
pyautogui.typewrite(['enter'],0.1)
pyautogui.typewrite('Name : Jiin-Kwei Hung', 0.1)















