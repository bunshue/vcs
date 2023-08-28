import pyautogui

pyautogui.moveTo(x=400, y=100)
pyautogui.moveRel(xOffset=300, yOffset=200, duration=3, tween=pyautogui.linear)
pyautogui.moveRel(xOffset=-600, yOffset=0, duration=3, tween=pyautogui.easeInQuad)
pyautogui.moveRel(xOffset=300, yOffset=-200, duration=3, tween=pyautogui.easeOutQuad)
