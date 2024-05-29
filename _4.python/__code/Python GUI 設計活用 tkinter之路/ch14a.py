"""
使用 PanedWindow()

"""
import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

pw = PanedWindow(orient=VERTICAL)       # 建立PanedWindow物件
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")         # 建立標籤Top Pane
pw.add(top)                             # top標籤插入PanedWindow

bottom = Label(pw,text="Bottom Pane")   # 建立標籤Bottom Pane
pw.add(bottom)                          # bottom標籤插入PanedWindow

pw.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe)                       # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe)                     # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe)                      # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=1)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=1)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=2)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=2)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

