# ch9_2.py
from tkinter import *
    
root = Tk()
root.title("ch9_2")                     # 視窗標題

slider = Scale(root,
               from_=0,                 # 起點值
               to=10,                   # 終點值
               troughcolor="yellow",    # 槽的顏色
               width="30",              # 槽的高度
               tickinterval=2,          # 刻度
               label="My Scale",        # Scale標籤
               length=300,              # Scale長度
               orient=HORIZONTAL)       # 水平
slider.pack()

root.mainloop()






