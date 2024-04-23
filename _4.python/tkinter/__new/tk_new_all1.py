import sys

import tkinter as tk

print("------------------------------------------------------------")  # 60個

import tkinter as tk

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

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("09-TkUI9Entry-python2")

import tkinter as tk
from tkinter import StringVar

def event1():
    label1.set("123")
	#print(entry1.get())

win = tk.Tk()
entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
v = StringVar()
label1 =tk.Label(win,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("09-TkUI9Entry-python3")

import tkinter as tk
from tkinter import StringVar

def event1():
    print(entry1.get())
    t1=entry1.get()
    v.set(t1)

win = tk.Tk()
entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
v = StringVar()     #
label1 =tk.Label(win,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("TkUI_exam")

import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()

def event1():
	value1=entry1.get()
	print(value1)
	value2=float(value1)
	value2=value2*0.15
	print(value2)
	label1.config(text='Button Pressed')


label1 =tk.Label(win,text="Hello World!")
label1.pack()

entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("TkUI10Entry-python3-Exam")

import tkinter as tk
from tkinter import StringVar

def event1():
    t1=float(entry1.get())
    t1=t1/30.5
    print(t1)
    v.set(str(t1))

win = tk.Tk()
entry1=tk.Entry(win)
entry1.pack()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()
v = StringVar()
label1 =tk.Label(win,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("grid")

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=30, text="台北景點")
taipei.grid(column=0,row=0)
kaohsiung=tk.Button(win, width=30, text="高雄景點")
kaohsiung.grid(column=0,row=1)
ilan=tk.Button(win, width=30, text="宜蘭景點")
ilan.grid(column=1,row=0)
tainan=tk.Button(win, width=30, text="台南景點")
tainan.grid(column=1,row=1)
	
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("homework1")

import tkinter as tk
win = tk.Tk()
win.geometry("100x100")
win.title("grid佈局")

one=tk.Button(win, width=20, text="January")
one.grid(column=0,row=0)
two=tk.Button(win, width=20, text="Februry")
two.grid(column=1,row=0)
three=tk.Button(win, width=20, text="March")
three.grid(column=2,row=0)
one=tk.Button(win, width=20, text="April")
one.grid(column=0,row=1)
two=tk.Button(win, width=20, text="May")
two.grid(column=1,row=1)
three=tk.Button(win, width=20, text="June")
three.grid(column=2,row=1)
one=tk.Button(win, width=20, text="July")
one.grid(column=0,row=2)
two=tk.Button(win, width=20, text="August")
two.grid(column=1,row=2)
three=tk.Button(win, width=20, text="September")
three.grid(column=2,row=2)
one=tk.Button(win, width=20, text="October")
one.grid(column=0,row=3)
two=tk.Button(win, width=20, text="November")
two.grid(column=1,row=3)
three=tk.Button(win, width=20, text="December")
three.grid(column=2,row=3)

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("pack")

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(win, width=20, text="高雄景點")
kaohsiung.pack(side="top")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("place")

import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=30, text="台北景點")
taipei.place(x=10, y=10)
kaohsiung=tk.Button(win, width=30, text="高雄景點")
kaohsiung.place(relx=0.5, rely=0.5, anchor="center")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("scrollbar")

from tkinter import *
win = Tk()
win.title("ScrollBar捲軸")
win.geometry('300x200')
text = Text(win, width = "30", height = "5")
text.grid(row = 0, column = 0)
scrollbar = Scrollbar(command = text.yview, orient = VERTICAL)
scrollbar.grid(row = 0, column = 1, sticky = "ns")
text.configure(yscrollcommand = scrollbar.set)
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("text")

from tkinter import *
sentences="玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"
win = Tk()
win.title("Text多行文字")
win.geometry('300x200')
text = Text(win, width = 30, height = 14, bg = "yellow", wrap=WORD)
text.insert(END,sentences)
text.pack()
win.mainloop()

print('------------------------------------------------------------')	#60個







print("------------------------------------------------------------")  # 60個

""" some wrong 有一點點不一樣

from __future__ import unicode_literals
from pytube import YouTube
import tkinter as tk
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
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
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

win.mainloop()
""" #some wrong

print("------------------------------------------------------------")  # 60個


#MP3播放器
def choose():
    global playsong
    message.set("\n播放歌曲：" + choice.get())
    playsong=choice.get()
def pausemp3(): 
    mixer.music.pause() 
    message.set("\n暫停播放 {}".format(playsong))   
def increase():
    global volume
    volume +=0.1
    if volume>=1.0:
        volume=1.0
    mixer.music.set_volume(volume) 
def decrease():
    global volume
    volume -=0.1
    if volume<=0.2:
        volume=0.2
    mixer.music.set_volume(volume)  
def playmp3():
    global status,playsong,preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1) 
        else:
            mixer.music.unpause() 
        message.set("\n正在播放：{}".format(playsong))
    else:
        playnewmp3()
        preplaysong=playsong 
def playnewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)   
    mixer.music.play(loops=-1)  
    message.set("\n正在播放：{}".format(playsong))
def stopmp3():
    mixer.music.stop()
    message.set("\n停止播放") 
def loadmp3():
    global volume
    global playsong
    global preplaysong
    global choice
    global pdir
    frame1 = tk.Frame(win)
    frame1.pack()
    mp3files = []
    mp3files = glob.glob(pdir.get()+"*.mp3")
    playsong=preplaysong = ""
    index = 0
    volume= 0.8
    choice = tk.StringVar()    
    for mp3 in mp3files:  
        prbutton = tk.Radiobutton(frame1,text=mp3,variable=choice,value=mp3,command=choose)
        if(index==0):     
            prbutton.select()
            playsong=preplaysong=mp3
        prbutton.grid(row=index, column=0, sticky="w")
        index += 1      
    message.set("\n讀取檔案")
def exitmp3():
    mixer.music.stop()
    win.destroy() 

import tkinter as tk
from pygame import mixer
import glob

mixer.init()
win=tk.Tk()
win.geometry("640x380")
win.title("MP3播放程式")
labeltitle = tk.Label(win, text="\nMP3播放程式", fg="blue",font=("標楷體",12))
labeltitle.pack()
frame0 = tk.Frame(win)
frame0.pack()
pdir = tk.StringVar()
plabel1 = tk.Label(frame0, text="請輸入目錄:", width=8)
plabel1.grid(row=0, column=0, padx=5, pady=5)
pentry = tk.Entry(frame0, textvariable=pdir, width=12)
pdir.set('music/')
pentry.grid(row=0, column=1, padx=5, pady=5)   
button1 = tk.Button(frame0, text="播放", width=8,command=playmp3)
button1.grid(row=1, column=0, padx=5, pady=5)
button2 = tk.Button(frame0, text="暫停", width=8,command=pausemp3)
button2.grid(row=1, column=1, padx=5, pady=5)
button3 = tk.Button(frame0, text="調大音量", width=8,command=increase)
button3.grid(row=1, column=2, padx=5, pady=5)
button4 = tk.Button(frame0, text="調小音量", width=8,command=decrease)
button4.grid(row=1, column=3, padx=5, pady=5)
button5 = tk.Button(frame0, text="停止", width=8,command=stopmp3)
button5.grid(row=1, column=4, padx=5, pady=5)
button7 = tk.Button(frame0, text="讀取檔案", width=8,command=loadmp3)
button7.grid(row=1, column=5, padx=5, pady=5)
button6 = tk.Button(frame0, text="結束", width=8,command=exitmp3)
button6.grid(row=1, column=6, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exitmp3)   
message = tk.StringVar()
message.set("\n播放歌曲：")
plabel2 = tk.Label(win, textvariable=message,fg="blue",font=("標楷體",10))
plabel2.pack() 
plabel3 = tk.Label(win, text="\n")
plabel3.pack()   
win.mainloop()

print("------------------------------------------------------------")  # 60個

def checknum():
    pmsg.set("Small")

import tkinter as tk
import random as r

win = tk.Tk()
win.geometry("400x300")
win.title("Guess Number")
ans=r.randint(0,100)
#print(ans)
#input guess number
pL1 = tk.Label(win, text="Please enter number:")
pL1.pack()
while (True):
    pnum = tk.StringVar()
    pE1 = tk.Entry(win, textvariable=pnum)
    pE1.pack()
    pB1 = tk.Button(win, text="OK", command=checknum)
    pB1.pack()

pmsg = tk.StringVar()
pL2 = tk.Label(win, textvariable=pmsg)
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
#print("you are win")    

win.mainloop()


print("------------------------------------------------------------")  # 60個

""" syntax fail
from __future__ import unicode_literals
from pytube import YouTube

import tkinter as tk
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
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
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

win.mainloop()
"""
print("------------------------------------------------------------")  # 60個

def checkp():
    p3.set(p2.get()/(p1.get()*p1.get()/10000))
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("計算BMI程式")
frame1 = tk.Frame(win)
frame1.pack(padx=20, pady=10)
p1 = tk.IntVar()
p2 = tk.IntVar()
p3 = tk.DoubleVar()
pLabel = tk.Label(frame1, text="請輸入身高(公分)")
pLabel.pack()
pEn1 = tk.Entry(frame1, textvariable=p1)
pEn1.pack()
pLabe2 = tk.Label(frame1, text="請輸入體重(公斤)")
pLabe2.pack()
pEn2 = tk.Entry(frame1, textvariable=p2)
pEn2.pack()
pButton = tk.Button(frame1, text="計算BMI", command=checkp)
pButton.pack()
pLmsg = tk.Label(frame1, textvariable=p3)
pLmsg.pack()
win.mainloop()





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

