import pyautogui
from PIL import ImageGrab
import time

x1, x2 = 260, 300
y1_bird, y2_bird = 305, 378
y1_cactus, y2_cactus = 379, 465
def isCollision_day(data):  #白天
    #檢查高飛翼手龍出現
    for i in range(x1, x2):
        for j in range(y1_bird, y2_bird):
            if data[i, j] < 150:
                pyautogui.keyDown("down")
                time.sleep(0.3)
                pyautogui.keyUp("down")
                return
    #檢查仙人掌出現
    for i in range(x1, x2):
        for j in range(y1_cactus, y2_cactus):
            if data[i, j] < 150:
                pyautogui.keyDown("up")
                return
    return

def isCollision_night(data):  #晚上
    for i in range(x1, x2):
        for j in range(y1_bird, y2_bird):
            if data[i, j] > 150:
                pyautogui.keyDown("down")
                time.sleep(0.3)
                pyautogui.keyUp("down")
                return
    for i in range(x1, x2):
        for j in range(y1_cactus, y2_cactus):
            if data[i, j] > 150:
                pyautogui.keyDown("up")
                return
    return

time.sleep(10)
pyautogui.keyDown("up")

while True:
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    if data[260, 300] > 150:
        isCollision_day(data)
    else:
        isCollision_night(data)

