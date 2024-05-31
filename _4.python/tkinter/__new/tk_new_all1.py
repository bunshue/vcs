import sys

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

import tkinter.messagebox

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

print("pack版面佈局")

taipei=tk.Button(window, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(window, width=20, text="高雄景點")
kaohsiung.pack(side="top")

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
window.title('秒數計算中...')
window.geometry('100x100+150+150')

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
show = tk.Label(window, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = tk.Button(window, text = 'Stop',
    width = 20, command = window.destroy)
btnStop.pack()

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

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = tk.Tk()

label = tk.Label(window)               # 標籤內容             
btn1 = tk.Button(window,text="Message",width=15,command=msgShow)
btn2 = tk.Button(window,text="Exit",width=15,command=window.destroy)
label.pack()                      
btn1.pack(side=tk.LEFT)                # 按鈕1
btn2.pack(side=tk.RIGHT)               # 按鈕2

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

import random           

def update_data():
    # 更新標籤顯示的數據為1到100的隨機數
    label_data.config(text=str(random.randint(1, 100)))
    # 每1000毫秒(即1秒)後再次調用update_data函數更新數據
    window.after(1000, update_data)

window = tk.Tk()
window.title("數據監控")                      # 視窗標題
# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(window, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程

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
        tk.messagebox.showinfo("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        tk.messagebox.showinfo("deer的簡介",str2)
    
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



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

scrollbar = tk.Scrollbar(window)           # 卷軸物件
text = tk.Text(window,height=2,width=30)   # 文字區域物件
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)       # 靠右安置與父物件高度相同
text.pack(side=tk.LEFT,fill=tk.Y)             # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(tk.END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(tk.END,str)

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


tkinter.messagebox.showinfo("Error","This word is not present in our lexicon\nDouble check it.")
tkinter.messagebox.showinfo("Error","This word is not present in our lexicon showing results for %s instead"% "aaaaa")

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個







#grid 大全

print("grid")

print("grid版面佈局")

taipei=tk.Button(window, width=30, text="台北景點")
taipei.grid(column=0,row=0)
kaohsiung=tk.Button(window, width=30, text="高雄景點")
kaohsiung.grid(column=0,row=1)
ilan=tk.Button(window, width=30, text="宜蘭景點")
ilan.grid(column=1,row=0)
tainan=tk.Button(window, width=30, text="台南景點")
tainan.grid(column=1,row=1)
	

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("100x100")
window.title("grid佈局")

one=tk.Button(window, width=20, text="January")
one.grid(column=0,row=0)
two=tk.Button(window, width=20, text="Februry")
two.grid(column=1,row=0)
three=tk.Button(window, width=20, text="March")
three.grid(column=2,row=0)
one=tk.Button(window, width=20, text="April")
one.grid(column=0,row=1)
two=tk.Button(window, width=20, text="May")
two.grid(column=1,row=1)
three=tk.Button(window, width=20, text="June")
three.grid(column=2,row=1)
one=tk.Button(window, width=20, text="July")
one.grid(column=0,row=2)
two=tk.Button(window, width=20, text="August")
two.grid(column=1,row=2)
three=tk.Button(window, width=20, text="September")
three.grid(column=2,row=2)
one=tk.Button(window, width=20, text="October")
one.grid(column=0,row=3)
two=tk.Button(window, width=20, text="November")
two.grid(column=1,row=3)
three=tk.Button(window, width=20, text="December")
three.grid(column=2,row=3)

window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
n1 = tk.IntVar()                   
n2 = tk.IntVar()
n3 = tk.IntVar()

e1 = tk.Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = tk.Label(window,width=3,text='+')      # 加號
e2 = tk.Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = tk.Button(window,width=5,text='=',command=add)   # =按鈕
e3 = tk.Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


print("------------------------------------------------------------")  # 60個


window = tk.Tk()

lab1 = tk.Label(window,text="Peter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="John",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="Notron",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab4 = tk.Label(window,text="Kevin",
              bg="lightgreen",      # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab5 = tk.Label(window,text="Tommy",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab6 = tk.Label(window,text="Mary",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab7 = tk.Label(window,text="Tracy",
              bg="lightblue",       # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab8 = tk.Label(window,text="Mike",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab9 = tk.Label(window,text="Vicent",
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

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab3 = tk.Label(window,text="標籤3",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab6 = tk.Label(window,text="標籤6",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
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

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab6 = tk.Label(window,text="標籤6",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab3 = tk.Label(window,text="標籤3",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
window = tk.Tk()

n1 = tk.IntVar()                   
n2 = tk.IntVar()
n3 = tk.IntVar()

e1 = tk.Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = tk.Label(window,width=3,text='+')      # 加號
e2 = tk.Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = tk.Button(window,width=5,text='=',command=add)   # =按鈕
e3 = tk.Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()

print("------------------------------------------------------------")  # 60個
          

window = tk.Tk()
window.geometry("400x100")
window.title("grid版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(window, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.grid(column=1,row=0)
divide=tk.Button(window, width=20, text="除法範例")
divide.grid(column=1,row=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x100")
window.title("grid版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(window, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.grid(column=0,row=2)
divide=tk.Button(window, width=20, text="除法範例")
divide.grid(column=0,row=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
pLabel1= tk.Label(window, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )


text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(window, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(window, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(window, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

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

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

"""
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky = 'nsew')
label3.grid(row = 0, column = 1)
"""

label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)

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
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝
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
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

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
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""

label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件


lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝


button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=1)


"""



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#account - password

window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)              # 文字方塊1
e2 = tk.Entry(window,show='*')     # 文字方塊2
e1.grid(row=0,column=1)         # 定位文字方塊1
e2.grid(row=1,column=1)         # 定位文字方塊2

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

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

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

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
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    e1.delete(0,tk.END)                # 刪除文字方塊1
    e2.delete(0,tk.END)                # 刪除文字方塊2
          
window = tk.Tk()

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
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個



window = tk.Tk()
window.title(' GUI介面- Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('選取的炸物有:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '請勾選要買的品項：', font = ft1)
lb1.grid(row = 0, column = 0)
item1 = '炸雞排'
var1 = tk.StringVar()
chk = tk.Checkbutton(window, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk.grid(row = 1, column = 0)
item2 = '高麗菜'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.grid(row = 2, column = 0)
item3 = '炸花枝'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.grid(row = 3, column = 0)

btnQuit = tk.Button(window, text = '離開', font = ft2,
    command = window.destroy)
btnQuit.grid(row = 2, column = 1, pady = 4)
btnShow = tk.Button(window, text = '購買明細', font = ft2,
    command = check)
btnShow.grid(row = 2, column = 2, pady = 4)

window.mainloop()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




#place 大全

print("------------------------------------------------------------")  # 60個

print("place版面佈局")

taipei=tk.Button(window, width=30, text="台北景點")
taipei.place(x=10, y=10)
kaohsiung=tk.Button(window, width=30, text="高雄景點")
kaohsiung.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()

print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.place(x=0, y=0)
button2.place(x=50, y=30)
button3.place(x=100, y=60)

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("400x100")
window.title("place版面佈局的示範")

plus=tk.Button(window, width=30, text="加法範例")
plus.place(x=10, y=10)
minus=tk.Button(window, width=30, text="減法範例")
minus.place(relx=0.5, rely=0.5, anchor="center")
multiply=tk.Button(window, width=30, text="乘法範例")
multiply.place(relx=0.5, rely=0)
divide=tk.Button(window, width=30, text="除法範例")
divide.place(relx=0.5, rely=0.7)

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
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

window.mainloop()

"""
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位
"""

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