from tkinter import *

window = Tk() #建立主視窗物件

"""
# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(window, text = 'Gray', bg = 'gray',
        fg = 'white').pack(side = 'right')#加入版面

lblb = Label(window, text = 'Yellow',
        bg = 'yellow', fg = 'gray').pack(
        side = 'right', padx = 5, pady = 10)

lblc = Label(window, text = 'Orange',
        bg = 'orange', fg = 'black').pack(side = 'right')

mainloop()
"""

photo = PhotoImage(file = '001.png')#建立圖片

#標籤 - bg 設背景色
t1 = Label(window, text = 'Hello\n Python', bg = '#78A', 
    fg = '#FF0', relief = 'groove', bd = 2, 
    width = 15, height = 3, justify = 'right')

t2 = Label(window, text = '世界', width = 6, height = 3,
    relief = RIDGE, bg = 'pink', font = ('標楷體', 16))

#在第3個標籤載入圖片
t3 = Label(window, image = photo, relief = 'sunken',
    bd = 5, width = 180, height = 150)

t1.grid(row = 0, column = 0)
t2.grid(row = 0, column = 1)
t3.grid(columnspan = 2)

mainloop()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
    
pic_image = ImageTk.PhotoImage(file=filename)
lab1 = tk.Label(window,image=pic_image).pack(side="right")

poem_text = """滕王高閣臨江渚，佩玉鳴鸞罷歌舞。
畫棟朝飛南浦雲，珠簾暮卷西山雨。
閒雲潭影日悠悠，物換星移幾度秋。
閣中帝子今何在？檻外長江空自流。"""
lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             padx=10).pack(side="left")
"""
lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")
"""

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_icon/Recording.bmp'

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

sun_gif = ImageTk.PhotoImage(file=filename)
btn = tk.Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

sun_gif = ImageTk.PhotoImage(file=filename)
btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.TOP)

label.pack()                      
btn.pack()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

sun_gif = ImageTk.PhotoImage(file=filename)
btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.CENTER)

label.pack()                      
btn.pack()

print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(win, width=20, text="高雄景點")
kaohsiung.pack(side="top")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("place.py")

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=30, text="台北景點")
taipei.place(x=10, y=10)
kaohsiung=tk.Button(win, width=30, text="高雄景點")
kaohsiung.place(relx=0.5, rely=0.5, anchor="center")

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("tk_new01.py")

import tkinter as tk

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#在半徑為100的援外建立12個點 然後將此12點彼此相連
import math

canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])




"""

label = tk.Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件

"""


lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容             
btn = tk.Button(window,text="Message",command=msgShow)

label.pack()                      
btn.pack()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容             
btn1 = tk.Button(window,text="Message",width=15,command=msgShow)
btn2 = tk.Button(window,text="Exit",width=15,command=window.destroy)
label.pack()                      
btn1.pack(side=LEFT)                # 按鈕1
btn2.pack(side=RIGHT)               # 按鈕2

print("------------------------------------------------------------")  # 60個

label = tk.Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")
label.pack()                        # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM)              # 包裝與定位元件
lab3.pack(side=BOTTOM)              # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=BOTTOM)              # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT)                # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT,padx=5)         # 包裝與定位元件,增加x軸間距
lab3.pack(side=LEFT)                # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=RIGHT)               # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

print("------------------------------------------------------------")  # 60個

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = tk.Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
btn = tk.Button(window,text="Hit",command=btn_hit).pack()                   

print("------------------------------------------------------------")  # 60個

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)              # 文字方塊1
e2 = tk.Entry(window,show='*')     # 文字方塊2
e1.grid(row=0,column=1)         # 定位文字方塊1
e2.grid(row=1,column=1)         # 定位文字方塊2

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
btn1.grid(row=2,column=0)
btn2 = tk.Button(window,text="Quit",command=window.quit)
btn2.grid(row=2,column=1)

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    e1.delete(0,END)                # 刪除文字方塊1
    e2.delete(0,END)                # 刪除文字方塊2
          
lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

print("------------------------------------------------------------")  # 60個

def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
n1 = IntVar()                   
n2 = IntVar()
n3 = IntVar()

e1 = tk.Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = tk.Label(window,width=3,text='+')      # 加號
e2 = tk.tk.Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = tk.Button(window,width=5,text='=',command=add)   # =按鈕
e3 = tk.Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

print("------------------------------------------------------------")  # 60個
          
text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n我的明志工專生活點滴")
text.pack()

print("------------------------------------------------------------")  # 60個

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)
text.pack()

print("------------------------------------------------------------")  # 60個
          
