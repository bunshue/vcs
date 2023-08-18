# ch14_1.py
from tkinter import *
    
pw = PanedWindow(orient=VERTICAL)       # 建立PanedWindow物件
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")         # 建立標籤Top Pane
pw.add(top)                             # top標籤插入PanedWindow

bottom = Label(pw,text="Bottom Pane")   # 建立標籤Bottom Pane
pw.add(bottom)                          # bottom標籤插入PanedWindow

pw.mainloop()











