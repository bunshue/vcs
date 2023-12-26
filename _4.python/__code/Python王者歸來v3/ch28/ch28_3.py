# ch28_3.py
import pyautogui

xloc = 0
while xloc < 1000:
    xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
    print(xloc, yloc)                    # 列印滑鼠游標位置