scrollbar = Scrollbar(window)           # 卷軸物件
text = Text(window,height=2,width=30)   # 文字區域物件
scrollbar.pack(side=RIGHT,fill=Y)       # 靠右安置與父物件高度相同
text.pack(side=LEFT,fill=Y)             # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)

print("------------------------------------------------------------")  # 60個

import tkinter as tk

window=tk.Tk()
tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='藍', bg='green', width=20).pack()
tk.Label(window, text='綠', bg='blue', width=20).pack()
window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()
window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

window = Tk()
window.title("ex18_2")              # 視窗標題
lab1 = Label(window,text="Peter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="John",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="Notron",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab4 = Label(window,text="Kevin",
              bg="lightgreen",      # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab5 = Label(window,text="Tommy",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab6 = Label(window,text="Mary",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab7 = Label(window,text="Tracy",
              bg="lightblue",       # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab8 = Label(window,text="Mike",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab9 = Label(window,text="Vicent",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15

lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=0,column=1)           # 格狀包裝
lab3.grid(row=0,column=2)           # 格狀包裝
lab4.grid(row=1,column=0)           # 格狀包裝
lab5.grid(row=1,column=1)           # 格狀包裝
lab6.grid(row=1,column=2)           # 格狀包裝
lab7.grid(row=2,column=0)           # 格狀包裝
lab8.grid(row=2,column=1)           # 格狀包裝
lab9.grid(row=2,column=2)           # 格狀包裝
window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def myfun():
    monthrate = interest.get() / (12*100)
    loan = loanmoney.get()
    molecules = loan * monthrate
    denominator = 1-(1/(1+monthrate) ** (years.get() * 12))
    monthpaid = int(molecules / denominator)
    monthpayment.set(monthpaid)
    totalpaid = int(monthpaid * 12 * years.get())
    totalpayment.set(totalpaid)
        
window = Tk()
window.title("ex18_4")                  # 視窗標題

Interest = Label(window, text="利率")
Years = Label(window, text="貸款年數")
LoanMoney = Label(window, text="貸款金額")
MonthPayment = Label(window, text="每月支付金額")
TotalPayment = Label(window, text="總支付金額")

interest = DoubleVar()
years = IntVar()
loanmoney = IntVar()
monthpayment = IntVar()
totalpayment = IntVar()

interestE = Entry(window, textvariable=interest)
yearsE = Entry(window, textvariable=years)
loanmoneyE = Entry(window, textvariable=loanmoney)
monthpaymentL = Label(window, textvariable=monthpayment, bg='lightyellow')
totalpaymentL = Label(window, textvariable=totalpayment, bg='lightyellow')

Interest.grid(row=0, column=0)
Years.grid(row=1, column=0)
LoanMoney.grid(row=2, column=0)
MonthPayment.grid(row=3, column=0)
TotalPayment.grid(row=4, column=0)

interestE.grid(row=0, column=1, padx=2)
yearsE.grid(row=1, column=1, padx=2)
loanmoneyE.grid(row=2, column=1, padx=2)
monthpaymentL.grid(row=3, column=1, padx=2)
totalpaymentL.grid(row=4, column=1, padx=2)

btnExec = Button(window, text="計算", command=myfun)
btnExec.grid(row=5, column=1, pady=2)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

xWidth = 300
yHeight = 300
r = 120

window = Tk() 
window.title("ex19_6.py") 
        
canvas = Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 

print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 繪線
        drawLine(x1, y1, x2, y2)
        # 繪左邊
        paintTree(depth,x2, y2, length*sizeRatio, angle+angleValue)
        # 繪右邊
        paintTree(depth, x2, y2, length*sizeRatio, angle-angleValue)
        
# 繪製p1和p2之間的線條
def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2,tags="myline")

# 顯示
def show():
    canvas.delete("myline")
    myDepth = depth.get()
    paintTree(myDepth, myWidth/2, myHeight, myHeight/3, math.pi/2)
    
# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight) # 建立畫布
canvas.pack()

