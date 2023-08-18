# ch8_2.py
from tkinter import *

root = Tk()
root.title("ch8_2")

# 用字典儲存框架顏色與游標外形
fms = {'red':'cross','green':'boat','blue':'clock'}
for fmColor in fms:         # 建立3個不同底色的框架與游標外形
    Frame(root,bg=fmColor,cursor=fms[fmColor],
          height=50,width=200).pack(side=LEFT)

root.mainloop()








