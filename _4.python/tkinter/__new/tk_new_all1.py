import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import *

print("------------------------------------------------------------")  # 60個

window = tk.Tk()  # 產生 tkinter 視窗

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
print('取得目前螢幕大小')
print(width, height)

window.destroy()  # 關閉視窗

print("------------------------------------------------------------")  # 60個

print("09-TkUI9Entry-python2")

def event1():
    label1.set("123")
	#print(entry1.get())


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)


entry1=tk.Entry(window)
entry1.pack()
btn1 =tk.Button(window,text="press me",command=event1)
btn1.pack()
v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print("09-TkUI9Entry-python3")

def event2():
    print(entry1.get())
    t1=entry1.get()
    v.set(t1)

entry1=tk.Entry(window)
entry1.pack()
btn1 =tk.Button(window,text="press me",command=event2)
btn1.pack()
v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print("TkUI_exam")

from PIL import ImageTk, Image


def event3():
	value1=entry1.get()
	print(value1)
	value2=float(value1)
	value2=value2*0.15
	print(value2)
	label1.config(text='Button Pressed')


label1 =tk.Label(window,text="Hello World!")
label1.pack()

entry1=tk.Entry(window)
entry1.pack()
btn1 =tk.Button(window,text="press me",command=event3)
btn1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print("TkUI10Entry-python3-Exam")

def event4():
    t1=float(entry1.get())
    t1=t1/30.5
    print(t1)
    v.set(str(t1))


entry1=tk.Entry(window)
entry1.pack()
btn1 =tk.Button(window,text="press me",command=event4)
btn1.pack()
v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

""" some wrong 有一點點不一樣

from __future__ import unicode_literals
from pytube import YouTube
import youtube_dl
import os

def Downmp4():
    yt = YouTube()
    yt.url = purl.get()
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    fvideo = yt.get("mp4", "360p")    
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
window=tk.Tk()
window.geometry("600x400")
window.title("MP4與MP3下載")

frame1 = tk.Frame(window, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

window.mainloop()
""" #some wrong

print("------------------------------------------------------------")  # 60個

"""
def checknum():
    pmsg.set("Small")

import random as r

window = tk.Tk()
window.geometry("400x300")
window.title("Guess Number")

ans=r.randint(0,100)
#print(ans)
#input guess number
pL1 = tk.Label(window, text="Please enter number:")
pL1.pack()
while (True):
    pnum = tk.StringVar()
    pE1 = tk.Entry(window, textvariable=pnum)
    pE1.pack()
    pB1 = tk.Button(window, text="OK", command=checknum)
    pB1.pack()

pmsg = tk.StringVar()
pL2 = tk.Label(window, textvariable=pmsg)
pL2.pack()

#num=121
#while (num!=ans):
#    num=int(input("please enter guess number:"))
#    if (num==ans):
#        break
#    if (num>ans):
#        print("bigger")
#    else:
#        print("smaller")   
#print("you win")    

window.mainloop()
"""


print("------------------------------------------------------------")  # 60個

""" syntax fail
from __future__ import unicode_literals
from pytube import YouTube

import youtube_dl
import os

def Downmp4():
    #yt = YouTube()
    #yt.url = purl.get()
    yt = YouTube('%s'%purl.get())
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    #fvideo = yt.get("mp4", "360p")    
    fvideo = yt.streams.filter(file_extension='mp4', res='360p').first()
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio'print("------------------------------------------------------------")  # 60個,
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
window=tk.Tk()
window.geometry("600x400")
window.title("MP4與MP3下載")

frame1 = tk.Frame(window, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

window.mainloop()
"""

print("------------------------------------------------------------")  # 60個

window=tk.Tk()

tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='綠', bg='green', width=20).pack()
tk.Label(window, text='藍', bg='blue', width=20).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import Tk, Frame, Button
from datetime import date #滙入datetime模組的date類別

#宣告類別
class wndApp(Frame):
    
    #方法一：初始化物件，加入主視窗版面
    def __init__(self, ruler = None):
        Frame.__init__(self, ruler)
        # 呼叫主視窗物件以pack()方法將自己加入
        self.pack()
        self.makeComponent()
        
    #方法二：定義按鈕元件的相關屬性值
    def makeComponent(self):
        self.day_is = tk.Button(self)
        
        #按鈕上欲顯示的文字
        self.day_is['text'] = '我是 按鈕\n(Click Me..)'
        
        #按下按鈕由command執行動作，此處呼叫方法display()
        self.day_is['command'] = self.display
        
        # 設定按鈕在主視窗左側，藍色文字，被按下後，關閉主視窗並做資源的釋放
        self.day_is.pack(side = 'left')
        self.QUIT = tk.Button(self, text = 'QUIT',
                fg = 'blue', command = wnd.destroy)
        # 設定按鈕在主視窗右側
        self.QUIT.pack(side = 'right')
        
    #方法三：按下按鈕後會以date類別呼叫today()顯示今天的日期
    def display(self):
        today = date.today()
        print('Day is', today)
        
window = tk.Tk()
# 實體化wndApp類別，以主視窗物件為引數做初始化動作
# 然後加入Frame元件，再由Frame加入兩個按鈕
work = wndApp(ruler = window)
work.mainloop()

print('------------------------------------------------------------')	#60個

