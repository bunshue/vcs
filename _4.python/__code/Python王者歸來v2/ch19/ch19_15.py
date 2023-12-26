# ch19_15.py
from tkinter import *
def bgUpdate(source):
    ''' 更改畫布背景顏色 '''
    red = rSlider.get()                                 # 讀取red值
    green = gSlider.get()                               # 讀取green值
    blue = bSlider.get( )                               # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))      # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)      # 將顏色轉成16進位字串
    canvas.config(bg=myColor)                           # 設定畫布背景顏色
    
tk = Tk()
canvas = Canvas(tk, width=640, height=240)              # 初始化背景
rSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
bSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                        # 設定green是125
rSlider.grid(row=0, column=0)                           
gSlider.grid(row=0, column=1)                           
bSlider.grid(row=0, column=2)                           
canvas.grid(row=1, column=0, columnspan=3)              
mainloop()















