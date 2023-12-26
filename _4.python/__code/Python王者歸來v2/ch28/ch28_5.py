# ch28_5.py
import pyautogui
                   
for i in range(5):
    pyautogui.moveRel(300, 0, duration=0.5)     # 往右上角移動
    pyautogui.moveRel(0, 300, duration=0.5)     # 往右下角移動
    pyautogui.moveRel(-300, 0, duration=0.5)    # 往左下角移動
    pyautogui.moveRel(0, -300, duration=0.5)    # 往左上角移動





