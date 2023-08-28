import pyautogui

pyautogui.moveTo(x=400, y=100)
pyautogui.moveTo(x=700, y=300, duration=3, tween=pyautogui.linear)
pyautogui.moveTo(x=100, y=300, duration=3, tween=pyautogui.easeInQuad)
pyautogui.moveTo(x=400, y=100, duration=3, tween=pyautogui.easeOutQuad)
