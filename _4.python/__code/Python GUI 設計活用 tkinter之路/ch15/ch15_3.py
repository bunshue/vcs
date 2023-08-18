# ch15_3.py
from tkinter import *
from tkinter.ttk import *
 
def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    loading()
def loading():                      # 模擬下載資料
    global bytes
    bytes += 500                    # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
 
root = Tk()
root.title("ch15_3")
bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()












