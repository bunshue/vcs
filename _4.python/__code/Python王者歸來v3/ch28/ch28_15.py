# ch28_15.py
import pyautogui
import time

time.sleep(10)      # 這10秒需要繪圖視窗取得焦點,選擇畫筆和選擇顏色
pyautogui.click()   # 按一下設定繪圖起始點                     
displacement = 10
while displacement < 300:
    pyautogui.dragRel(displacement, 0, duration=0.2)
    pyautogui.dragRel(0, displacement, duration=0.2)
    pyautogui.dragRel(-displacement, 0, duration=0.2)
    pyautogui.dragRel(0, -displacement, duration=0.2)
    displacement += 10





