# ch15_4.py
from tkinter import *
from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:        
        pb.step(2)
        root.update()               # 更新畫面
        print(pb.cget("value"))     # 列印指針值
        time.sleep(0.05)
 
root = Tk()
root.title("ch15_4")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()












