import sys

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

import tkinter as tk
import tkinter.filedialog as fd

window = tk.Tk()

def open():
    filename = fd.askopenfilename()
    print('open file => ' + filename)

def exit():
    window.destroy()

def find():
    print('find ! ')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)

window.mainloop()


print("------------------------------------------------------------")  # 60個


# 以Menu元件建置功能表
from tkinter import *
from tkinter import messagebox

# 定義回應函式
def New():
    messagebox.showinfo('新檔案',
        '檔案功能表下的開啟新檔指令')
    
def Open():
    messagebox.showinfo('開啟舊檔',
        '檔案功能表下的開啟舊檔指令')

def Save():
    messagebox.showinfo('儲存檔案',
        '檔案功能表下的儲存檔案指令')
    
def Copyright():
    messagebox.showinfo('版權宣告',
        '我的第一支含視窗功能表程式-使用Python語言撰寫')


wnd = Tk()#主視窗物件
wnd.title('GUI介面-Menu')

# 1.產生功能表物件menuBar
menuBar = Menu(wnd)

# 2.將功能表物件menuBar佈置到主視窗的頂部
wnd.config(menu = menuBar)

# 3.加入主功能表項目
menu_file = Menu(menuBar, tearoff = 0)
menu_font = Menu(menuBar, tearoff = 0)
menu_help = Menu(menuBar, tearoff = 0)

# 4. 產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字體大小', menu = menu_font)
menuBar.add_cascade(label = '版權宣告', menu = menu_help)

# 5-1. 加入'檔案'功能表下拉選單
menu_file.add_command(label = '新檔案',
        underline = 1, accelerator = 'Ctrl+N',
        command = New)
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = Open)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        underline = 1, accelerator = 'Ctrl+S',
        command = Save)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        underline = 1, accelerator = 'Ctrl+Q',
        command = lambda : wnd.destroy())

# 5-2. 加入'字體大小'功能表下拉選單
labels = ('大', '中', '小')
for item in labels:
    menu_font.add_radiobutton(label = item)

# 5-3. 加入'版權宣告'功能表下拉選單
menu_help.add_command(label = '原創者聲明', command = Copyright)

mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Application")
        self.create_menu()
        self.pack()

    def create_menu(self):
        # 建立主功能表
        menubar = tk.Menu(self.master)

        # 建立檔案主功能
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="開啟檔案", command=self.open_file)
        file_menu.add_command(label="儲存檔案", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="結束", command=self.master.quit)
        menubar.add_cascade(label="檔案", menu=file_menu)

        # 建立編輯主功能
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="複製", command=self.copy)
        edit_menu.add_command(label="剪下", command=self.cut)
        edit_menu.add_command(label="貼上", command=self.paste)
        menubar.add_cascade(label="編輯", menu=edit_menu)

        # 建立執行主功能
        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="執行程式", command=self.run)
        menubar.add_cascade(label="執行", menu=run_menu)

        # 建立線上說明主功能
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="使用說明", command=self.show_help)
        menubar.add_cascade(label="線上說明", menu=help_menu)

        # 設定主功能表
        self.master.config(menu=menubar)

    def open_file(self):
        print("開啟檔案")

    def save_file(self):
        print("儲存檔案")

    def copy(self):
        print("複製")

    def cut(self):
        print("剪下")

    def paste(self):
        print("貼上")

    def run(self):
        print("執行程式")

    def show_help(self):
        print("使用說明")

# 建立主視窗
root = tk.Tk()

# 建立應用程式
app = Application(master=root)

# 執行主迴圈
app.mainloop()

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
from tkinter import messagebox

wnd = Tk()
wnd.title('訊息方塊元件(messagebox)')
wnd.geometry('180x120+20+50')

def answer():
    messagebox.showerror('顯示類訊息框',
            '這是messagebox.showerror的訊息框')

def callback():
    messagebox.askyesno('詢問類訊息框', 
            '這是messagebox.askyesno的訊息框')

Button(wnd, text='顯示詢問訊息框的外觀', command = callback).pack(side = 'left', padx = 10)
Button(wnd, text='顯示錯誤訊息框的外觀', command = answer).pack(side = 'left')

mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


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


save_dir = open_file_dialog()

print(save_dir)

 

window.mainloop()



print("------------------------------------------------------------")  # 60個


from tkinter import *
from tkinter import messagebox

def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        messagebox.showinfo("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        messagebox.showinfo("deer的簡介",str2)
    
win = Tk()
lb=Label(win,text="請點選想了解的動物簡介:").pack()
choice=IntVar()
choice.set(0)
pic1=PhotoImage(file="cattle.gif")
pic2=PhotoImage(file="deer.gif")
Radiobutton(win,image=pic1,variable=choice,value=0).pack()
Radiobutton(win,image=pic2,variable=choice,value=1).pack()
Button(win,text="進一步了解", command=more).pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from StillClock import StillClock
   
def setNewTime():
    clock.setHour(hour.get())
    clock.setMinute(minute.get())
    clock.setSecond(second.get())
    
window = tk.Tk()
window.title("Change Clock Time")

clock = StillClock(window) # Create a clock
clock.pack()

frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text = "Hour: ").pack(side = tk.LEFT)
hour = tk.IntVar()
hour.set(clock.getHour())
tk.Entry(frame, textvariable = hour, width = 2).pack(side = tk.LEFT) 

tk.Label(frame, text = "Minute: ").pack(side = tk.LEFT)
minute = tk.IntVar()
minute.set(clock.getMinute())
tk.Entry(frame, textvariable = minute, width = 2).pack(side = tk.LEFT)

tk.Label(frame, text = "Second: ").pack(side = tk.LEFT)
second = tk.IntVar()
second.set(clock.getMinute())
tk.Entry(frame, textvariable = second, width = 2).pack(side = tk.LEFT)

tk.Button(frame, text = "設定時間", command = setNewTime).pack(side = tk.LEFT)

window.mainloop()


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




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



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

