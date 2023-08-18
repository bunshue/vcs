# ch14_5.py
from tkinter import *

pw = PanedWindow(orient=HORIZONTAL)     # 建立外層PanedWindow
pw.pack(fill = BOTH,expand=True)

entry = Entry(pw,bd=3)                  # 建立entry            
pw.add(entry)                           # 這是外層PanedWindow的子物件

# 建立PanedWindow物件pwin,這是外層PanedWindow的子物件
pwin = PanedWindow(pw,orient=VERTICAL)  
pw.add(pwin)                            
# 建立Scale,這是pwin物件的子物件
scale = Scale(pwin,orient=HORIZONTAL)   
pwin.add(scale)                         

pw.mainloop()











