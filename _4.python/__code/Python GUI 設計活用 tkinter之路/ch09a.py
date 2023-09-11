import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch9_1")             # 視窗標題

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL).pack()

window.mainloop()







#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_2.py

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







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_3.py

# ch9_3.py
from tkinter import *

def printInfo():
    print("垂直捲軸值 = %d, 水平捲軸值 = %d" % (sV.get(),sH.get()))
    
root = Tk()
root.title("ch9_3")                           # 視窗標題

sV = Scale(root,label="垂直",from_=0,to=10)   # 建立垂直卷軸
sV.set(5)                                     # 設定垂直卷軸初值是5
sV.pack()

sH = Scale(root,label="水平",from_=0,to=10,   # 建立水平卷軸
                length=300,orient=HORIZONTAL)
sH.set(3)                                     # 設定水平捲軸初值是3
sH.pack()

Button(root,text="Print",command=printInfo).pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_4.py

# ch9_4.py
from tkinter import *

def bgUpdate(source):
    ''' 更改視窗背景顏色 '''
    red = rSlider.get()                             # 讀取red值
    green = gSlider.get()                           # 讀取green值
    blue = bSlider.get( )                           # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    root.config(bg=myColor)                         # 設定視窗背景顏色
    
root = Tk()
root.title("ch9_4")
root.geometry("360x240")

rSlider = Scale(root, from_=0, to=255, command=bgUpdate)
gSlider = Scale(root, from_=0, to=255, command=bgUpdate)
bSlider = Scale(root, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                    # 設定green初值是125
rSlider.grid(row=0, column=0)                       # row=0, col=0
gSlider.grid(row=0, column=1)                       # row=0, col=1
bSlider.grid(row=0, column=3)                       # row=0, col=2

root.mainloop()
















print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_4_1.py

# ch9_4_1.py
from tkinter import *
from tkinter.colorchooser import *

def bgUpdate():
    ''' 更改視窗背景顏色 '''
    myColor = askcolor()            # 列出色彩對話方塊
    print(type(myColor),myColor)    # 列印傳回值
    root.config(bg=myColor[1])      # 設定視窗背景顏色
        
root = Tk()
root.title("ch9_4_1")
root.geometry("360x240")

btn = Button(text="Select Color",command=bgUpdate)
btn.pack(pady=5)

root.mainloop()
















print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_5.py

# ch9_5.py
from tkinter import *
def bgUpdate(source):
    ''' 更改視窗背景顏色 '''
    red = rSlider.get()                             # 讀取red值
    green = gSlider.get()                           # 讀取green值
    blue = bSlider.get( )                           # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))  # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)  # 將顏色轉成16進位字串
    root.config(bg=myColor)                         # 設定視窗背景顏色
    
root = Tk()
root.title("ch9_5")
root.geometry("360x240")

fm = Frame(root)                                    # 建立框架
fm.pack()                                           # 自動安置在上方中央

rSlider = Scale(fm, from_=0, to=255, command=bgUpdate)
gSlider = Scale(fm, from_=0, to=255, command=bgUpdate)
bSlider = Scale(fm, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                    # 設定green初值是125
rSlider.grid(row=0, column=0)                       # row=0, col=0
gSlider.grid(row=0, column=1)                       # row=0, col=1
bSlider.grid(row=0, column=3)                       # row=0, col=2

root.mainloop()
















print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_6.py

# ch9_6.py
from tkinter import *
    
root = Tk()
root.title("ch9_6")             # 視窗標題
root.geometry("300x100")
spin = Spinbox(root,from_=10,to=30,increment=2)
spin.pack(pady=20)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_7.py

# ch9_7.py
from tkinter import *

def printInfo():        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_7")

sp = Spinbox(root,from_ = 0,to = 10,           
             command = printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_8.py

# ch9_8.py
from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_8")

sp = Spinbox(root,
             values=(10,38,170,101),    # 以元組儲存數值
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch09\ch9_9.py

# ch9_9.py
from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("ch9_9")
cities = ("新加坡","上海","東京")       # 以元組儲存數值

sp = Spinbox(root,
             values=cities,    
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()







print('------------------------------------------------------------')	#60個
已複製資料到系統剪貼簿

