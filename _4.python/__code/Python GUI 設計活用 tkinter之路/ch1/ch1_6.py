# ch1_6.py
from tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()      # 螢幕寬度
screenHeight = root.winfo_screenheight()    # 螢幕高度
w = 300                                     # 視窗寬
h = 160                                     # 視窗高
x = (screenWidth - w) / 2                   # 視窗左上角x軸位置
y = (screenHeight - h ) / 2                 # 視窗左上角Y軸位置
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.mainloop()




