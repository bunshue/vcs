# ch35_6.py
from tkinter import *
from pytube import YouTube

def loadVideo():                    # 列印下載資訊
    vlinks = "https//www.youtube.com/watch?v="
    vlinks = vlinks + links.get()   # 影音檔案網址
    yt = YouTube(vlinks)
    yt.streams.first().download()
    x.set("影音檔案下載完成 ...")
          
window = Tk()
window.title("ch35_6")              # 視窗標題

x = StringVar()
x.set("請輸入影音檔案序列碼")
links = StringVar()

lab1 = Label(window,text="輸入影音檔案序列碼 : ").grid(row=0)
lab2 = Label(window,text="請輸入儲存的資料夾 : ").grid(row=1)
lab3 = Label(window,textvariable=x,
             height=3).grid(row=2,column=0,columnspan=2)
             
e1 = Entry(window,textvariable=links)   # 文字方塊1
e2 = Entry(window)                      # 文字方塊2
e1.grid(row=0,column=1)                 # 定位文字方塊1
e2.grid(row=1,column=1)                 # 定位文字方塊2

btn1 = Button(window,text="下載",command=loadVideo)
btn1.grid(row=3,column=0)
btn2 = Button(window,text="結束",command=window.destroy)
btn2.grid(row=3,column=1)

window.mainloop()