frame = Frame(tk)                               # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入depth數Entry, 按鈕Button
Label(frame, text="輸入depth : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT,padx=3)
Button(frame, text="Recursive Tree",
       command=show).pack(side=LEFT)
angleValue = math.pi / 4                       # 設定角度
sizeRatio = 0.6                                 # 設定下一層的長度與前一層的比率是0.6

tk.mainloop()

print("------------------------------------------------------------")  # 60個

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
        self.day_is = Button(self)
        
        #按鈕上欲顯示的文字
        self.day_is['text'] = '我是 按鈕\n(Click Me..)'
        
        #按下按鈕由command執行動作，此處呼叫方法display()
        self.day_is['command'] = self.display
        
        # 設定按鈕在主視窗左側，藍色文字，被按下後，關閉主視窗並做資源的釋放
        self.day_is.pack(side = 'left')
        self.QUIT = Button(self, text = 'QUIT',
                fg = 'blue', command = wnd.destroy)
        # 設定按鈕在主視窗右側
        self.QUIT.pack(side = 'right')
        
    #方法三：按下按鈕後會以date類別呼叫today()顯示今天的日期
    def display(self):
        today = date.today()
        print('Day is', today)
        
# 呼叫Tk()建構函式產生主視窗
wnd = Tk()
# 實體化wndApp類別，以主視窗物件為引數做初始化動作
# 然後加入Frame元件，再由Frame加入兩個按鈕
work = wndApp(ruler = wnd)
# 讓視窗程式開始做訊息化輸出
work.mainloop()





print('------------------------------------------------------------')	#60個


from tkinter import *

#建立Frame子類別
class appWork(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()

#產生Frame子類別物件
work = appWork()

# 顯示於視窗標題列
work.master.title('Python GUI')
work.master.maxsize(500, 250)

# 視窗訊息初始化
work.mainloop()


print('------------------------------------------------------------')	#60個



from tkinter import *

# 呼叫Tk()建構式產生主視窗
wnd = Tk()

# 顯示主視窗標題列的文字
wnd.title('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = Button(wnd, text = item, state = item)
    btn.pack()    #以元件加入主視窗
wnd.mainloop()



print('------------------------------------------------------------')	#60個


from tkinter import *

# 呼叫Tk()建構式產生主視窗
root = Tk()
# 方法title()顯示主視窗標題列的文字
root.title('秒數計算中...')
# 呼叫geometry()設視窗大小
root.geometry('100x100+150+150')

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
      label.after(1000, count)
   count()
   
#設定標籤並把它放入主視窗
show = Label(root, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = Button(root, text = 'Stop',
    width = 20, command = root.destroy)
btnStop.pack()
root.mainloop()





print('------------------------------------------------------------')	#60個


import tkinter as tk

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

button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=1)

print('------------------------------------------------------------')	#60個

button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.place(x=0, y=0)
button2.place(x=50, y=30)
button3.place(x=100, y=60)

print('------------------------------------------------------------')	#60個

tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='綠', bg='green', width=20).pack()
tk.Label(window, text='藍', bg='blue', width=20).pack()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()

print('------------------------------------------------------------')	#60個


import tkinter as tk

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

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_2.py

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_3.py

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas.create_rectangle(x1, y1, x2, y2)














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_4.py

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_5.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# 以下以橢圓形為基礎
canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_6.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下是圓形
canvas.create_oval(10, 10, 110, 110)
canvas.create_oval(150, 10, 300, 160, fill='yellow')
# 以下是橢圓形
canvas.create_oval(10, 200, 310, 350)
canvas.create_oval(350, 200, 550, 300, fill='aqua', outline='blue', width=5)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_7.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_8.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
#canvas = Canvas(tk, width=640, height=240, bg='yellow')
canvas.pack()

canvas.create_text(200, 50, text='Ming-Chi Institute of Technology')
canvas.create_text(200, 80, text='Ming-Chi Institute of Technology', fill='blue')
canvas.create_text(300, 120, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='明志科技大學', fill='blue',
                   font=('華康新綜藝體 Std W7',20))


print("------------------------------------------------------------")  # 60個

from tkinter import *

window = Tk()
window.title("ch18_4")              # 視窗標題
label = Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_4_1.py

# ch18_4_1.py
from tkinter import *

window = Tk()
window.title("ch18_4_1")            # 視窗標題
label = Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")
label.pack()                        # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_5.py

# ch18_5.py
from tkinter import *

window = Tk()
window.title("ch18_5")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_6.py

# ch18_6.py
from tkinter import *

window = Tk()
window.title("ch18_6")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM)              # 包裝與定位元件
lab3.pack(side=BOTTOM)              # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_6_1.py

# ch18_6_1.py
from tkinter import *

window = Tk()
window.title("ch18_6")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=BOTTOM)              # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_7.py

# ch18_7.py
from tkinter import *

window = Tk()
window.title("ch18_7")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT)                # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_7_1.py

# ch18_7_1.py
from tkinter import *

window = Tk()
window.title("ch18_7")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT,padx=5)         # 包裝與定位元件,增加x軸間距
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_8.py

# ch18_8.py
from tkinter import *

window = Tk()
window.title("ch18_8")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=RIGHT)               # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_9.py

# ch18_9.py
from tkinter import *

window = Tk()
window.title("ch18_9")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()







print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10.py

# ch18_10.py
from tkinter import *

window = Tk()
window.title("ch18_10")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_1.py

# ch18_10_1.py
from tkinter import *

window = Tk()
window.title("ch18_10_1")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_2.py

