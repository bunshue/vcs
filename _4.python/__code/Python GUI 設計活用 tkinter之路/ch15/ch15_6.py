# ch15_6.py
from tkinter import *
from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()
root.title("ch15_6")

pb = Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()












