# ch28_10.py
import pyautogui
import time

print('按Ctrl-C 可以中斷本程式')
try:
    while True:
        xloc, yloc = pyautogui.position()       # 獲得滑鼠游標位置
        xylocStr = "x= " + str(xloc).rjust(4) + " y= " + str(yloc).rjust(4)
        print(xylocStr, end="\r", flush=True)   # 設定同一行最左邊輸出
        time.sleep(1)
except KeyboardInterrupt:
    print('\nBye')


