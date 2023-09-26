import pyautogui
import time

print('3秒後, 以記事本開啟<selenium.txt>檔案，並將視窗放到最大')
print('視窗大小不合')

time.sleep(3)
pyautogui.click(x=20, y=31, button='left')  #點選檔案功能表
pyautogui.leftClick(x=400, y=116, duration=2)  #在空白處點擊滑鼠左鍵
pyautogui.click(x=600, y=130, duration=2, button='right')  #按滑鼠右鍵
pyautogui.doubleClick(x=755, y=48, duration=2, button='left')  #雙擊滑鼠左鍵