# ch18_10_2.py
from tkinter import *

window = Tk()
window.title("ch18_10_2")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_3.py

# ch18_10_3.py
from tkinter import *

window = Tk()
window.title("ch18_10_3")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_11.py

# ch18_11.py
from tkinter import *

window = Tk()
window.title("ch18_11")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_12.py

# ch18_12.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_12")             # 視窗標題
label = Label(window)               # 標籤內容             
btn = Button(window,text="Message",command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13.py

# ch18_13.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_13")             # 視窗標題
label = Label(window)               # 標籤內容             
btn1 = Button(window,text="Message",width=15,command=msgShow)
btn2 = Button(window,text="Exit",width=15,command=window.destroy)
label.pack()                      
btn1.pack(side=LEFT)                # 按鈕1
btn2.pack(side=RIGHT)               # 按鈕2

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_1.py

# ch18_13_1.py
from tkinter import *

def yellow():                   # 設定視窗背景是黃色
    window.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    window.config(bg="blue")
    
window = Tk()
window.title("ch18_13_1")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=blue)
yellowbtn = Button(window,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_2.py

# ch18_13_2.py
from tkinter import *

def bColor(bgColor):          # 設定視窗背景顏色
    window.config(bg=bgColor)
    
window = Tk()
window.title("ch18_13_2")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(window,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_3.py

# ch18_13_3.py
from tkinter import *

window = Tk()
window.title("ch18_13_2")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=lambda:window.config(bg="blue"))
yellowbtn = Button(window,text="Yellow",command=lambda:window.config(bg="yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_14.py

# ch18_14.py
from tkinter import *

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
window = Tk()
window.title("ch18_14")             # 視窗標題

msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
btn = Button(window,text="Hit",command=btn_hit).pack()                   

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_15.py

# ch18_15.py
from tkinter import *

window = Tk()
window.title("ch18_15")         # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)              # 文字方塊1
e2 = Entry(window,show='*')     # 文字方塊2
e1.grid(row=0,column=1)         # 定位文字方塊1
e2.grid(row=1,column=1)         # 定位文字方塊2

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_16.py

# ch18_16.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_16")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
btn1.grid(row=2,column=0)
btn2 = Button(window,text="Quit",command=window.quit)
btn2.grid(row=2,column=1)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_17.py

# ch18_17.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_17")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_18.py

# ch18_18.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_18")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_19.py

# ch18_19.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    e1.delete(0,END)                # 刪除文字方塊1
    e2.delete(0,END)                # 刪除文字方塊2
          
window = Tk()
window.title("ch18_19")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_20.py

# ch18_20.py
from tkinter import *
def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
window = Tk()
window.title("ch18_20")                     # 視窗標題

n1 = IntVar()                   
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = Label(window,width=3,text='+')      # 加號
e2 = Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = Button(window,width=5,text='=',command=add)   # =按鈕
e3 = Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_21.py

# ch18_21.py
from tkinter import *
          
window = Tk()
window.title("ch18_21")             # 視窗標題

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n我的明志工專生活點滴")
text.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_22.py

# ch18_22.py
from tkinter import *
          
window = Tk()
window.title("ch18_22")             # 視窗標題

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)
text.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_23.py

# ch18_23.py
from tkinter import *
          
window = Tk()
window.title("ch18_23")                 # 視窗標題
scrollbar = Scrollbar(window)           # 卷軸物件
text = Text(window,height=2,width=30)   # 文字區域物件
scrollbar.pack(side=RIGHT,fill=Y)       # 靠右安置與父物件高度相同
text.pack(side=LEFT,fill=Y)             # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
    
window = Tk()
window.title("ch18_30")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

html_gif = PhotoImage(file=filename)
Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
    
window = Tk()
window.title("ch18_31")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sselogo = PhotoImage(file=filename)
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """
功蓋三分國，
名成八陣圖。
江流石不轉，
遺恨失吞吳。
"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
    
window = Tk()
window.title("ch18_32")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sselogo = PhotoImage(file=filename)
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """
功蓋三分國，
名成八陣圖。
江流石不轉，
遺恨失吞吳。
"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             justify=LEFT,padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33")             # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33_1")           # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=TOP)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33_2")           # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=CENTER)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個
from tkinter import *

root = Tk()
root.title("ch18_36_1")
label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()  

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
def calculate():                    # 執行計算並顯示結果
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))
    
def show(buttonString):             # 更新顯示區的計算公式
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)

def backspace():                    # 刪除前一個字元
    equ.set(str(equ.get()[:-1]))

def clear():                        # 清除顯示區,放置0
    equ.set("0")

root = Tk()
root.title("計算器")

equ = StringVar()
equ.set("0")                        # 預設是顯示0

