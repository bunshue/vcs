import pyautogui
import time

time.sleep(2)
stime = time.time()
print('Game Start')
while time.time()-stime < 10:
	pyautogui.click(x=1030, y=419, button='left')
	# pyautogui.doubleClick(x=1030, y=419, button='left')	
print('Game Over')