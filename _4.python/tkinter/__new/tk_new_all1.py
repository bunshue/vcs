import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

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

print('下拉式選單')

# order.py


def fnOK():
    global order,total		#宣告order,tota為全域變數
    f=selFood.get()  #取得使用者選擇的菜單
    n=selNum.get()   #取得使用者選擇的數量
    i=foods.index(f) #取得菜單在foods串列的索引值
    m=money[i]*n     #計算本次點餐的小計
    total+=m         #計算點餐的總計
    order+='{} {} 碗 {}元\n'.format(foods[i],n,m) #加入本次點餐的資訊
    lblOrder.config(text='{}總計： {} 元'.format(order,total))
    
window = tk.Tk()
window.title('台中肉圓點餐系統')
window.geometry('300x160')

foods = ['肉圓','冬粉湯','魚丸湯']  #菜單項目串列
money=[40,30,30]                  #單價串列
selFood = tk.StringVar()
selFood.set('肉圓')
opnFood=tk.OptionMenu(window, selFood, *foods)
opnFood.config(width=10,font=('微軟正黑體',14))
opnFood.grid(row=0,column=0,pady=5)
selNum = tk.IntVar()
selNum.set(1)
opnNum=tk.OptionMenu(window, selNum, 1,2,3,4,5)
opnNum.config(width=8,font=('微軟正黑體',14))
opnNum.grid(row=0,column=1)
lblOrder=tk.Label(window,text='')
lblOrder.grid(row=1,column=0,columnspan=2,sticky='w')
btnOK=tk.Button(window, text='確定', command=fnOK)
btnOK.grid(row=1,column=1,sticky='n')
order=''    #點餐的文字訊息
total=0     #點餐的總計

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('調色盤')
# palette.py


def fnBg(e):
    red=r.get()	#用get()方法讀取刻度值
    green=g.get()
    blue=b.get()
    color='#{:02x}{:02x}{:02x}'.format(red,green,blue)
    frmColor.config(bg=color)
    
window = tk.Tk()
window.title('調色盤')
window.geometry('250x200')

frmColor=tk.Frame(window,width=100,height=180,relief='raised',borderwidth=3,bg='white')
frmColor.pack(side='left',padx=10)
frmRGB=tk.Frame(window,width=200,height=200)
frmRGB.pack(side='left')
r=tk.IntVar()
sclR=tk.Scale(frmRGB,label='紅：',orient='horizontal',variable=r,from_=0,to=255,command=fnBg)
r.set(255)	#用set()方法設定刻度值
sclR.pack()
g=tk.IntVar()
sclG=tk.Scale(frmRGB,label='綠：',orient='horizontal',variable=g,from_=0,to=255,command=fnBg)
sclG.pack()
g.set(255)
b=tk.IntVar()
sclB=tk.Scale(frmRGB,label='藍：',orient='horizontal',variable=b,from_=0,to=255,command=fnBg)
sclB.pack()
b.set(255)

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

# album.py
# 只能用png ?

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work1.png'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work2.png'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work3.png'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work4.png'

def fnSet(img):
    lblPhoto.config(image=img)
    
window = tk.Tk()
window.title('相簿')
window.geometry('1000x900')

imgPhoto1=tk.PhotoImage(file=filename1)
imgPhoto2=tk.PhotoImage(file=filename2)
imgPhoto3=tk.PhotoImage(file=filename3)
imgPhoto4=tk.PhotoImage(file=filename4)

imgPhoto1_s=imgPhoto1.subsample(4,4)
imgPhoto2_s=imgPhoto2.subsample(4,4)
imgPhoto3_s=imgPhoto3.subsample(4,4)
imgPhoto4_s=imgPhoto4.subsample(4,4)

lblPhoto=tk.Label(window,image=imgPhoto1)
lblPhoto.pack()
lfrmSet=tk.LabelFrame(window,text='選擇照片',relief='raised',borderwidth=2)
lfrmSet.pack()
btn1=tk.Button(lfrmSet,image=imgPhoto1_s,command=lambda:fnSet(imgPhoto1))
btn1.pack(side='left',padx=5)
btn2=tk.Button(lfrmSet,image=imgPhoto2_s,command=lambda:fnSet(imgPhoto2))
btn2.pack(side='left',padx=5)
btn3=tk.Button(lfrmSet,image=imgPhoto3_s,command=lambda:fnSet(imgPhoto3))
btn3.pack(side='left',padx=5)
btn4=tk.Button(lfrmSet,image=imgPhoto4_s,command=lambda:fnSet(imgPhoto4))
btn4.pack(side='left',padx=5)

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




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