#建立Frame子類別
class appWork(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()

#產生Frame子類別物件
work = appWork()

work.master.title('Python GUI')
work.master.maxsize(500, 250)

work.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

window.title('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = tk.Button(window, text = item, state = item)
    btn.pack()    #以元件加入主視窗

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

print('------------------------------------------------------------')	#60個

button1 = tk.Button(window, text='push1', width=20).pack()
button2 = tk.Button(window, text='push2', width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text='push3', width=20).pack(side=tk.RIGHT)

print('------------------------------------------------------------')	#60個


def yellow():                   # 設定視窗背景是黃色
    window.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    window.config(bg="blue")
    
window = tk.Tk()
# 依次建立3個鈕
exitbtn = tk.Button(window,text="Exit",command=window.destroy)
bluebtn = tk.Button(window,text="Blue",command=blue)
yellowbtn = tk.Button(window,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def bColor(bgColor):          # 設定視窗背景顏色
    window.config(bg=bgColor)
    
window = tk.Tk()

# 依次建立3個鈕
exitbtn = tk.Button(window,text="Exit",command=window.destroy)
bluebtn = tk.Button(window,text="Blue",command=lambda:bColor("blue"))
yellowbtn = tk.Button(window,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 依次建立3個鈕
exitbtn = tk.Button(window,text="Exit",command=window.destroy)
bluebtn = tk.Button(window,text="Blue",command=lambda:window.config(bg="blue"))
yellowbtn = tk.Button(window,text="Yellow",command=lambda:window.config(bg="yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def buttonClick1():
     buttonvar.set("心想事成，天天開心")

def buttonClick2():
     #改變背景顏色
     button2.config(bg = "blue")  

window = tk.Tk()
window.title("按鈕元件(Button)功能示範 Entry")
    
buttonvar = tk.StringVar() 
button1 = tk.Button(window, textvariable=buttonvar, command=buttonClick1)
buttonvar.set("按下我會有祝賀語")
button1.pack(padx=20, pady=10)

button2 = tk.Button(window, text="按我會改變按鈕背景色", command=buttonClick2)
button2.pack(padx=20, pady=10)

entry = tk.Entry(window, bg="#ffff00", font = "新細明體 16 bold" ,borderwidth = 3)
entry.insert(0,"天天")
entry.insert("2","青春永駐")
entry.insert("end"," 莫忘初心")
entry.delete(0, 2)  #刪除前面兩個字元
entry.pack(padx=20, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("Label元件的參數設定")

label = tk.Label(window, bg="#ff00ff", fg="#ffff00", \
                font =("標楷體", 14, "bold", "italic"), \
                padx=5, pady=30, text = "生日快樂")
label.pack()

label = tk.Label(window, bg="#ff00ff", fg="#ffff00", \
                font ="新細明體 14 bold italic", \
                padx=20, pady=5, text = "生日快樂")
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x100")
window.title("pack版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.pack(side="left")
minus=tk.Button(window, width=20, text="減法範例")
minus.pack(side="left")
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.pack(side="left")
divide=tk.Button(window, width=20, text="除法範例")
divide.pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

counter = 0 #儲存數值

# 自訂函式一：顯示標籤(Label)元件
def display(label):
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      label.config(text = str(counter),
         bg = 'pink', width = 20, height = 2)
      label.after(100, count) #ms
   count()
   
#設定標籤並把它放入主視窗
show = tk.Label(window, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = tk.Button(window, text = '離開', width = 20, command = window.destroy)
btnStop.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('連續建立多個button, 使用Button屬性state')

for i in range(3):
    btn = tk.Button(window, text = 'button'+str(i), state = 'normal')
    btn.pack()
for i in range(3):
    btn = tk.Button(window, text = 'button'+str(i), state = 'active')
    btn.pack()
for i in range(3):
    btn = tk.Button(window, text = 'button'+str(i), state = 'disabled')
    btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 900
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

def bless():
     btnvar.set("心想事成，天天開心")

def changecolor():
     btn2.config(bg = "blue")  

label = tk.Label(window, bg="#ff00ff", fg="#ffff00", \
                font =("標楷體", 14, "bold", "italic"), \
                padx=5, pady=30, text = "生日快樂")
label.pack()


label = tk.Label(window, bg="#ff00ff", fg="#ffff00", \
                font ="新細明體 14 bold italic", \
                padx=20, pady=5, text = "生日快樂")
label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


"""
text=tk.Text(window)
text.insert(tk.INSERT, "從入門到精通\n")
text.insert(tk.CURRENT, "Illustrator CC\n")
text.insert(tk.END, "玩轉 Ai 設計風華的16堂課")
text.pack()
text.config(state=tk.DISABLED)
"""

entry = tk.Entry(window, bg="#ffff00", font = "新細明體 16 bold" ,borderwidth = 3)
entry.insert(0,"天天")
entry.insert("2","青春永駐")
entry.insert("end"," 莫忘初心")
entry.delete(0, 2)  #刪除前面兩個字元
entry.pack(padx=20, pady=10)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
   
btnvar = tk.StringVar() 
btn1 = tk.Button(window, textvariable=btnvar, command=bless)
btnvar.set("按下我會有祝賀語")
btn1.pack(padx=20, pady=10)

btn2 = tk.Button(window, text="按我會改變按鈕背景色", command=changecolor)
btn2.pack(padx=20, pady=10)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
tk.Label(window, 
      text = "請選擇喜愛的景點: ", font = ft,
      justify = tk.LEFT, padx = 20).pack()
place = [('宜蘭', 1), ('台北', 2),
          ('高雄', 3)]
var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
                   font = ft, variable = var, padx = 20,
                   command = select).pack(anchor = tk.W)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def select():
    print('你的選項是 :', var.get())
ft = ('標楷體', 14)
tk.Label(window, 
      text = "請選擇喜愛的運動: ", font = ft,
      justify = tk.RIGHT, padx = 20).pack()
place = [('籃球', 1), ('桌球', 2),
          ('游泳', 3)]
var = tk.IntVar()
var.set(3)

for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = tk.NE)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = tk.Listbox(window, yscrollcommand = scrollbar.set )

for line in range(26):
   list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = list1.yview )

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
""" 缺檔案
def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        print("cattle的簡介 :", str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        print("deer的簡介 :", str2)
    
lb=tk.Label(window,text="請點選想了解的動物簡介:").pack()
choice=tk.IntVar()
choice.set(0)
pic1=ImageTk.PhotoImage(file="image/cattle.gif")
pic2=ImageTk.PhotoImage(file="image/deer.gif")
tk.Radiobutton(window,image=pic1,variable=choice,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=choice,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()
"""
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

""" 缺檔案
window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

# Create PhotoImage objects
caImage = tk.PhotoImage(file = "image/ca.gif")
chinaImage = tk.PhotoImage(file = "image/china.gif")
leftImage = tk.PhotoImage(file = "image/left.gif")
rightImage = tk.PhotoImage(file = "image/right.gif")
usImage = tk.PhotoImage(file = "image/usIcon.gif")
ukImage = tk.PhotoImage(file = "image/ukIcon.gif")
crossImage = tk.PhotoImage(file = "image/x.gif")
circleImage = tk.PhotoImage(file = "image/o.gif")

# frame1 to contain label and canvas
frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, image = caImage).pack(side = tk.LEFT)
canvas = tk.Canvas(frame1)
canvas.create_image(90, 50, image = chinaImage)
canvas["width"] = 200
canvas["height"] = 100
canvas.pack(side = tk.LEFT)

# frame2 to contain buttons, check buttons, and radio buttons
frame2 = tk.Frame(window)
frame2.pack()
tk.Button(frame2, image = leftImage).pack(side = tk.LEFT)
tk.Button(frame2, image = rightImage).pack(side = tk.LEFT)

tk.Checkbutton(frame2, image = usImage).pack(side = tk.LEFT)
tk.Checkbutton(frame2, image = ukImage).pack(side = tk.LEFT)

tk.Radiobutton(frame2, image = crossImage).pack(side = tk.LEFT)
tk.Radiobutton(frame2, image = circleImage).pack(side = tk.LEFT)

window.mainloop()
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個




window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab2.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab3.pack(side=tk.BOTTOM)              # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab2.pack(side=tk.BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=tk.BOTTOM)              # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.LEFT)                # 包裝與定位元件
lab2.pack(side=tk.LEFT)                # 包裝與定位元件
lab3.pack(side=tk.LEFT)                # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.LEFT)                # 包裝與定位元件
lab2.pack(side=tk.LEFT,padx=5)         # 包裝與定位元件,增加x軸間距
lab3.pack(side=tk.LEFT)                # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=tk.RIGHT)               # 包裝與定位元件
lab3.pack(side=tk.LEFT)                # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")
label.pack()                        # 包裝與定位元件
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("歡迎來到美國")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
msg_on = False                      # 全域變數預設是False    
x = tk.StringVar()                     # Label的變數內容

label = tk.Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
btn = tk.Button(window,text="Hit",command=btn_hit).pack()                   
tk.mainloop()

print("------------------------------------------------------------")  # 60個

label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")
label.pack()                        # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab2.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab3.pack(side=tk.BOTTOM)              # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.BOTTOM)              # 包裝與定位元件
lab2.pack(side=tk.BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=tk.BOTTOM)              # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.LEFT)                # 包裝與定位元件
lab2.pack(side=tk.LEFT)                # 包裝與定位元件
lab3.pack(side=tk.LEFT)                # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 =tk. Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=tk.LEFT)                # 包裝與定位元件
lab2.pack(side=tk.LEFT,padx=5)         # 包裝與定位元件,增加x軸間距
lab3.pack(side=tk.LEFT)                # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=tk.RIGHT)               # 包裝與定位元件
lab3.pack(side=tk.LEFT)                # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("歡迎來到美國")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
window = tk.Tk()

msg_on = False                      # 全域變數預設是False    
x = tk.StringVar()                     # Label的變數內容

label = tk.Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
btn = tk.Button(window,text="Hit",command=btn_hit).pack()                   

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

label=tk.Label(window,text="歡迎來到美國",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()  

window.mainloop()

print("------------------------------------------------------------")  # 60個




"""  新進待整理


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個

"""
print("------------------------------------------------------------")  # 60個
#tk.Text
print("------------------------------------------------------------")  # 60個

window = tk.Tk()

text = tk.Text(window,height=2,width=30)
text.insert(tk.END,"我懷念\n我的明志工專生活點滴")
text.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個
          
window = tk.Tk()

text = tk.Text(window,height=2,width=30)
text.insert(tk.END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(tk.END,str)
text.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

def check(): #回應核取方塊變數狀態
   print('選取的炸物有:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '請勾選要買的品項：', font = ft1)
#lb1.grid(row = 0, column = 0)
lb1.pack()
item1 = '炸雞排'
var1 = tk.StringVar()
chk = tk.Checkbutton(window, text = item1, font = ft1,
                     variable = var1, onvalue = item1, offvalue = '')
#chk.grid(row = 1, column = 0)
chk.pack()
item2 = '高麗菜'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
                   variable = var2, onvalue = item2, offvalue = '')
#chk2.grid(row = 2, column = 0)
chk2.pack()

item3 = '炸花枝'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
                   variable = var3, onvalue = item3, offvalue = '')
#chk3.grid(row = 3, column = 0)
chk3.pack()

btnQuit = tk.Button(window, text = '離開', font = ft2,
                 command = window.destroy)
#btnQuit.grid(row = 2, column = 1, pady = 4)
btnQuit.pack()

btnShow = tk.Button(window, text = '購買明細', font = ft2,
                 command = check)
#btnShow.grid(row = 2, column = 2, pady = 4)
btnShow.pack()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# label.py

window=tk.Tk()
window.geometry('300x200')
window.title('Label標籤')
window.configure(bg='white') 
tk.Label(window, text = '王之渙涼州詞', fg='blue',bg='lightblue',bitmap='gray25',\
         compound='left',font=('標楷體', 24, 'bold')).pack()
msg=('黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。')
tk.Label(window, text = msg, width=28,wraplength=240,justify='left',\
         pady=10,font=('細明體', 14)).pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個

# pack.py

window=tk.Tk()
window.geometry('300x200')
window.title('pack配置')
window.configure(bg='white')

lbl1=tk.Label(window, text = '元件版面配置',font=('微軟正黑體', 16),fg='white',bg='blue')
lbl2=tk.Label(window, text = '方法',font=('標楷體', 12))
lbl3=tk.Label(window, text = 'pack()方法',font=('標楷體', 12),bg='lightgreen')
lbl4=tk.Label(window, text = 'grid()方法',font=('標楷體', 12),bg='pink')
lbl5=tk.Label(window, text = 'place()方法',font=('標楷體', 12),bg='lightblue')
lbl1.pack(fill='x')
lbl2.pack(side='left', fill='y')
lbl3.pack(pady=5, fill='both', expand=True)
lbl4.pack(pady=5, fill='both', expand=True)
lbl5.pack(pady=5, fill='both', expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# place.py

window=tk.Tk()
window.geometry('300x200')
window.configure(bg='white') 
window.title('place配置')

lbl1=tk.Label(window, text = "五色鳥 Muller's Barbet", font=('微軟正黑體', 18),\
              fg='white',bg='black')
lbl2=tk.Label(window, text = '啄木鳥目', font=('標楷體', 16),fg='blue',bg='lightblue')
lbl3=tk.Label(window, text = '五色鳥科', font=('標楷體', 14),fg='green',bg='lightgreen')
msg='分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。'
lbl4=tk.Label(window, text = msg,font=('細明體', 12),wraplength=170)
lbl1.place(x=10,y=5,width=280,height=40)
lbl2.place(x=10,y=50,width=90,height=50)
lbl3.place(x=10,y=105,width=90,height=50)
lbl4.place(x=110,y=50,width=180,height=105)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# test.py

import random

def fnTest():
    global ans		#宣告ans為全域變數來記錄答案
    n=int(spnNum.get()) #取得使用者選擇的位數
    num=[[1,9],[10,99],[100,999]]   #用二維串列儲存各位數的亂數範圍
    r1=random.randint(num[n-1][0],num[n-1][1])
    r2=random.randint(num[n-1][0],num[n-1][1])
    if(r2>r1):	#若r2>r1就兩者互換
        r1,r2=r2,r1
    if(spnOpt.get()=='加法'):	#若選擇'加法'
        opt='+'
        ans=r1+r2
    else:
        opt='-'
        ans=r1-r2        
    lblTest.config(text='{} {} {} ='.format(r1,opt,r2))
    entAns.focus_set()
    btnTest.config(state='disable')
    btnAns.config(state='normal')
    
def fnAns():
    global ans
    userAns=int(entAns.get())
    if(userAns==ans):
        msg.set('太棒了！答案正確！')
    else:
        msg.set('答錯了！答案是：{}'.format(ans))
    btnTest.config(state='normal')
    btnAns.config(state='disable')
    
window = tk.Tk()
window.title('加減法測驗')
window.geometry('300x160')

frmTest=tk.Frame(window,relief='raised',borderwidth=2)
frmTest.pack(side='left',padx=5,pady=3)
lblTest=tk.Label(frmTest,text=' ',font=('微軟正黑體',20))
lblTest.pack(pady=5)
ans=tk.IntVar()
entAns=tk.Entry(frmTest,textvariable=ans)
entAns.pack(pady=5)
msg=tk.StringVar()
msg.set('設定後按 <出題> 鈕開始測驗')
lblMsg=tk.Label(frmTest,textvariable=msg)
lblMsg.pack(pady=5)
frmSet=tk.Frame(window,relief='raised',borderwidth=2)
frmSet.pack(side='left',padx=5,pady=3)
tk.Label(frmSet,text='運算：').pack(anchor='w')
lstOpt=['加法','減法']
spnOpt=tk.Spinbox(frmSet,values=lstOpt)
spnOpt.pack(anchor='w')
tk.Label(frmSet,text='位數：').pack(anchor='w')
spnNum=tk.Spinbox(frmSet,from_=1,to=3)
spnNum.pack(anchor='w')
btnTest=tk.Button(frmSet, text='出題', command=fnTest)
btnTest.pack(side='left',pady=3)
btnAns=tk.Button(frmSet, text='核對', command=fnAns,state='disable')
btnAns.pack(side='right',pady=3)
ans=0

window.mainloop()

print("------------------------------------------------------------")  # 60個

# bmi.py


def fnBmi():
    height = userH.get()	#用get方法取得身高
    weight = userW.get()
    bmi = round(weight / pow(height, 2), 2)
    msg=''
    if bmi < 18.5:
        msg='體重過輕！'
    elif bmi >= 24:
        msg='體重過重！'
    else :
        msg='體重剛好！'
    print('注意, 你的BMI指數為：{} {}'.format(bmi, msg))
    
window = tk.Tk()
window.title('BMI計算')
window.geometry('240x200')
window.configure(bg='white')

lblTitle = tk.Label(window, text='BMI 計算',font=('微軟正黑體', 16),fg='white',bg='blue')
lblTitle.pack(pady=10,fill='x')
tk.Label(window, text='身高(公尺，請輸入浮點數)').pack(pady=5,anchor='w')
userH=tk.DoubleVar()		#宣告userH為浮點數物件
entH = tk.Entry(window,textvariable=userH).pack()  #textvariable參數值為userH
tk.Label(window, text='體重(公斤，請輸入整數)').pack(pady=5,anchor='w')
userW=tk.IntVar()		#宣告userW為整數物件
entW = tk.Entry(window,textvariable=userW).pack()  #textvariable參數值為userW
btnCal = tk.Button(window, text=' 計算 ', command=fnBmi).pack(pady=5)
window.mainloop()

print("------------------------------------------------------------")  # 60個

# circle.py

def fnCal():
    r = userR.get()
    u=unid.get()
    if (kind.get() == '圓周長'):  		#若選取圓周長
        a=3.14*2*r
        print('圓周長為 {:.2f} {}'.format(a,u))
    else:
        a=3.14*r*r
        print('圓面積為 {:.2f} 平方{}'.format(a,u))
  
window = tk.Tk()
window.title('圓形計算')
window.geometry('300x200')

lfrmR=tk.LabelFrame(window,text='輸入半徑：')
lfrmR.pack(pady=10)
userR=tk.IntVar()
userR.set(10)
entR= tk.Entry(lfrmR,textvariable=userR).pack(pady=3)
lblMsg=tk.Label(lfrmR, text = '請輸入半徑(整數)然後選擇項目').pack(pady=10)

lfrmKind=tk.LabelFrame(window,text='計算類別')
lfrmKind.pack(side='left',pady=10,padx=10,fill='x',expand=1)
kinds=['圓周長','圓面積']
kind=tk.StringVar()
for k in kinds:
    tk.Radiobutton(lfrmKind,text=k,variable=kind,value=k,command=fnCal).pack(pady=3)
kind.set('圓周長')

lfrmUnid=tk.LabelFrame(window,text='單位')
lfrmUnid.pack(side='left',pady=10,padx=10,fill='x',expand=1)
unids=['公分','英吋']
unid=tk.StringVar()
for u in unids:
    tk.Radiobutton(lfrmUnid,text=u,variable=unid,value=u,command=fnCal).pack(pady=3)
unid.set(unids[0])  

window.mainloop()

print("------------------------------------------------------------")  # 60個

# color.py

def fnBlue():
    frmColor.config(bg='blue')

def fnRed():
    frmColor.config(bg='red')

def fnGreen():
    frmColor.config(bg='green')  
    
window = tk.Tk()

window.title('顏色切換')
window.geometry('240x200')

frmColor=tk.Frame(window,width=200,height=100,relief='raised',borderwidth=3,bg='white')
frmColor.pack(pady=5)

#建立1個 LabelFrame 在 window 下
labelFrame1=tk.LabelFrame(window,text='顏色')
labelFrame1.pack(pady=20,fill='x')

#建立3個 button 在 LabelFrame 下
button1=tk.Button(labelFrame1,text='藍色',width=8,command=fnBlue).pack(side='left',padx=5)
button2=tk.Button(labelFrame1,text='紅色',width=8,command=fnRed).pack(side='left',padx=5)
button3=tk.Button(labelFrame1,text='綠色',width=8,command=fnGreen).pack(side='left',padx=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# counter.py

num = 0
def fnAdd():
    global num		#宣告為全域變數
    num += 1		#num加1
    lblNum['text']=str(num)	#重設標籤文字
    if (num>0):		#若num大於0，就設歸零鈕可以使用
        btnClear['state']='normal'
    
def fnClear():
    global num
    num = 0
    lblNum['text']=str(num)
    btnClear['state']='disabled'  #設歸零鈕不能使用
 
window=tk.Tk()
window.geometry('300x200')
window.title('計數器')
window.configure(bg='white')

lblTitle=tk.Label(window, text = '計數器',font=('標楷體', 16),fg='white',bg='blue')
lblNum=tk.Label(window, text = '0',font=('微軟正黑體', 36))
btnAdd=tk.Button(window, text = '加 1',pady=5,padx=10,command=fnAdd)
btnClear=tk.Button(window, text = '歸零',pady=5,padx=10,command=fnClear,state='disabled')
lblTitle.pack(pady=10,fill='x')
lblNum.pack(pady=20,fill='x')
btnAdd.pack(pady=5, side='left',fill='x', expand=True)
btnClear.pack(pady=5, side='left',fill='x', expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# survey.py

def fnOk():
    lfrmSpot=tk.LabelFrame(window,text='勾選建議地點(可複選)：')
    lfrmSpot.pack(pady=10)
    for i in range(3):
        check[i]=tk.BooleanVar()	#設check[]元素值為布林值物件
        tk.Checkbutton(lfrmSpot,text=spots[i],variable=check[i]).pack(anchor='w')
def fnMsg():
    if ok.get()==True:
        msg='勾選的地點為：'
        for i in range(3):
            if check[i].get()==True:	#若check[i]元素值為True
                msg += (spots[i]+'、')	#將spots[i]元素值加入msg字串
        print('訊息 :', msg[:len(msg)-1])
    else:
        print('訊息 : 期盼下次你能參加')
    window.destroy()
    
window = tk.Tk()
window.title('旅遊問卷')
window.geometry('220x180')

ok=tk.BooleanVar()
chkOK=tk.Checkbutton(window,text='參加旅遊',variable=ok, command=fnOk).pack()
spots=['九份與金瓜石','日月潭','墾丁國家公園']
check={}
btnSend = tk.Button(window, text=' 送出 ', command=fnMsg).pack(pady=5)

window.mainloop()


print("------------------------------------------------------------")  # 60個



# grid.py

window=tk.Tk()
window.geometry('200x200')
window.title('grid配置')
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)

lbl1=tk.Label(window, text = '北',font=('標楷體', 40))
lbl2=tk.Label(window, text = '東',font=('標楷體', 40),bg='yellow')
lbl3=tk.Label(window, text = '西',font=('標楷體', 40),bg='lightgreen')
lbl4=tk.Label(window, text = '中',font=('標楷體', 40),bg='pink')
lbl5=tk.Label(window, text = '南',font=('標楷體', 40),bg='lightblue')
lbl1.grid(row=0,column=0,columnspan=2,sticky='nswe')
lbl2.grid(row=0,column=2,rowspan=2,sticky='nswe')
lbl3.grid(row=1,column=0,rowspan=2,sticky='nswe')
lbl4.grid(row=1,column=1,sticky='nswe')
lbl5.grid(row=2,column=1,columnspan=2,sticky='nswe')

window.mainloop()

print("------------------------------------------------------------")  # 60個


import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

# tkinterCheck.py

root = tk.Tk()
r = tk.StringVar()						# 使用StringVar產生字串變數用於單選框元件
r.set('1')							# 起始化變數值
radio = tk.Radiobutton(root,				# 產生單選框元件
			variable = r, 				# 設定單選框關聯的變數
			value = '1',				# 設定勾選單選框時其所關聯的變數的值，即r的值
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '2',				# 當勾選該單選框時r的值為2
			text = 'Radio2' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '3',				# 當勾選該單選框時r的值為3
			text = 'Radio3' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '4',				# 當勾選該單選框時r的值為4
			text = 'Radio4' )
radio.pack()
c = tk.IntVar()						# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(root,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,				# 設定復選框關聯的變數
			onvalue = 1,				# 當勾選復選框時，c的值為1
			offvalue = 2)				# 當未勾選復選框時，c的值為2
check.pack()

root.mainloop()
print(r.get())							# 輸出r的值
print(c.get())						# 輸出c的值

print("------------------------------------------------------------")  # 60個

# tkinterDialog.py

class MyDialog:										# 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)					# 產生Toplevel元件
        label = tk.Label(self.top, text='Please Input')	# 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)					# 產生文字框元件
        self.entry.pack()
        self.entry.focus()							# 讓文字框獲得焦點
        button = tk.Button(self.top, text='Ok',command=self.Ok)					# 設定按鈕事件處理函數
        button.pack()
    def Ok(self):									# 定義按鈕事件處理函數
        self.input = self.entry.get()						# 取得文字框中內容，儲存為input
        self.top.destroy()							# 銷毀交談視窗
    def get(self):									# 傳回在文字框輸入的內容
        return self.input

class MyButton():									# 定義按鈕類別
    def __init__(self, root, type):							# 按鈕起始化
        self.root = root							# 儲存父視窗參考
        if type == 0:								# 根據型態建立不同按鈕
            self.button = tk.Button(root, text='Create',command = self.Create)				# 設定Create按鈕的事件處理函數
        else:
            self.button = tk.Button(root, text='Quit',command = self.Quit)				# 設定Quit按鈕的事件處理函數
        self.button.pack()
    def Create(self):								# Create按鈕的事件處理函數
        d = MyDialog(self.root)							# 產生交談視窗
        self.button.wait_window(d.top)						# 等待交談視窗結束
        print('你輸入了 :' + d.get())		# 取得交談視窗中輸入值，並輸出
    def Quit(self):									# Quit按鈕的事件處理函數
        self.root.quit()							# 離開主視窗

root = tk.Tk()									# 產生主視窗

MyButton(root,0)									# 產生Create按鈕
MyButton(root,1)									# 產生Quit按鈕

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterEntry.py

root = tk.Tk()
entry1 = tk.Entry(root,						# 產生單行文字框元件
			show = '*',)					# 輸入文字框中的字元被顯示為“*”
entry1.pack()								# 將文字框新增到視窗中
entry2 = tk.Entry(root,
			show = '#',					# 輸入文字框中的字元被顯示為“#”
			width = 50)					# 將文字框的寬度設定為50
entry2.pack()
entry3 = tk.Entry(root,
			bg = 'red',					# 將文字框的背景色設定為紅色
			fg = 'blue')					# 將文字框的前景色設定為藍色
entry3.pack()
entry4 = tk.Entry(root,
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
entry4.pack()
entry5 = tk.Entry(root,
			state = tk.DISABLED)			# 將文字框設定為禁用
entry5.pack()
edit1 = tk.Text(root,						# 產生多行文字框元件
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
edit1.pack()

root.mainloop()								# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterLabel.py

root = tk.Tk()

label1 = tk.Label(root,
			anchor = tk.E,				# 設定文字的位置
			bg = 'blue',					# 設定標簽背景色
			fg = 'red',					# 設定標簽前景色
			text = 'Python',				# 設定標簽中的文字
			width = 30,					# 設定標簽的寬度為30
			height = 5)					# 設定標簽的的高度為5
label1.pack()
label2 = tk.Label(root,
			text = 'Python GUI\nTkinter',			# 設定標簽中的文字，在字串中使用換行符
			justify = tk.LEFT,				# 設定多行文字為齊左
			width = 30,
			height = 5)
label2.pack()
label3 = tk.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tk.RIGHT,			# 設定多行文字為齊右
			width = 30,
			height = 5)
label3.pack()
label4 = tk.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tk.CENTER,			# 設定多行文字為劇中對齊
			width = 30,
			height = 5)
label4.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterRCButton.py

root = tk.Tk()

r = tk.StringVar()						# 使用StringVar產生字串變數用於單選框元件
r.set('1')							# 起始化變數值
radio = tk.Radiobutton(root,				# 產生單選框元件
			variable = r, 				# 設定單選框關聯的變數
			value = '1',				# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '2',				# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '3',				# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '4',				# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()
c = tk.IntVar()						# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(root,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,				# 設定復選框關聯的變數
			indicatoron = 0,			# 將復選框繪製成按鈕型態
			onvalue = 1,				# 當勾選復選框時，c的值為1
			offvalue = 2)				# 當未勾選復選框時，c的值為2
check.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterSimpleDialog.py

import tkinter.simpledialog									# 匯入tkSimpleDialog模組

def InStr():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askstring('Python Tkinter',					# 建立字串輸入交談視窗
			'Input String',							# 指定提示字元
			initialvalue='Tkinter')						# 指定起始化文字
	print(r)									# 輸出傳回值
def InInt():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askinteger('Python Tkinter','Input Integer')			# 建立整數輸入交談視窗
	print(r)
def InFlo():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askfloat('Python Tkinter','Input Float')			# 建立浮點數輸入交談視窗
	print(r)
root = tk.Tk()
button1 = tk.Button(root,text = 'Input String',					# 建立按鈕
		command = InStr)							# 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tk.Button(root,text = 'Input Integer',
		command = InInt)							# 指定按鈕事件處理函數
button2.pack(side='left')
button2 = tk.Button(root,text = 'Input Float',
		command = InFlo)							# 指定按鈕事件處理函數
button2.pack(side='left')

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個

from tkinter import *
    
root = Tk()
root.title("")             # 視窗標題
root.geometry("300x100")
spin = Spinbox(root,from_=10,to=30,increment=2)
spin.pack(pady=20)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("")

sp = Spinbox(root,from_ = 0,to = 10,           
             command = printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("")

sp = Spinbox(root,
             values=(10,38,170,101),    # 以元組儲存數值
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印顯示的值
    print(sp.get())
    
root = Tk()
root.title("")
cities = ("新加坡","上海","東京")       # 以元組儲存數值

sp = Spinbox(root,
             values=cities,    
             command=printInfo)
sp.pack(pady=10,padx=10)

root.mainloop()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

from tkinter.ttk import Separator

root = Tk()

#字 前景 背景 寬 高 字位置預設 字型
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="red",bg="gray",
            height=3,width=15,
            font=("Helvetica",8,"bold"))
label.pack()

#字 前景 背景 寬 高 字位置西北
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="blue",bg="lime",
            height=3,width=15,
            anchor="nw")
label.pack()

#字 前景 背景 寬 高 字位置西北 卷寬度
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw",
            wraplength = 80,
            justify="left")     #left / center / right
label.pack()

label=Label(root,bitmap="hourglass")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="left",text="我的天空")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="top",text="我的天空")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="center",text="我的天空")
label.pack()  

label=Label(root,text="raised",relief="raised")
label.pack()

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10)
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

label=Label(root,text="Welcome to the United States and have a nice day")
label.pack()        # 包裝與定位元件
print(label.keys())

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import Separator

root = Tk()

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

label1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
label1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

label2 = Label(root,text=myContent)
label2.pack(padx=10,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15

label1.pack(side=BOTTOM)              # 包裝與定位元件
label2.pack(side=BOTTOM)              # 包裝與定位元件
label3.pack(side=BOTTOM)              # 包裝與定位元件

"""
label1.pack(side=LEFT)                # 包裝與定位元件
label2.pack(side=LEFT)                # 包裝與定位元件
label3.pack(side=LEFT)                # 包裝與定位元件
"""

"""
label1.pack()                         # 包裝與定位元件
label2.pack(side=RIGHT)               # 靠右包裝與定位元件
label3.pack(side=LEFT)                # 靠左包裝與定位元件
"""

window.mainloop()

print('------------------------------------------------------------')	#60個

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

root = Tk()

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

root = Tk()

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(pady=10)                  # y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X,pady=10)           # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)                  # Y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.pack(padx=50)                  # 左右邊界間距是50像素
label2.pack(padx=50)                  # 左右邊界間距是50像素
label3.pack(padx=50)                  # 左右邊界間距是50像素

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.pack(side=LEFT)                # 包裝與定位元件
label2.pack(side=LEFT,padx=10)        # 左右間距padx=10
label3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack()                         # 包裝與定位元件
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack()                         # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack()                         # 包裝與定位元件
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.geometry("300x180")            # 設定視窗勘寬300高180

oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.geometry("300x180")            # 設定視窗勘寬300高180

oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack()                         # 包裝與定位元件
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(fill=Y)                   # 填滿Y軸包裝與定位元件
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT)                # 從左配置控件
label2.pack()                         # 預設從上開始配置控件
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=X)                   # 預設從上開始配置控件fill=X

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH)                # 預設從上開始配置控件fill=BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH,expand=True)    # fill=BOTH,expand=True

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.geometry("300x200")
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=X)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=X)  

root.mainloop() 

print('------------------------------------------------------------')	#60個

root = Tk()
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=LEFT,fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  

root.mainloop() 

print('------------------------------------------------------------')	#60個

root = Tk()
root.geometry("300x180")            # 設定視窗勘寬300高180

print("執行前",root.pack_slaves())
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10
print("執行後",root.pack_slaves())

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
label2 = Label(window,text="歡迎來到美國",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
label3 = Label(window,text="歡迎來到美國",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
label1.grid(row=0,column=0)           # 格狀包裝
label2.grid(row=1,column=0)           # 格狀包裝
label3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
label2 = Label(window,text="歡迎來到美國",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
label3 = Label(window,text="歡迎來到美國",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
label1.grid(row=0,column=0)           # 格狀包裝
label2.grid(row=1,column=2)           # 格狀包裝
label3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=0,column=2,padx=5,pady=5)
label4.grid(row=0,column=3,padx=5,pady=5)
label5.grid(row=1,column=0,padx=5)
label6.grid(row=1,column=1,padx=5)
label7.grid(row=1,column=2,padx=5)
label8.grid(row=1,column=3,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

Colors = ["red","orange","yellow","green","blue","purple"]

r = 0                               # row編號
for color in Colors:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r += 1

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W+E)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.place(x=0,y=0)                 # 直接定位
label2.place(x=30,y=50)               # 直接定位
label3.place(x=60,y=100)              # 直接定位

window.mainloop()

print('------------------------------------------------------------')	#60個

def yellow():                   # 設定視窗背景是黃色
    root.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    root.config(bg="blue")
    
root = Tk()
root.geometry("300x200")        # 固定視窗大小

# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=blue)
yellowbtn = Button(root,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

def bColor(bgColor):          # 設定視窗背景顏色
    root.config(bg=bgColor)
    
root = Tk()
root.geometry("300x200")        # 固定視窗大小

# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(root,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

lab  = Label(root,text="",bg="yellow",width=20)
btn7 = Button(root,text="7",width=3)
btn8 = Button(root,text="8",width=3)
btn9 = Button(root,text="9",width=3)
btnM = Button(root,text="*",width=3)                # 乘法符號
btn4 = Button(root,text="4",width=3)
btn5 = Button(root,text="5",width=3)
btn6 = Button(root,text="6",width=3)
btnS = Button(root,text="-",width=3)                # 減法符號
btn1 = Button(root,text="1",width=3)
btn2 = Button(root,text="2",width=3)
btn3 = Button(root,text="3",width=3)
btnP = Button(root,text="+",width=3)                # 加法符號
btn0 = Button(root,text="0",width=8)
btnD = Button(root,text=".",width=3)                # 小數點符號
btnE = Button(root,text="=",width=3)                # 等號符號

lab.grid(row=0,column=0,columnspan=4)
btn7.grid(row=1,column=0,padx=5)
btn8.grid(row=1,column=1,padx=5)
btn9.grid(row=1,column=2,padx=5)
btnM.grid(row=1,column=3,padx=5)                    # 乘法符號
btn4.grid(row=2,column=0,padx=5)
btn5.grid(row=2,column=1,padx=5)
btn6.grid(row=2,column=2,padx=5)
btnS.grid(row=2,column=3,padx=5)                    # 減法符號
btn1.grid(row=3,column=0,padx=5)
btn2.grid(row=3,column=1,padx=5)
btn3.grid(row=3,column=2,padx=5)
btnP.grid(row=3,column=3,padx=5)                    # 加法符號
btn0.grid(row=4,column=0,padx=5,columnspan=2)
btnD.grid(row=4,column=2,padx=5)                    # 小數點符號
btnE.grid(row=4,column=3,padx=5)                    # 等號符號

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

nameL = Label(root,text="Name ")        # name標籤
nameL.grid(row=0)
addressL = Label(root,text="Address")   # address標籤
addressL.grid(row=1)

nameE = Entry(root)                     # 文字方塊name
addressE = Entry(root)                  # 文字方塊address
nameE.grid(row=0,column=1)              # 定位文字方塊name
addressE.grid(row=1,column=1)           # 定位文字方塊address

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=0)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=1)

accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=0,column=1)           # 定位文字方塊account
pwdE.grid(row=1,column=1)               # 定位文字方塊pwd

root.mainloop()

print('------------------------------------------------------------')	#60個

def cal():                          # 執行數學式計算
    out.configure(text = "結果 : " + str(eval(equ.get())))
    
root = Tk()

label = Label(root, text="請輸入數學表達式:")
label.pack()

equ = Entry(root)                   # 在此輸入表達式
equ.pack(pady=5)                    

out = Label(root)                   # 存放計算結果
out.pack()                          

btn = Button(root,text="計算",command=cal)    # 計算按鈕
btn.pack(pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
root = Tk()

msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = Label(root,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   

btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()                   

root.mainloop()

print('------------------------------------------------------------')	#60個

def btn_hit():                      # 處理按鈕事件
    if x.get() == "":               # 如果目前是空字串
        x.set("I like tkinter")     # 顯示文字
    else:
        x.set("")                   # 不顯示文字
   
root = Tk()
    
x = StringVar()                     # Label的變數內容

label = Label(root,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   

btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()                   

root.mainloop()

print('------------------------------------------------------------')	#60個

def callback(*args):
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

root.mainloop()

print('------------------------------------------------------------')	#60個

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)   

root.mainloop()

print('------------------------------------------------------------')	#60個

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
  
root = Tk()
    
xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW
xE.trace("r",callbackR)                 # 若是有被讀取執行callbackR

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

btn = Button(root,text="讀取",command=hit)    # 建立讀取按鈕
btn.pack(pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 
  
root = Tk()
    
xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root = Tk()

var = IntVar()                                  # 選項紐綁定的變數
var.set(1)                                      # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value=1,
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value=2,
                      command=printSelection)
rbwoman.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    label.config(text="你是"+var.get())

root = Tk()

var = StringVar()                               # 選項紐綁定的變數
var.set("男生")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value="男生",
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value="女生",
                      command=printSelection)
rbwoman.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

root = Tk()

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(root,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(root,
                text=city,
                variable=var,value=val, 
                command=printSelection).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

root = Tk()

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(root,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(root,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

lab = Label(root,text="請選擇喜歡的運動",fg="blue",bg="lightyellow",width=30)
lab.grid(row=0)

var1 = IntVar()                      
cbtnNFL = Checkbutton(root,text="美式足球",variable=var1)
cbtnNFL.grid(row=1,sticky=W)

var2 = IntVar()
cbtnMLB = Checkbutton(root,text="棒球",variable=var2)
cbtnMLB.grid(row=2,sticky=W)

var3 = IntVar()
cbtnNBA = Checkbutton(root,text="籃球",variable=var3)
cbtnNBA.grid(row=3,sticky=W)   

root.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()

Label(root,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(root,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
btn = Button(root,text="確定",width=10,command=printInfo)
btn.grid(row=i+2)

root.mainloop()

print('------------------------------------------------------------')	#60個

# 以下是callback方法
def selAll():                               # 選取全部字串
    entry.select_range(0,END)
def deSel():                                # 取消選取
    entry.select_clear()
def clr():                                  # 刪除文字
    entry.delete(0,END)
def readonly():                             # 設定Entry狀態
    if var.get() == True:
        entry.config(state=DISABLED)        # 設為DISABLED
    else:
        entry.config(state=NORMAL)          # 設為NORMAL

root = Tk()

# 以下row=0建立Entry
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,
           padx=5,pady=5,sticky=W)
# 以下row=1建立Button
btnSel = Button(root,text="選取",command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)
btnDesel = Button(root,text="取消選取",command=deSel)
btnDesel.grid(row=1,column=1,padx=5,pady=5,sticky=W)
btnClr = Button(root,text="刪除",command=clr)
btnClr.grid(row=1,column=2,padx=5,pady=5,sticky=W)
btnQuit = Button(root,text="結束",command=root.destroy)
btnQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)
# 以下row=2建立Checkboxes
var = BooleanVar()
var.set(False)
chkReadonly = Checkbutton(root,text="唯讀",variable=var,
                          command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import Tk
from tkinter.ttk import Frame, Style

"""fail
root = Tk()

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(root,bg=fm,height=50,width=250).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(bg=fm,height=50,width=250).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

# 用字典儲存框架顏色與游標外形
fms = {'red':'cross','green':'boat','blue':'clock'}
for fmColor in fms:         # 建立3個不同底色的框架與游標外形
    Frame(root,bg=fmColor,cursor=fms[fmColor],
          height=50,width=200).pack(side=LEFT)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

frameUpper = Frame(root,bg="lightyellow")   # 建立上層框架
frameUpper.pack()
btnRed = Button(frameUpper,text="Red",fg="red")
btnRed.pack(side=LEFT,padx=5,pady=5)
btnGreen = Button(frameUpper,text="Green",fg="green")
btnGreen.pack(side=LEFT,padx=5,pady=5)
btnBlue = Button(frameUpper,text="Blue",fg="blue")
btnBlue.pack(side=LEFT,padx=5,pady=5)

frameLower = Frame(root,bg="lightblue")     # 建立下層框架
frameLower.pack()
btnPurple = Button(frameLower,text="Purple",fg="purple")
btnPurple.pack(side=LEFT,padx=5,pady=5)

root.mainloop()
"""
print('------------------------------------------------------------')	#60個

root = Tk()

fm1 = Frame(width=150,height=80,relief=GROOVE, borderwidth=5)
fm1.pack(side=LEFT,padx=5,pady=10)

fm2 = Frame(width=150,height=80,relief=RAISED, borderwidth=5)
fm2.pack(side=LEFT,padx=5,pady=10)

fm3 = Frame(width=150,height=80,relief=RIDGE, borderwidth=5)
fm3.pack(side=LEFT,padx=5,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

fm = Frame(width=150,height=80,relief=RAISED,borderwidth=5) # 建立框架
lab = Label(fm,text="請複選常用的程式語言")     # 建立標籤
lab.pack()
python = Checkbutton(fm,text="Python")          # 建立phthon核取方塊          
python.pack(anchor=W)
java = Checkbutton(fm,text="Java")              # 建立java核取方塊
java.pack(anchor=W)
ruby = Checkbutton(fm,text="Ruby")              # 建立ruby核取方塊
ruby.pack(anchor=W)
fm.pack(padx=10,pady=10)                        # 包裝框架

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

style = Style()                 # 改用Style
style.theme_use("alt")          # 改用alt支援Style

fm1 = Frame(root,width=150,height=80,relief="flat")
fm1.grid(row=0,column=0,padx=5,pady=5)

fm2 = Frame(root,width=150,height=80,relief="groove")
fm2.grid(row=0,column=1,padx=5,pady=5)

fm3 = Frame(root,width=150,height=80,relief="raised")
fm3.grid(row=0,column=2,padx=5,pady=5)

fm4 = Frame(root,width=150,height=80,relief="ridge")
fm4.grid(row=1,column=0,padx=5,pady=5)

fm5 = Frame(root,width=150,height=80,relief="solid")
fm5.grid(row=1,column=1,padx=5,pady=5)

fm6 = Frame(root,width=150,height=80,relief="sunken")
fm6.grid(row=1,column=2,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()

root.geometry("400x220")
# 以下建立標籤框架與和曲方塊
labFrame = LabelFrame(root,text="選擇最喜歡的運動")
sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(labFrame,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
labFrame.pack(ipadx=5,ipady=5,pady=10)      # 包裝定位標籤框架

btn = Button(root,text="確定",width=10,command=printInfo)
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

tl = Toplevel()
Label(tl,text = 'I am a Toplevel').pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")

Label(tl,text = 'I am a Toplevel').pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

import random

root = Tk()

msgYes, msgNo, msgExit = 1,2,3
def MyAnswer():                   # 建立對話方塊
    msgType = random.randint(1,3)   # 隨機數產生對話方塊方式
    if msgType == msgYes:           # 產生Yes字串
        labTxt = 'Yes'
    elif msgType == msgNo:          # 產生No字串
        labTxt = 'No'
    elif msgType == msgExit:        # 產生Exit字串
        labTxt = 'Exit'    
    tl = Toplevel()                 # 建立Toplevel視窗
    tl.geometry("300x180")          # 建立對話方塊大小
    tl.title("My Answer")
    Label(tl,text=labTxt).pack(fill=BOTH,expand=True)

btn = Button(root,text='Click Me',command = MyAnswer)
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked():            # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me",command=buttonClicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個








print('------------------------------------------------------------')	#60個

"""
使用 PanedWindow()

"""
pw = PanedWindow(orient=VERTICAL)       # 建立PanedWindow物件
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")         # 建立標籤Top Pane
pw.add(top)                             # top標籤插入PanedWindow

bottom = Label(pw,text="Bottom Pane")   # 建立標籤Bottom Pane
pw.add(bottom)                          # bottom標籤插入PanedWindow

pw.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

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

from tkinter.ttk import *

root = Tk()

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

from tkinter.ttk import *

root = Tk()

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

""" fail
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
"""

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *

root = Tk()
root.geometry("300x140")

# 使用預設建立進度條
pb1 = Progressbar(root)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各參數設定方式建立進度條
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode ="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    for i in range(100):
        pb["value"] = i+1           # 每次更新1
        root.update()               # 更新畫面
        time.sleep(0.05)
 
root = Tk()

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:        
        pb.step(2)
        root.update()               # 更新畫面
        print(pb.cget("value"))     # 列印指針值
        time.sleep(0.05)
 
root = Tk()

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()

pb = Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個




root = Tk()
root.geometry("300x210")                        # 視窗寬300高210

lb1 = Listbox(root)                             # 建立listbox 1
lb1.pack(side=LEFT,padx=5,pady=10)
lb2 = Listbox(root,height=5,relief="raised")    # 建立listbox 2
lb2.pack(anchor=N,side=LEFT,padx=5,pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              # 建立listbox 
lb.insert(END,"Banana")
lb.insert(END,"Watermelon")
lb.insert(END,"Pineapple")
lb.pack(pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              # 建立listbox
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=MULTIPLE)  # 建立可以多選項的listbox
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple"]

root = Tk()
root.geometry("300x210")                    # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.insert(ACTIVE,"Orange","Grapes","Mango") # 前面補充建立3個項目
lb.pack(pady=10)

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")                    # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print("items數字 : ", lb.size())            # 列出選項數量

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0)             # 預設選擇第0個項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)    
lb.pack(pady=10)
lb.selection_set(0,3)                   # 預設選擇第0-3索引項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1)                    # 刪除索引1的項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1,3)                  # 刪除索引1-3的項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1))                # 列印索引1的項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1,3))              # 列印索引1-3的項目

root.mainloop()

print("------------------------------------------------------------")  # 60個

def callback():                 # 列印所選的項目                
    indexs = lb.curselection()
    for index in indexs:        # 取得索引值
        print(lb.get(index))    # 列印所選的項目
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Print",command=callback)
btn.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個

def callback():                 # 列印檢查結果                
    print(lb.selection_includes(3))
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Check",command=callback)
btn.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個








def itemAdded():                        # 增加項目處理程式
    varAdd = entry.get()                # 讀取Entry的項目
    if (len(varAdd.strip()) == 0):      # 沒有增加不處理
        return
    lb.insert(END,varAdd)               # 將項目增加到Listbox
    entry.delete(0,END)                 # 刪除Entry的內容

def itemDeleted():                      # 刪除項目處理程式
    index = lb.curselection()           # 取得所選項目索引
    if (len(index) == 0):               # 如果長度是0表示沒有選取
        return
    lb.delete(index)                    # 刪除選項    

root = Tk()

entry = Entry(root)                     # 建立Entry            
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
btnAdd = Button(root,text="增加",width=10,command=itemAdded)
btnAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = Listbox(root)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)

# 建立刪除按鈕
btnDel = Button(root,text="刪除",width=10,command=itemDeleted)
btnDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

root.mainloop()

print("------------------------------------------------------------")  # 60個

def itemsSorted():                  # 排序
    if (var.get() == True):         # 如果設定
        revBool = True              # 大到小排序是True
    else:
        revBool = False             # 大到小排序是False
    listTmp = list(lb.get(0,END))   # 取得項目內容
    sortedList = sorted(listTmp,reverse=revBool) # 執行排序
    lb.delete(0,END)                # 刪除原先Listbox內容
    for item in sortedList:         # 將排序結果插入Listbox
        lb.insert(END,item)
            
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()

lb = Listbox(root)                  # 建立Listbox          
for fruit in fruits:                # 建立水果項目
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

# 建立排序按鈕
btn = Button(root,text="排序",command=itemsSorted)
btn.pack(side=LEFT,padx=10,pady=5)

# 建立排序設定核取方塊
var = BooleanVar()
cb = Checkbutton(root,text="大到小排序",variable=var)
cb.pack(side=LEFT)

root.mainloop()
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個

root = Tk()

text = Text(root,height=2,width=30)
text.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

text = Text(root,height=3,width=30)
text.pack()
text.insert(END,"Python王者歸來\nJava王者歸來\n")
text.insert(INSERT,"深石數位公司")

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

text = Text(root,height=3,width=30)
text.pack()
str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

from tkinter.font import Font

def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
      
root = Tk()
root.geometry("300x180")

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(root,familyVar,*familyFamily,command=familyChanged)
family.pack(pady=2)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
      
root = Tk()
root.geometry("300x180")

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(root,familyVar,*familyFamily,command=familyChanged)
family.pack(pady=2)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font

def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
      
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
      
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個

def selectedText():                             # 列印所選的文字
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("選取文字: ",selText)
    except TclError:
        print("沒有選取文字")
      
root = Tk()
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")    # 插入文字

root.mainloop()

print("------------------------------------------------------------")  # 60個


def selectedText():                             # 列印所選的文字
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("選取文字: ",selText)
        print("selectionstart: ", text.index(SEL_FIRST))
        print("selectionend  : ", text.index(SEL_LAST))
    except TclError:
        print("沒有選取文字")
      
root = Tk()
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")    # 插入文字

root.mainloop()

print("------------------------------------------------------------")  # 60個

def printIndex():                               # 列印索引        
    print("INSERT : ", text.index(INSERT))
    print("CURRENT: ", text.index(CURRENT))
    print("END    : ", text.index(END))
      
root = Tk()
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print index",command=printIndex)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")  # 插入文字
text.insert(END,"夢醒時分")                     # 插入文字

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x180")

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")  # 插入文字
text.insert(1.14,"夢醒時分 ")                   # 插入文字

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x180")

text = Text(root)

for i in range(1,10):
    text.insert(END,str(i) + ' Python GUI設計王者歸來 \n')

# 設定書籤
text.mark_set("mark1","5.0")
text.mark_set("mark2","8.0")

print(text.get("mark1","mark2"))
text.pack(fill=BOTH,expand=True)
              
root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()
root.geometry("300x180")

text = Text(root)

for i in range(1,10):
    text.insert(END,str(i) + ' Python GUI設計王者歸來 \n')

# 設定書籤
text.mark_set("mark1","5.0")
text.mark_set("mark2","8.0")

# 設定標籤
text.tag_add("tag1","mark1","mark2")
text.tag_config("tag1",foreground="blue",background="lightyellow")
text.pack(fill=BOTH,expand=True)
              
root.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

def mySearch():
    text.tag_remove("found","1.0",END)              # 刪除標籤但是不刪除標籤定義
    start = "1.0"                                   # 設定搜尋起始位置
    key = entry.get()                               # 讀取搜尋關鍵字

    if (len(key.strip()) == 0):                     # 沒有輸入
        return
    while True:                                     # while迴圈搜尋        
        pos = text.search(key,start,END)            # 執行搜尋
        if (pos == ""):                             # 找不到結束while迴圈
            break
        text.tag_add("found",pos,"%s+%dc" % (pos, len(key)))    # 加入標籤
        start = "%s+%dc" % (pos, len(key))          # 更新搜尋起始位置
                         
root = Tk()
root.geometry("300x180")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

entry = Entry()
entry.grid(row=0,column=0,padx=5,sticky=W+E)

btn = Button(root,text="搜尋",command=mySearch)
btn.grid(row=0,column=1,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.grid(row=1,column=0,columnspan=2,padx=3,pady=5,
          sticky=N+S+W+E)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("found", background="yellow")    # 定義未來找到的標籤定義

root.mainloop()

print("------------------------------------------------------------")  # 60個

def spellingCheck():
    text.tag_remove("spellErr","1.0",END)           # 刪除標籤但是不刪除標籤定義
    textwords = text.get("1.0",END).split()         # Text控件的內文
    print("字典內容\n",textwords)                   # 列印字典內容

    startChar = ("(")                               # 可能的啟始字元
    endChar = (".", ",", ":", ";", "?", "!", ")")   # 可能的結束字元
        
    start = "1.0"                                   # 檢查起始索引位置
    for word in textwords:     
        if word[0] in startChar:                    # 是否含非字母的啟始字元
            word = word[1:]                         # 刪除非字母的啟始字元         
        if word[-1] in endChar:                     # 是否含非字母的結束字元
            word = word[:-1]                        # 刪除非字母的結束字元                        
        if  (word not in dicts and word.lower() not in dicts):
            print("error", word)
            pos = text.search(word, start, END)
            text.tag_add("spellErr", pos, "%s+%dc" % (pos,len(word)))            
            pos = "%s+%dc" % (pos,len(word))     
    
def clrText():
    text.tag_remove("spellErr","1.0",END)
                            
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

chkBtn = Button(toolbar,text="拼字檢查",command=spellingCheck)
chkBtn.pack(side=LEFT,padx=5,pady=5)

clrBtn = Button(toolbar,text="清除",command=clrText)
clrBtn.pack(side=LEFT,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

text.tag_configure("spellErr", foreground="red")    # 定義未來找到的標籤定義
with open("myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")              # 自訂字典串列
    
root.mainloop()

print("------------------------------------------------------------")  # 60個

    
def saveFile():
    textContent = text.get("1.0",END)
    filename = "tmp_write_file.txt"
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)
                            
root = Tk()
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")
    
root.mainloop()

sys.exit()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("#1",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities"),show="headings")
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("#1",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

list1 = ["芝加哥","800"]               # 以串列方式設定欄內容         
list2 = ["洛杉磯","1000"]
list3 = ["南京","900"]
# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立內容
tree.insert("",index=END,text="伊利諾",values=list1)
tree.insert("",index=END,text="加州",values=list2)
tree.insert("",index=END,text="江蘇",values=list3)
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 格式化欄位
tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 格式化欄位
tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()
cityDict = tree.column("cities")
print(cityDict)

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")             # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue") # 設定標籤
rowCount = 1                                # 行號從1算起
for state in stateCity.keys():
    if (rowCount % 2 == 1):                 # 如果True則是奇數行
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))     # 建立淺藍色底
    rowCount += 1                           # 行號數加1
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
      
root = Tk()

asia = {"中國":"北京","日本":"東京","泰國":"曼谷","韓國":"首爾"}
euro = {"英國":"倫敦","法國":"巴黎","德國":"柏林","挪威":"奧斯陸"}
             
# 建立Treeview
tree = Treeview(root,columns=("capital"))
# 建立欄標題
tree.heading("#0",text="國家")             # 圖標欄位icon column
tree.heading("capital",text="首都")
# 建立id
idAsia = tree.insert("",index=END,text="Asia")
idEuro = tree.insert("",index=END,text="Europe")
# 建立idAsia底下內容
for country in asia.keys():
    tree.insert(idAsia,index=END,text=country,values=asia[country])
# 建立idEuro底下內容
for country in euro.keys():
    tree.insert(idEuro,index=END,text=country,values=euro[country])     
tree.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
def removeItem():                   # 刪除所選項目
    iids = tree.selection()         # 取得所選項目
    for iid in iids:                # 所選項目可能很多所以用迴圈
        tree.delete(iid)            # 刪除所選項目
         
root = Tk()

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.pack()

rmBtn = Button(root,text="Remove",command=removeItem)   # 刪除鈕
rmBtn.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

def removeItem():                   # 刪除所選項目
    ids = tree.selection()          # 取得所選項目
    for id in ids:                  # 所選項目可能很多所以用迴圈
        tree.delete(id)             # 刪除所選項目
def insertItem():
    state = stateEntry.get()        # 獲得stateEntry的輸入
    city = cityEntry.get()          # 獲得cityEntry的輸入
# 如果輸入資料未完全不往下執行
    if (len(state.strip())==0 or len(city.strip())==0):
        return
    tree.insert("",END,text=state,values=(city))    # 插入
    stateEntry.delete(0,END)        # 刪除stateEntry
    cityEntry.delete(0,END)         # 刪除cityEntry
         
root = Tk()

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 以下3行主要是應用在縮放視窗
root.rowconfigure(1,weight=1)       # row1會隨視窗縮放1:1變化
root.columnconfigure(1,weight=1)    # column1會隨視窗縮放1:1變化
root.columnconfigure(3,weight=1)    # column3會隨視窗縮放1:1變化

stateLab = Label(root,text="State :")   # 建立State :標籤
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry = Entry()                    # 建立State :文字方塊
stateEntry.grid(row=0,column=1,sticky=W+E,padx=5,pady=3)
cityLab = Label(root,text="City : ")    # 建立City :標籤
cityLab.grid(row=0,column=2,sticky=E)
cityEntry = Entry()                     # 建立City :文字方塊
cityEntry.grid(row=0,column=3,sticky=W+E,padx=5,pady=3)
# 建立Insert按鈕
inBtn = Button(root,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)            
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

rmBtn = Button(root,text="刪除",command=removeItem)   # 刪除鈕
rmBtn.grid(row=2,column=2,padx=5,pady=3,sticky=W)

root.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
         
root = Tk()

stateCity = {"Illinois":"芝加哥","California":"洛杉磯",
             "Texas":"休士頓","Washington":"西雅圖",
             "Jiangsu":"南京","Shandong":"青島",
             "Guangdong":"廣州","Fujian":"廈門",
             "Mississippi":"Oxford","Kentucky":"Lexington",
             "Florida":"Miama","Indiana":"West Lafeyette"}

tree = Treeview(root,columns=("cities"))
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

def treeview_sortColumn(col):
    global reverseFlag                  # 定義排序旗標全域變數
    lst = [(tree.set(st, col), st) 
            for st in tree.get_children("")]
    print(lst)                          # 列印串列
    lst.sort(reverse=reverseFlag)       # 排序串列
    print(lst)                          # 列印串列
    for index, item in enumerate(lst):  # 重新移動項目內容
        tree.move(item[1],"",index)
    reverseFlag = not reverseFlag       # 更改排序旗標
            
root = Tk()

reverseFlag = False                     # 排序旗標註明是否反向排序

myStates = {"Illinois","California","Texas","Washington",
            "Jiangsu","Shandong","Guangdong","Fujian",
            "Mississippi","Kentucky","Florida","Indiana"}

tree = Treeview(root,columns=("states"),show="headings")
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("states",text="State")
# 建立內容
for state in myStates:                  # 第一次的Treeview內容
    tree.insert("",index=END,values=(state,))
# 點選標題欄將啟動treeview_sortColumn
tree.heading("#1",text="State",
             command=lambda c="states": treeview_sortColumn(c))

root.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("準備搬出的")
print("------------------------------------------------------------")  # 60個





print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個
print('xxxxxxx')
print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個
print('xxxxxxx')
print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#各種事件的寫法

def msgShow():
    print('你按了 button')

btn1 = Button(root,text="列印訊息",width=15,command=msgShow)
btn2 = Button(root,text="結束",width=15,command=root.destroy)
                     

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
btn1 = tk.Button(window,text="Message",width=15,command=msgShow)
btn2 = tk.Button(window,text="Exit",width=15,command=window.destroy)

btn1.pack(side=tk.LEFT)                # 按鈕1
btn2.pack(side=tk.RIGHT)               # 按鈕2

window.mainloop()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個




print("pack版面佈局")

taipei=tk.Button(window, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(window, width=20, text="高雄景點")
kaohsiung.pack(side="top")

print("------------------------------------------------------------")  # 60個
print(".bind")
print("------------------------------------------------------------")  # 60個


# drag.py


def fnEnter(event):
    lblTest['bg']='lightblue'

def fnLeave(event):
    lblTest.config(text='試試看',bg='gray')
    
def fnMotion(event):
    lblTest['text']='游標移動'

def fnClick(event):
    global mx,my	#宣告mx,my為全域變數
    mx=event.x	#紀錄按下時滑鼠游標的x坐標
    my=event.y	#紀錄按下時滑鼠游標的y坐標
    
def fnB1Motion(event):
    global mx,my	#宣告mx,my為全域變數
    lblX=lblTest.winfo_rootx()-window.winfo_rootx()	#計算lblTest在視窗的x坐標
    lblY=lblTest.winfo_rooty()-window.winfo_rooty()	#計算lblTest在視窗的y坐標
    lblTest['text']='拖曳中...'
    lblTest.place(x=lblX+(event.x-mx),y=lblY+(event.y-my))	#重設lblTest位置
    
window = tk.Tk()
window.title('滑鼠事件測試')
window.geometry('240x240')

mx=0
my=0
lblTest=tk.Label(window,text='試試看',width=8,height=2,relief='groove',bg='gray')
lblTest.place(x=80,y=100)
lblTest.bind('<Enter>',fnEnter) #<Enter>事件綁定fnEnter事件處理函式
lblTest.bind('<Leave>',fnLeave) #<Leave>事件綁定fnLeave事件處理函式
lblTest.bind('<Motion>',fnMotion) #<Motion>事件綁定fnMotion事件處理函式
lblTest.bind('<Button-1>',fnClick) #<Button-1>事件綁定fnClick事件處理函式
lblTest.bind('<B1-Motion>',fnB1Motion) #<B1-Motion>事件綁定fnB1Motion事件處理函式

window.mainloop()

print("------------------------------------------------------------")  # 60個


# night_market.py


def fnArea(e):
    global iArea,iNM		#宣告iArea,iNM為全域變數
    i=lstArea.curselection()    #取得地區選項索引的元組
    iArea=i[0]  #設iArea值為第一個元組值
    lstNM.delete(0,'end')   #清除所有夜市項目
    for x in range(len(nm[iArea])): #依序加入對應地區的夜市到清單
        lstNM.insert('end',nm[iArea][x])

def fnNM(e):
    global iArea,iNM		#宣告iArea,iNM為全域變數
    i=lstNM.curselection()    #取得夜市選項索引的元組
    iNM=i[0]  #設iNM值為第一個元組值
    lblMsg.config(text=msg[iArea][iNM]) #重設標籤的文字內容
    
window = tk.Tk()
window.title('台灣夜市簡介')
window.geometry('300x180')

tk.Label(window,text='台灣夜市之旅',font=('微軟正黑體',16)).pack()
lfrmNM=tk.LabelFrame(window,text='夜市名稱',relief='raised',borderwidth=2)
lfrmNM.pack(side='left',anchor='n',padx=5,pady=3)
areas=['北台灣','中台灣','南台灣','東台灣'] #宣告地區串列
lstArea=tk.Listbox(lfrmNM,height=4)
for a in areas: #將地區串列值依序插入清單中
    lstArea.insert('end',a)
lstArea.pack()
iArea=0 #預設地區選項的索引值為0
lstArea.bind('<<ListboxSelect>>',fnArea)    #選項改變的事件綁定fnArea函式
nm =[['基隆廟口','士林夜市','華西街夜市'],['逢甲夜市','一中街夜市'],
     ['文化路夜市','花園夜市','六合夜市'],['羅東夜市','東大門夜市']]
lstNM=tk.Listbox(lfrmNM,height=3)
lstNM.pack()
for x in range(len(nm[0])): #將北台灣的夜市串列值依序插入清單中
    lstNM.insert('end',nm[0][x])
lstNM.selection_set(0)  #預設選取第一個夜市
iNM=0 #預設夜市選項的索引值為0
lstNM.bind('<<ListboxSelect>>',fnNM)    #選項改變的事件綁定fnNM函式
lfrmMsg=tk.LabelFrame(window,text='夜市簡介',relief='raised',borderwidth=2)
lfrmMsg.pack(side='left',anchor='n',padx=5,pady=3)
msg=[['基隆夜市的廟口小吃遠近馳名\n\n營業時間：17:00-03:00',
      '集合大江南北小吃觀光客必到夜市\n\n營業時間：11:00-02:00',
      '最著名的夜市吸引國內外觀光客\n\n營業時間：16:00-24:00'],
     ['「價位便宜，應有盡有」是特色\n\n營業時間：12:00-02:00',
      '小吃攤、飲食店、流行服飾店林立\n\n營業時間：11:00–22:10'],
     ['文化路夜市聚集千家以上的攤販\n\n營業時間：17:00-06:00',
      '花園夜市規模大，交通便利\n\n營業時間：18:00-24:00(四、六、日)',
      '各地特產、小吃等一應俱全\n\n營業時間：17:00-02:00'],
     ['羅東夜市有豐富的當地小吃\n\n營業時間：17:00-01:00',
      '占地遼闊吃喝玩樂逛不完\n\n營業時間:18:00-00:00']]
lblMsg=tk.Label(lfrmMsg,text=msg[0][0],font=(12),wraplength=120,justify='left')
lblMsg.pack(anchor='n')

window.mainloop()

print("------------------------------------------------------------")  # 60個

def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked(event):       # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me")
btn.pack(anchor=W)
btn.bind("<Button-1>",buttonClicked)  # 按一下Click me綁定buttonClicked方法

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def callback(event):                        # 事件處理程式
    print("滑鼠點擊位置 :", event.x, event.y)   # 列印座標
    
root = Tk()

frame = Frame(root,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "滑鼠位置 : x:{}, y:{}".format(x,y)
    var.set(textvar)
    
root = Tk()

root.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)   # 增加事件處理程式

root.mainloop()

print('------------------------------------------------------------')	#60個

def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
root = Tk()
root.geometry("300x180")

btn = Button(root,text="離開",command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>",enter)               # 進入綁定enter
btn.bind("<Leave>",leave)               # 離開綁定leave

x = StringVar()
lab = Label(root,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

root.mainloop()

print('------------------------------------------------------------')	#60個

def leave(event):                       # <Esc>事件處理程式
    print('你按了 ESC')
   
root = Tk()

root.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = Label(root,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
root = Tk()

root.bind("<Key>",key)              # <Key>鍵綁定key函數

root.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
root = Tk()

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
root = Tk()
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter")   # 建立按鈕tkinter
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()                  # 建立核取方塊
cbtn = Checkbutton(root,text="bind/unbind",variable=var,
                   command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

def btnClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def btnClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter")
    
root = Tk()
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter",   # 建立按鈕tkinter
             command=btnClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",btnClicked2,add="+")  # 增加事件處理程式

root.mainloop()





print("------------------------------------------------------------")  # 60個


def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個


def itemSelected(event):        # 列出所選單一項目
    index = lb.curselection()   # 取得索引
    var.set(lb.get(index))      # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個


def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<Double-Button-1>",itemSelected) # 連按2下綁定
lb.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個

def itemsSelected(event):       # 列印所選結果
    obj = event.widget          # 取得事件的物件
    indexs = obj.curselection() # 取得索引
    for index in indexs:        # 將元組內容列出
        print(obj.get(index))
    print("----------")         # 區隔輸出
    
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root,selectmode=EXTENDED)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemsSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()


print("------------------------------------------------------------")  # 60個

def getIndex(event):                    # 處理按一下選項
    lb.index = lb.nearest(event.y)      # 目前選項的索引
    
def dragJob(event):                     # 處理拖曳選項
    newIndex = lb.nearest(event.y)      # 目前選項的新索引
    if newIndex < lb.index:             # 往上拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex+1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引
    elif newIndex > lb.index:           # 往下拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex-1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()

lb = Listbox(root)                      # 建立Listbox          
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)      # 按一下綁定getIndex
    lb.bind("<B1-Motion>",dragJob)      # 拖曳綁定dragJob
lb.pack(padx=10,pady=10)

root.mainloop()


print("------------------------------------------------------------")  # 60個


from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.configure(font=f)                  # 更新text的font size    
      
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack(side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個


from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.tag_config(SEL,font=f)
      
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                        # size family更新
    f=Font(size=sizeVar.get())                  # 取得新font size
    text.tag_config(SEL,font=f)
      
root = Tk()
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n","a")     # 插入時同時設定Tag
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()
# 將Tag a設為置中,藍色,含底線
text.tag_config("a",foreground="blue",justify=CENTER,underline=True)

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox
def cutJob():                           # Cut方法
    copyJob()                           # 複製選取文字
    text.delete(SEL_FIRST,SEL_LAST)     # 刪除選取文字
def copyJob():                          # Copy方法
    try:
        text.clipboard_clear()          # 清除剪貼簿
        copyText = text.get(SEL_FIRST,SEL_LAST)             # 複製選取區域
        text.clipboard_append(copyText) # 寫入剪貼簿
    except TclError:
        print("沒有選取")
def pasteJob():                         # Paste方法
    try:
        copyText = text.selection_get(selection="CLIPBOARD") # 讀取剪貼簿內容
        text.insert(INSERT,copyText)        # 插入內容
    except TclError:
        print("剪貼簿沒有資料")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def cutJob():                           # Cut方法
    text.event_generate("<<Cut>>")
def copyJob():                          # Copy方法
    text.event_generate("<<Copy>>")
def pasteJob():                         # Paste方法
    text.event_generate("<<Paste>>")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox
def cutJob():                           # Cut方法
    text.event_generate("<<Cut>>")
def copyJob():                          # Copy方法
    text.event_generate("<<Copy>>")
def pasteJob():                         # Paste方法
    text.event_generate("<<Paste>>")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)
def undoJob():                          # 復原undo方法
    try:
        text.edit_undo()
    except:
        print("先前未有動作")
def redoJob():                          # 重複redo方法
    try:
        text.edit_redo()
    except:
        print("先前未有動作")

root = Tk()
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

# 建立Button
undoBtn = Button(toolbar,text="Undo",command=undoJob)
undoBtn.pack(side=LEFT,pady=2)
redoBtn = Button(toolbar,text="Redo",command=redoJob)
redoBtn.pack(side=LEFT,pady=2)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()



print("------------------------------------------------------------")  # 60個


from tkinter.ttk import *

def treeSelect(event):
    widgetObj = event.widget                # 取得控件
    itemselected = widgetObj.selection()[0] # 取得選項
    col1 = widgetObj.item(itemselected,"text")  # 取得圖標欄內容
    col2 = widgetObj.item(itemselected,"values")[0] # 取得第0索引欄位內容
    str = "{0} : {1}".format(col1,col2)     # 取得所選項目內容
    var.set(str)                            # 設定狀態列內容
         
root = Tk()

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"),selectmode=BROWSE)
# 建立欄標題
tree.heading("#0",text="State")             # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue") # 設定標籤
rowCount = 1                                # 行號從1算起
for state in stateCity.keys():
    if (rowCount % 2 == 1):                 # 如果True則是奇數行
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))     # 建立淺藍色底
    rowCount += 1                           # 行號數加1

tree.bind("<<TreeviewSelect>>",treeSelect)  # Treeview控件Select發生
tree.pack()

var = StringVar()
label = Label(root,textvariable=var,relief="groove")    # 建立狀態列
label.pack(fill=BOTH,expand=True)

root.mainloop()



print("------------------------------------------------------------")  # 60個


from tkinter import messagebox
from tkinter.ttk import *

def doubleClick(event):
    e = event.widget                        # 取得事件控件
    iid = e.identify("item",event.x,event.y)    # 取得連按2下項目id
    state = e.item(iid,"text")              # 取得State
    city = e.item(iid,"values")[0]          # 取得City
    str = "{0} : {1}".format(state,city)    # 格式化
    messagebox.showinfo("Double Clicked",str)   # 輸出
         
root = Tk()

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.bind("<Double-1>",doubleClick)     # 連按2下綁定doubleClick方法
tree.pack()

root.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

def paint(event):                           # 拖曳可以繪圖
    x1,y1 = (event.x, event.y)              # 設定左上角座標
    x2,y2 = (event.x, event.y)              # 設定右下角座標
    canvas.create_oval(x1,y1,x2,y2,fill="blue")
def cls():                                  # 清除畫面
    canvas.delete("all")
    
tk = Tk()
lab = Label(tk,text="拖曳滑鼠可以繪圖")     # 建立標題
lab.pack()
canvas = Canvas(tk,width=640, height=300)   # 建立畫布
canvas.pack()

btn = Button(tk,text="清除",command=cls)    # 建立清除按鈕
btn.pack(pady=5)

canvas.bind("<B1-Motion>",paint)            # 滑鼠拖曳綁定paint

canvas.mainloop()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


