# ch28_6.py
import pyautogui

xloc = 0
print('按Ctrl-C 可以中斷本程式')
try:
    while xloc < 1000:
        xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
        print(xloc, yloc)                    # 列印滑鼠游標位置
except KeyboardInterrupt:
    print('\nBye')