# 設計顯示區
label = Label(root,width=25,height=2,relief="raised",anchor=SE,         
              textvariable=equ)
label.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

# 清除顯示區按鈕
clearButton = Button(root,text="C",fg="blue",width=5,command=clear)   
clearButton.grid(row = 1, column = 0)
# 以下是row1的其它按鈕
Button(root,text="DEL",width=5,command=backspace).grid(row=1,column=1)
Button(root,text="%",width=5,command=lambda:show("%")).grid(row=1,column=2)
Button(root,text="/",width=5,command=lambda:show("/")).grid(row=1,column=3)
# 以下是row2的其它按鈕
Button(root,text="7",width=5,command=lambda:show("7")).grid(row=2,column=0)
Button(root,text="8",width=5,command=lambda:show("8")).grid(row=2,column=1)
Button(root,text="9",width=5,command=lambda:show("9")).grid(row=2,column=2)
Button(root,text="*",width=5,command=lambda:show("*")).grid(row=2,column=3)
# 以下是row3的其它按鈕
Button(root,text="4",width=5,command=lambda:show("4")).grid(row=3,column=0)
Button(root,text="5",width=5,command=lambda:show("5")).grid(row=3,column=1)
Button(root,text="6",width=5,command=lambda:show("6")).grid(row=3,column=2)
Button(root,text="-",width=5,command=lambda:show("-")).grid(row=3,column=3)
# 以下是row4的其它按鈕
Button(root,text="1",width=5,command=lambda:show("1")).grid(row=4,column=0)
Button(root,text="2",width=5,command=lambda:show("2")).grid(row=4,column=1)
Button(root,text="3",width=5,command=lambda:show("3")).grid(row=4,column=2)
Button(root,text="+",width=5,command=lambda:show("+")).grid(row=4,column=3)
# 以下是row5的其它按鈕
Button(root,text="0",width=12,
       command=lambda:show("0")).grid(row=5,column=0,columnspan=2)
Button(root,text=".",width=5,
       command=lambda:show(".")).grid(row=5,column=2)
Button(root,text="=",width=5,bg ="yellow",
       command=lambda:calculate()).grid(row=5,column=3)

root.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import random           

def update_data():
    # 更新標籤顯示的數據為1到100的隨機數
    label_data.config(text=str(random.randint(1, 100)))
    # 每1000毫秒(即1秒)後再次調用update_data函數更新數據
    root.after(1000, update_data)

root = tk.Tk()
root.title("數據監控")                      # 視窗標題
# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(root, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程
root.mainloop()

print("------------------------------------------------------------")  # 60個

def buttonClick1():
     buttonvar.set("心想事成，天天開心")

def buttonClick2():
     #改變背景顏色
     button2.config(bg = "blue")  

import tkinter as tk

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

import tkinter as tk

win = tk.Tk()
win.title("Label元件的參數設定")

label = tk.Label(win, bg="#ff00ff", fg="#ffff00", \
                font =("標楷體", 14, "bold", "italic"), \
                padx=5, pady=30, text = "生日快樂")
label.pack()

label = tk.Label(win, bg="#ff00ff", fg="#ffff00", \
                font ="新細明體 14 bold italic", \
                padx=20, pady=5, text = "生日快樂")
label.pack()

win.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局的示範")

plus=tk.Button(win, width=20, text="加法範例")
plus.pack(side="left")
minus=tk.Button(win, width=20, text="減法範例")
minus.pack(side="left")
multiply=tk.Button(win, width=20, text="乘法範例")
multiply.pack(side="left")
divide=tk.Button(win, width=20, text="除法範例")
divide.pack(side="left")

win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("place版面佈局的示範")

plus=tk.Button(win, width=30, text="加法範例")
plus.place(x=10, y=10)
minus=tk.Button(win, width=30, text="減法範例")
minus.place(relx=0.5, rely=0.5, anchor="center")
multiply=tk.Button(win, width=30, text="乘法範例")
multiply.place(relx=0.5, rely=0)
divide=tk.Button(win, width=30, text="除法範例")
divide.place(relx=0.5, rely=0.7)

win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
    
window = tk.Tk()
window.title("用Label顯示文字及圖片")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dog.gif'

pic = tk.PhotoImage(file=filename)
label1 = tk.Label(window,image=pic).pack(side="right")

