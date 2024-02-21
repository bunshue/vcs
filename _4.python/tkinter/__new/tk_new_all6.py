import sys

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

print('------------------------------------------------------------')	#60個

print("01-TkUI11Canvas")

import tkinter as tk

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

win = tk.Tk()

c1 = tk.Canvas(win, 
           width=1000, 
           height=410)

coord = 10, 10, 100, 100
arc = c1.create_arc(coord, start=0, extent=350, fill="red")

img =  ImageTk.PhotoImage(file = filename)
#c1.create_image(300,100,image = img)
c1.create_image(120+305//2, 10+400//2,image = img)

c1.create_line(500,100,600,10, fill="red", width=3)

c1.create_text(700,50, text="牡丹亭")

c1.create_rectangle(800,50,900,100,fill="blue")

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   c1.create_oval( x1, y1, x2, y2, fill = python_green )

c1.bind( "<B1-Motion>", paint )

c1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("02-TkUI2WindowTitleSize")

import tkinter as tk

win = tk.Tk()
win.wm_title('測試tkinter')
win.minsize(width=666, height=480)
win.maxsize(width=666, height=480)
win.resizable(width=False, height=False)

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("03-TkUI3Label")

import tkinter as tk

win = tk.Tk()

label1 =tk.Label(win,text="Hello World!")
label1.pack()
label2 =tk.Label(win,bg="yellow",text="Hello No2!",fg="red")
label2.pack()
label3 =tk.Label(win,text="Hello No3!")
label3.pack(side="top", anchor="w" )
label4 =tk.Label(win,text="Hello No4!")
label4.place(x=120, y=160)
label5 =tk.Label(win,text="Powen Ko",bg="#ff0000")
label5.place(x=120, y=140)

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("04-TkUI4Image")

import tkinter as tk

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

win = tk.Tk()
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(win, image = img)
label1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("05-TkUI5Button")

import tkinter as tk

def event1():
   print("btn1 pressed.")

win = tk.Tk()
btn1 =tk.Button(win,text="press me",command=event1)
btn1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("06-TkUI6Button2WithImage")

import tkinter as tk
from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

win = tk.Tk()

def event1():
   print("btn1 pressed.")

img = ImageTk.PhotoImage(Image.open(filename))
btn1 =tk.Button(win,text="press me", image=img ,command=event1)
btn1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("07-TkUI7tkMessageBox")

import tkinter as tk
import tkinter.messagebox as tkMessageBox
#import tkinter.messagebox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo('訊息框', "Hello World")

B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("08-TkUI8tkMessageBoxs")

import tkinter as tk
import tkinter.messagebox as tkMessageBox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo('訊息框', "showinfo")
   tkMessageBox.showwarning('訊息框', "showwarning")
   tkMessageBox.showerror('訊息框', "showerror")
   result =tkMessageBox.askquestion('訊息框', "askquestion")
   print(result)
   result=tkMessageBox.askokcancel('訊息框', "askokcancel")
   print(result)
   result=tkMessageBox.askyesno('訊息框', "showeraskyesnoror")
   print(result)
   result=tkMessageBox.askretrycancel('訊息框', "askretrycancel")
   print(result)

B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("09-TkUI9Entry-python2")

import tkinter as tk

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




import sys

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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("button")

import tkinter as tk
win = tk.Tk()
win.title("Button按鈕")
win.geometry('300x200')
button = tk.Button(win, text = "Press", underline=0)
button.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("Checkbutton")

from tkinter import *
wnd = Tk()
wnd.title('Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('這學期預定選修的科目包括:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=Label(wnd, text = '選修的科目：', font = ft1).pack()
item1 = '人工智慧'
var1 = StringVar()
chk1 = Checkbutton(wnd, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk1.pack()
item2 = '程式語言'
var2 = StringVar()
chk2 = Checkbutton(wnd, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.pack()
item3 = '數位行銷'
var3 = StringVar()
chk3 = Checkbutton(wnd, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.pack()
btnShow = Button(wnd, text = '列出選修結果', font = ft2,
    command = check)
btnShow.pack()
mainloop()

print("------------------------------------------------------------")  # 60個

print("entry")

import tkinter as tk
win = tk.Tk()
win.title("密碼資料")
win.geometry('300x200')

label = tk.Label(win, text = "請輸入密碼: ")
label.pack()
entry = tk.Entry(win,bg='yellow',fg='red',show='*')
entry.pack()

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

print("homework2")

from tkinter import *
wnd = Tk()
wnd.title('程式語言能力調查：')
def select():
    print('你的選項是 :', var.get())
ft = ('標楷體', 14)
Label(wnd, 
      text = "請選擇精通的程式語言: ", font = ft,
      justify = LEFT, padx = 20).pack()
place = [('Python語言', 1), ('C語言', 2),
          ('C++語言', 3),('Java語言', 4)]
var = IntVar()
var.set(3)
for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = NW)

print("------------------------------------------------------------")  # 60個

print("label")

import tkinter as tk
win = tk.Tk()
win.title("Label標籤")
label = tk.Label(win, text = "Label標籤")
label.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("menu1")

import tkinter as tk
win = tk.Tk()
win.title("")
win.geometry('300x200')
menubar = tk.Menu(win)
win.config(menu = menubar)
file_menu = tk.Menu(menubar)
menubar.add_cascade(label = "檔案", menu = file_menu)
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("menu2")

import tkinter as tk
win = tk.Tk()
win.title("")
win.geometry('300x200')
menubar = tk.Menu(win,tearoff=0)
win.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("menu3")

import tkinter as tk

win = tk.Tk()
win.title("")
win.geometry('300x200')
menubar = tk.Menu(win,tearoff=0)
win.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("messagebox")

from tkinter import *
from tkinter import messagebox
wnd = Tk()
wnd.title('訊息方塊元件(messagebox)')
wnd.geometry('180x120+20+50')

def first():
    messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

Button(wnd, text='顯示類對話方塊', command =
       first).pack(side = 'left', padx = 10)
Button(wnd, text='詢問類對話方塊', command =
       second).pack(side = 'left')
mainloop()

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

print("Radiobutton")

from tkinter import *
wnd = Tk()
wnd.title('Radiobutton元件')
def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
Label(wnd, 
      text = "請問您的最高學歷: ", font = ft,
      justify = LEFT, padx = 20).pack()
place = [('博士', 1), ('碩士', 2),('大學', 3),
          ('高中', 4),('國中', 5),('國小', 6)]
var = IntVar()
var.set(2)
for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = W)
mainloop()

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



