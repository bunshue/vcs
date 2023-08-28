import pyautogui
import time

print('請開啟小算盤')
time.sleep(5)

num = '2021'
for n in num:
    box = pyautogui.locateOnScreen(n + '.png', grayscale=True)
    if box:
        x, y = pyautogui.center(box)
        pyautogui.leftClick(x, y)
    else:
        print('找不到圖片')

screen = pyautogui.screenshot()
screen.save('screenshot.png')