description ="""
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""
label2 = tk.Label(window,text=description,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")

window.mainloop()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("grid版面佈局的示範")

plus=tk.Button(win, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(win, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(win, width=20, text="乘法範例")
multiply.grid(column=1,row=0)
divide=tk.Button(win, width=20, text="除法範例")
divide.grid(column=1,row=1)

win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk

win = tk.Tk()
win.geometry("400x100")
win.title("grid版面佈局的示範")

plus=tk.Button(win, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(win, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(win, width=20, text="乘法範例")
multiply.grid(column=0,row=2)
divide=tk.Button(win, width=20, text="除法範例")
divide.grid(column=0,row=3)

win.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
wnd = Tk()
wnd.title(' GUI介面- Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('選取的炸物有:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=Label(wnd, text = '請勾選要買的品項：', font = ft1)
lb1.grid(row = 0, column = 0)
item1 = '炸雞排'
var1 = StringVar()
chk = Checkbutton(wnd, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk.grid(row = 1, column = 0)
item2 = '高麗菜'
var2 = StringVar()
chk2 = Checkbutton(wnd, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.grid(row = 2, column = 0)
item3 = '炸花枝'
var3 = StringVar()
chk3 = Checkbutton(wnd, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.grid(row = 3, column = 0)

btnQuit = Button(wnd, text = '離開', font = ft2,
    command = wnd.destroy)
btnQuit.grid(row = 2, column = 1, pady = 4)
btnShow = Button(wnd, text = '購買明細', font = ft2,
    command = check)
btnShow.grid(row = 2, column = 2, pady = 4)
mainloop()


print("------------------------------------------------------------")  # 60個

import sys

import tkinter as tk

# 呼叫Tk()建構式產生主視窗
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
	global resized_tk

	# size 
	width = event.width
	height = event.height

	# create an image
	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)

	# place on the canvas
	canvas.create_image(0,0,image = resized_tk, anchor = 'nw')

def fill_image(event):
	global resized_tk

	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		width = int(event.width) 
		height = int(width / image_ratio)
	else: # canvas is narrower than the image
		height = int(event.height)
		width = int(height * image_ratio) 

	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)

def show_full_image(event):
	global resized_tk

	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		height = int(event.height)
		width = int(height * image_ratio) 
	else: # canvas is narrower than the image
		width = int(event.width) 
		height = int(width / image_ratio)



	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)

# exercise:
# create a third scaling behaviour to always show the full image without cutting off parts

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1)

# import an image 
image_original = Image.open('raccoon.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('python_dark.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
	light_image = Image.open('python_dark.png'),
	dark_image = Image.open('python_light.png'))

# widget
# label = ttk.Label(window, text = 'raccoon', image = image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text = '   A button', image = python_dark_tk, compound = 'left')
button.pack(pady = 10)

button_ctk = ctk.CTkButton(button_frame, text = 'A button', image = img_ctk, compound = 'left')
button_ctk.pack(pady = 10)

button_frame.grid(column = 0, row = 0, sticky = 'nsew')

# canvas -> image
canvas = tk.Canvas(window, background = 'black', bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')

canvas.bind('<Configure>', show_full_image)

window.mainloop()


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


pLabel1= tk.Label(win, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )


text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(win, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(win, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(win, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.messagebox

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

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
text=tk.Text(win)
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



# Frame測試
tk.Label(text = 'Frame測試').pack()
frame1 = tk.Frame(window)
frame1.pack()

label1 = tk.Label(frame1, text = "標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Message測試
tk.Label(text = 'Message測試').pack()

#w = tk.Message(window, text = "this is a relatively long message")    #自動換行
w = tk.Message(window, text = "this is a relatively long message", width = 50)  #限定寬度
w.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線






separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()




print("------------------------------------------------------------")  # 60個


import tkinter as tk
import tkinter.messagebox

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def answer():
    tk.messagebox.showerror('顯示類訊息框',
            '這是messagebox.showerror的訊息框')

def callback():
    tk.messagebox.askyesno('詢問類訊息框', 
            '這是messagebox.askyesno的訊息框')

tk.Button(window, text='顯示詢問訊息框的外觀', command =
          callback).pack(side = 'left', padx = 10)
tk.Button(window, text='顯示錯誤訊息框的外觀', command =
          answer).pack(side = 'left')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

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

def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        tk.messagebox.showinfo("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        tk.messagebox.showinfo("deer的簡介",str2)
    
lb=tk.Label(window,text="請點選想了解的動物簡介:").pack()
choice=tk.IntVar()
choice.set(0)
pic1=tk.PhotoImage(file="image/cattle.gif")
pic2=tk.PhotoImage(file="image/deer.gif")
tk.Radiobutton(window,image=pic1,variable=choice,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=choice,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk

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


print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('500x500')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'green', width = 10)
label3 = ttk.Label(window, text = 'Label 3', background = 'blue', width = 10)

# layout 
# label1.pack()
# label2.pack()

# grid 
window.columnconfigure((0,2), weight = 1, uniform = 'a')    #column 為  0 1 2
window.rowconfigure((0,2), weight = 1, uniform = 'a')       #row 為  0 1 2

'''
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky = 'nsew')
label3.grid(row = 0, column = 1)
'''
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)

# run
window.mainloop()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


