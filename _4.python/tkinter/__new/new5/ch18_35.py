# ch18_35.py
from tkinter import *

def printInfo():
    print(slider1.get(),slider2.get())
    
window = Tk()
window.title("ch18_35")             # 視窗標題

slider1 = Scale(window,from_=0,to=10)
slider1.pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL)
slider2.set(3)                      # 設定水平尺度值
slider2.pack()
Button(window,text="Print",command=printInfo).pack()

window.mainloop()






