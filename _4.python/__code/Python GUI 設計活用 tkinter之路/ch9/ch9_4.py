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















