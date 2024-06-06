import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import *

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
print('取得目前螢幕大小')
print(width, height)

window.destroy()  # 關閉視窗

print("------------------------------------------------------------")  # 60個

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
button1 =tk.Button(window,text="press me",command=event1)
button1.pack()

v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def event2():
    print(entry1.get())
    t1=entry1.get()
    v.set(t1)

entry1=tk.Entry(window)
entry1.pack()

button1 =tk.Button(window,text="press me",command=event2)
button1.pack()

v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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

button1 =tk.Button(window,text="press me",command=event3)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def event4():
    t1=float(entry1.get())
    t1=t1/30.5
    print(t1)
    v.set(str(t1))


entry1=tk.Entry(window)
entry1.pack()
button1 =tk.Button(window,text="press me",command=event4)
button1.pack()
v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='綠', bg='green', width=20).pack()
tk.Label(window, text='藍', bg='blue', width=20).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    button1 = tk.Button(window, text = item, state = item)
    button1.pack()    #以元件加入主視窗

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick1():
     buttonvar.set("心想事成，天天開心")

def buttonClick2():
     #改變背景顏色
     button2.config(bg = "blue")  

print("按鈕元件(Button)功能示範 Entry")
    
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print("Label元件的參數設定")

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
print("------------------------------------------------------------")  # 60個

def bless():
     btnvar.set("心想事成，天天開心")

def changecolor():
     button2.config(bg = "blue")  

btnvar = tk.StringVar() 
button1 = tk.Button(window, textvariable=btnvar, command=bless)
btnvar.set("按下我會有祝賀語")
button1.pack(padx=20, pady=10)

button2 = tk.Button(window, text="按我會改變按鈕背景色", command=changecolor)
button2.pack(padx=20, pady=10)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


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
print("------------------------------------------------------------")  # 60個

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
print("pack")
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT,padx=5)         # 增加x軸間距
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def button_hit():                      # 處理按鈕事件
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
button1 = tk.Button(window,text="Hit",command=button_hit).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)
lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM)
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.BOTTOM)
lab2.pack(side=tk.BOTTOM,pady=5)       # 增加y軸間距
lab3.pack(side=tk.BOTTOM)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack(side=tk.LEFT)
lab2.pack(side=tk.LEFT,padx=5)  # 增加x軸間距
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

lab1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
lab2 = tk.Label(window,text="歡迎來到日本",bg="lightgreen",width=15)
lab3 = tk.Label(window,text="歡迎來到加拿大",bg="lightblue",width=15)

lab1.pack()
lab2.pack(side=tk.RIGHT)
lab3.pack(side=tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def button_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("歡迎來到美國")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
window = tk.Tk()
window.geometry("600x400")

msg_on = False                      # 全域變數預設是False    
x = tk.StringVar()                     # Label的變數內容

label = tk.Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
button1 = tk.Button(window,text="Hit",command=button_hit).pack()                   

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

label=tk.Label(window,text="歡迎來到美國",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()  

window.mainloop()

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

buttonQuit = tk.Button(window, text = '離開', font = ft2,
                 command = window.destroy)
#buttonQuit.grid(row = 2, column = 1, pady = 4)
buttonQuit.pack()

buttonShow = tk.Button(window, text = '購買明細', font = ft2,
                 command = check)
#buttonShow.grid(row = 2, column = 2, pady = 4)
buttonShow.pack()

print("------------------------------------------------------------")  # 60個

window=tk.Tk()
window.geometry("600x400")
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
window.geometry("600x400")
window.title('pack配置')
window.configure(bg='white')

label1=tk.Label(window, text = '元件版面配置',font=('微軟正黑體', 16),fg='white',bg='blue')
label2=tk.Label(window, text = '方法',font=('標楷體', 12))
label3=tk.Label(window, text = 'pack()方法',font=('標楷體', 12),bg='lightgreen')
label4=tk.Label(window, text = 'grid()方法',font=('標楷體', 12),bg='pink')
label5=tk.Label(window, text = 'place()方法',font=('標楷體', 12),bg='lightblue')
label1.pack(fill='x')
label2.pack(side='left', fill='y')
label3.pack(pady=5, fill='both', expand=True)
label4.pack(pady=5, fill='both', expand=True)
label5.pack(pady=5, fill='both', expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# place.py

window=tk.Tk()
window.geometry('300x200')
window.configure(bg='white') 
window.title('place配置')

label1=tk.Label(window, text = "五色鳥 Muller's Barbet", font=('微軟正黑體', 18),\
              fg='white',bg='black')
label2=tk.Label(window, text = '啄木鳥目', font=('標楷體', 16),fg='blue',bg='lightblue')
label3=tk.Label(window, text = '五色鳥科', font=('標楷體', 14),fg='green',bg='lightgreen')
msg='分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。'
label4=tk.Label(window, text = msg,font=('細明體', 12),wraplength=170)
label1.place(x=10,y=5,width=280,height=40)
label2.place(x=10,y=50,width=90,height=50)
label3.place(x=10,y=105,width=90,height=50)
label4.place(x=110,y=50,width=180,height=105)

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
window.geometry("600x400")
window.title('BMI計算')
window.configure(bg='white')

labelTitle = tk.Label(window, text='BMI 計算',font=('微軟正黑體', 16),fg='white',bg='blue')
labelTitle.pack(pady=10,fill='x')
tk.Label(window, text='身高(公尺，請輸入浮點數)').pack(pady=5,anchor='w')
userH=tk.DoubleVar()		#宣告userH為浮點數物件
entH = tk.Entry(window,textvariable=userH).pack()  #textvariable參數值為userH
tk.Label(window, text='體重(公斤，請輸入整數)').pack(pady=5,anchor='w')
userW=tk.IntVar()		#宣告userW為整數物件
entW = tk.Entry(window,textvariable=userW).pack()  #textvariable參數值為userW

buttonCal = tk.Button(window, text=' 計算 ', command=fnBmi).pack(pady=5)
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
window.geometry("600x400")
window.title('圓形計算')

lfrmR=tk.LabelFrame(window,text='輸入半徑：')
lfrmR.pack(pady=10)
userR=tk.IntVar()
userR.set(10)
entR= tk.Entry(lfrmR,textvariable=userR).pack(pady=3)
labelMsg=tk.Label(lfrmR, text = '請輸入半徑(整數)然後選擇項目').pack(pady=10)

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
window.geometry("600x400")
window.title('顏色切換')

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
    labelNum['text']=str(num)	#重設標籤文字
    if (num>0):		#若num大於0，就設歸零鈕可以使用
        buttonClear['state']='normal'
    
def fnClear():
    global num
    num = 0
    labelNum['text']=str(num)
    buttonClear['state']='disabled'  #設歸零鈕不能使用
 
window=tk.Tk()
window.geometry("600x400")
window.title('計數器')
window.configure(bg='white')

labelTitle=tk.Label(window, text = '計數器',font=('標楷體', 16),fg='white',bg='blue')
labelNum=tk.Label(window, text = '0',font=('微軟正黑體', 36))

buttonAdd=tk.Button(window, text = '加 1',pady=5,padx=10,command=fnAdd)
buttonClear=tk.Button(window, text = '歸零',pady=5,padx=10,command=fnClear,state='disabled')

labelTitle.pack(pady=10,fill='x')
labelNum.pack(pady=20,fill='x')

buttonAdd.pack(pady=5, side='left',fill='x', expand=True)
buttonClear.pack(pady=5, side='left',fill='x', expand=True)

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
window.geometry("600x400")
window.title('旅遊問卷')

ok=tk.BooleanVar()
chkOK=tk.Checkbutton(window,text='參加旅遊',variable=ok, command=fnOk).pack()
spots=['九份與金瓜石','日月潭','墾丁國家公園']
check={}

buttonSend = tk.Button(window, text=' 送出 ', command=fnMsg).pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterCheck.py

window = tk.Tk()
window.geometry("600x400")

r = tk.StringVar()		# 使用StringVar產生字串變數用於單選框元件
r.set('1')			# 起始化變數值
radio = tk.Radiobutton(window,# 產生單選框元件
			variable = r, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tk.Radiobutton(window,
			variable = r,
			value = '2',# 當勾選該單選框時r的值為2
			text = 'Radio2' )
radio.pack()
radio = tk.Radiobutton(window,
			variable = r,
			value = '3',# 當勾選該單選框時r的值為3
			text = 'Radio3' )
radio.pack()
radio = tk.Radiobutton(window,
			variable = r,
			value = '4',# 當勾選該單選框時r的值為4
			text = 'Radio4' )
radio.pack()
c = tk.IntVar()		# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,# 設定復選框關聯的變數
			onvalue = 1,# 當勾選復選框時，c的值為1
			offvalue = 2)# 當未勾選復選框時，c的值為2
check.pack()

window.mainloop()
print(r.get())			# 輸出r的值
print(c.get())		# 輸出c的值

print("------------------------------------------------------------")  # 60個

# tkinterDialog.py

class MyDialog:		# 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)	# 產生Toplevel元件
        label = tk.Label(self.top, text='Please Input')	# 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)	# 產生文字框元件
        self.entry.pack()
        self.entry.focus()			# 讓文字框獲得焦點
        button = tk.Button(self.top, text='Ok',command=self.Ok)	# 設定按鈕事件處理函數
        button.pack()
    def Ok(self):	# 定義按鈕事件處理函數
        self.input = self.entry.get()		# 取得文字框中內容，儲存為input
        self.top.destroy()			# 銷毀交談視窗
    def get(self):	# 傳回在文字框輸入的內容
        return self.input

class MyButton():	# 定義按鈕類別
    def __init__(self, root, type):			# 按鈕起始化
        self.root = root			# 儲存父視窗參考
        if type == 0:# 根據型態建立不同按鈕
            self.button = tk.Button(root, text='Create',command = self.Create)# 設定Create按鈕的事件處理函數
        else:
            self.button = tk.Button(root, text='Quit',command = self.Quit)# 設定Quit按鈕的事件處理函數
        self.button.pack()
    def Create(self):# Create按鈕的事件處理函數
        d = MyDialog(self.root)			# 產生交談視窗
        self.button.wait_window(d.top)		# 等待交談視窗結束
        print('你輸入了 :' + d.get())		# 取得交談視窗中輸入值，並輸出
    def Quit(self):	# Quit按鈕的事件處理函數
        self.root.quit()			# 離開主視窗

window = tk.Tk()	# 產生主視窗
window.geometry("600x400")

MyButton(window,0)	# 產生Create按鈕
MyButton(window,1)	# 產生Quit按鈕

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

entry1 = tk.Entry(window,		# 產生單行文字框元件
			show = '*',)	# 輸入文字框中的字元被顯示為“*”
entry1.pack()  # 將文字框新增到視窗中
entry2 = tk.Entry(window,
			show = '#',	# 輸入文字框中的字元被顯示為“#”
			width = 50)	# 將文字框的寬度設定為50
entry2.pack()
entry3 = tk.Entry(window,
			bg = 'red',	# 將文字框的背景色設定為紅色
			fg = 'blue')	# 將文字框的前景色設定為藍色
entry3.pack()
entry4 = tk.Entry(window,
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
entry4.pack()
entry5 = tk.Entry(window,
			state = tk.DISABLED)			# 將文字框設定為禁用
entry5.pack()
edit1 = tk.Text(window,		# 產生多行文字框元件
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
edit1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,
			anchor = tk.E,# 設定文字的位置
			bg = 'blue',	# 設定標簽背景色
			fg = 'red',	# 設定標簽前景色
			text = 'Python',# 設定標簽中的文字
			width = 30,	# 設定標簽的寬度為30
			height = 5)	# 設定標簽的的高度為5
label1.pack()
label2 = tk.Label(window,
			text = 'Python GUI\nTkinter',			# 設定標簽中的文字，在字串中使用換行符
			justify = tk.LEFT,# 設定多行文字為齊左
			width = 30,
			height = 5)
label2.pack()
label3 = tk.Label(window,
			text = 'Python GUI\nTkinter',
			justify = tk.RIGHT,			# 設定多行文字為齊右
			width = 30,
			height = 5)
label3.pack()
label4 = tk.Label(window,
			text = 'Python GUI\nTkinter',
			justify = tk.CENTER,			# 設定多行文字為劇中對齊
			width = 30,
			height = 5)
label4.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

"""
r = tk.StringVar()		# 使用StringVar產生字串變數用於單選框元件
r.set('1')			# 起始化變數值

radio = tk.Radiobutton(window,# 產生單選框元件
			variable = r, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '2',# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '3',# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '4',# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()
"""


c = tk.IntVar()		# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,# 設定復選框關聯的變數
			indicatoron = 0,			# 將復選框繪製成按鈕型態
			onvalue = 1,# 當勾選復選框時，c的值為1
			offvalue = 2)# 當未勾選復選框時，c的值為2
check.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.simpledialog	# 匯入tkSimpleDialog模組

def InStr():		# 按鈕事件處理函數
	r = tkinter.simpledialog.askstring('Python Tkinter',	# 建立字串輸入交談視窗
			'Input String',			# 指定提示字元
			initialvalue='Tkinter')		# 指定起始化文字
	print(r)	# 輸出傳回值
def InInt():		# 按鈕事件處理函數
	r = tkinter.simpledialog.askinteger('Python Tkinter','Input Integer')			# 建立整數輸入交談視窗
	print(r)
def InFlo():		# 按鈕事件處理函數
	r = tkinter.simpledialog.askfloat('Python Tkinter','Input Float')			# 建立浮點數輸入交談視窗
	print(r)

window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window,text = 'Input String',	# 建立按鈕
		command = InStr)			# 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tk.Button(window,text = 'Input Integer',
		command = InInt)			# 指定按鈕事件處理函數
button2.pack(side='left')
button2 = tk.Button(window,text = 'Input Float',
		command = InFlo)			# 指定按鈕事件處理函數
button2.pack(side='left')

window.mainloop()

print('------------------------------------------------------------')	#60個
from tkinter.ttk import Separator

window = Tk()
window.geometry("600x400")

#字 前景 背景 寬 高 字位置預設 字型
label=Label(window,text="Welcome to the United States and have a nice day",
            fg="red",bg="gray",
            height=3,width=15,
            font=("Helvetica",8,"bold"))
label.pack()

#字 前景 背景 寬 高 字位置西北
label=Label(window,text="Welcome to the United States and have a nice day",
            fg="blue",bg="lime",
            height=3,width=15,
            anchor="nw")
label.pack()

#字 前景 背景 寬 高 字位置西北 卷寬度
label=Label(window,text="Welcome to the United States and have a nice day",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw",
            wraplength = 80,
            justify="left")     #left / center / right
label.pack()

label=Label(window,bitmap="hourglass")
label.pack()  

label=Label(window,bitmap="hourglass",
            compound="left",text="我的天空")
label.pack()  

label=Label(window,bitmap="hourglass",
            compound="top",text="我的天空")
label.pack()  

label=Label(window,bitmap="hourglass",
            compound="center",text="我的天空")
label.pack()  

label=Label(window,text="raised",relief="raised")
label.pack()

label=Label(window,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10)
label.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label=Label(window,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label=Label(window,text="Welcome to the United States and have a nice day")
label.pack()        # 包裝與定位元件
print(label.keys())

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import Separator

window = Tk()
window.geometry("600x400")

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

label1 = Label(window,text=myTitle,
             font="Helvetic 20 bold")
label1.pack(padx=10,pady=10)

sep = Separator(window,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

label2 = Label(window,text=myContent)
label2.pack(padx=10,pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15

label1.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
label3.pack(side=BOTTOM)

"""
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
"""

"""
label1.pack()
label2.pack(side=RIGHT)               # 靠右包裝與定位元件
label3.pack(side=LEFT)                # 靠左包裝與定位元件
"""

window.mainloop()

print('------------------------------------------------------------')	#60個

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

window = Tk()
window.geometry("600x400")

for Relief in Reliefs:
    Label(window,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

window = Tk()
window.geometry("600x400")

for bitMap in bitMaps:
    Label(window,bitmap=bitMap).pack(side=LEFT,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(pady=10)                  # y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X,pady=10)           # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)                  # Y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",bg="lightblue",
              width=15)             # 標籤寬度是15
label1.pack(padx=50)                  # 左右邊界間距是50像素
label2.pack(padx=50)                  # 左右邊界間距是50像素
label3.pack(padx=50)                  # 左右邊界間距是50像素

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",bg="lightblue",
              width=15)             # 標籤寬度是15
label1.pack(side=LEFT)
label2.pack(side=LEFT,padx=10)        # 左右間距padx=10
label3.pack(side=LEFT)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")
label1.pack()
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")
label1.pack()
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

oklabel=Label(window,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

oklabel=Label(window,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(window,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack()
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(fill=Y)                   # 填滿Y軸包裝與定位元件
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=LEFT)                # 從左配置控件
label2.pack()                         # 預設從上開始配置控件
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=X)                   # 預設從上開始配置控件fill=X

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH)                # 預設從上開始配置控件fill=BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH,expand=True)    # fill=BOTH,expand=True

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")
    
Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=X)  
Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=BOTH,expand=True)  
Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=X)  

window.mainloop() 

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")
    
Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  
Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=LEFT,fill=BOTH,expand=True)  
Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  

window.mainloop() 

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

print("執行前",window.pack_slaves())
oklabel=Label(window,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(window,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10
print("執行後",window.pack_slaves())

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
label2 = Label(window,text="歡迎來到美國",bg="lightgreen",width=15)
label3 = Label(window,text="歡迎來到美國",bg="lightblue",width=15)
label1.place(x=0,y=0)                 # 直接定位
label2.place(x=30,y=50)               # 直接定位
label3.place(x=60,y=100)              # 直接定位

window.mainloop()

print('------------------------------------------------------------')	#60個


def cal():                          # 執行數學式計算
    out.configure(text = "結果 : " + str(eval(equ.get())))


window = Tk()
window.geometry("600x400")

label = Label(window, text="請輸入數學表達式:")
label.pack()

equ = Entry(window)                   # 在此輸入表達式
equ.pack(pady=5)                    

out = Label(window)                   # 存放計算結果
out.pack()                          

button1 = Button(window,text="計算",command=cal)    # 計算按鈕
button1.pack(pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

def button_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
window = Tk()
window.geometry("600x400")

msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = Label(window,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   

button1 = Button(window,text="Click Me",command=button_hit)
button1.pack()                   

window.mainloop()

print('------------------------------------------------------------')	#60個

def button_hit():                      # 處理按鈕事件
    if x.get() == "":               # 如果目前是空字串
        x.set("I like tkinter")     # 顯示文字
    else:
        x.set("")                   # 不顯示文字
   
window = Tk()
window.geometry("600x400")

x = StringVar()                     # Label的變數內容

label = Label(window,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   

button1 = Button(window,text="Click Me",command=button_hit)
button1.pack()                   

window.mainloop()

print('------------------------------------------------------------')	#60個

def callback(*args):
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
window = Tk()
window.geometry("600x400")

xE = StringVar()                        # Entry的變數內容
entry = Entry(window,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

window.mainloop()

print('------------------------------------------------------------')	#60個

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
window = Tk()
window.geometry("600x400")

xE = StringVar()                        # Entry的變數內容
entry = Entry(window,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

xL = StringVar()                        # Label的變數內容
label = Label(window,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)   

window.mainloop()

print('------------------------------------------------------------')	#60個

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
  
window = Tk()
window.geometry("600x400")

xE = StringVar()                        # Entry的變數內容

entry = Entry(window,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW
xE.trace("r",callbackR)                 # 若是有被讀取執行callbackR

xL = StringVar()                        # Label的變數內容
label = Label(window,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

button1 = Button(window,text="讀取",command=hit)    # 建立讀取按鈕
button1.pack(pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 
  
window = Tk()
window.geometry("600x400")

xE = StringVar()                        # Entry的變數內容

entry = Entry(window,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW

xL = StringVar()                        # Label的變數內容
label = Label(window,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

window = Tk()
window.geometry("600x400")

var = IntVar()                                  # 選項紐綁定的變數
var.set(1)                                      # 預設選項是男生
                       
label = Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=var,value=1,
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=var,value=2,
                      command=printSelection)
rbwoman.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    label.config(text="你是"+var.get())

window = Tk()
window.geometry("600x400")

var = StringVar()                               # 選項紐綁定的變數
var.set("男生")                                 # 預設選項是男生
                       
label = Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=var,value="男生",
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=var,value="女生",
                      command=printSelection)
rbwoman.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = Tk()
window.geometry("600x400")

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                variable=var,value=val, 
                command=printSelection).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = Tk()
window.geometry("600x400")

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import Tk
from tkinter.ttk import Frame, Style

"""fail
window = Tk()
window.geometry("600x400")

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(window,bg=fm,height=50,width=250).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(bg=fm,height=50,width=250).pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

# 用字典儲存框架顏色與游標外形
fms = {'red':'cross','green':'boat','blue':'clock'}
for fmColor in fms:         # 建立3個不同底色的框架與游標外形
    Frame(window,bg=fmColor,cursor=fms[fmColor],
          height=50,width=200).pack(side=LEFT)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

frameUpper = Frame(window,bg="lightyellow")   # 建立上層框架
frameUpper.pack()
buttonRed = Button(frameUpper,text="Red",fg="red")
buttonRed.pack(side=LEFT,padx=5,pady=5)
buttonGreen = Button(frameUpper,text="Green",fg="green")
buttonGreen.pack(side=LEFT,padx=5,pady=5)
buttonBlue = Button(frameUpper,text="Blue",fg="blue")
buttonBlue.pack(side=LEFT,padx=5,pady=5)

frameLower = Frame(window,bg="lightblue")     # 建立下層框架
frameLower.pack()
buttonPurple = Button(frameLower,text="Purple",fg="purple")
buttonPurple.pack(side=LEFT,padx=5,pady=5)

window.mainloop()
"""
print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

fm1 = Frame(width=150,height=80,relief=GROOVE, borderwidth=5)
fm1.pack(side=LEFT,padx=5,pady=10)

fm2 = Frame(width=150,height=80,relief=RAISED, borderwidth=5)
fm2.pack(side=LEFT,padx=5,pady=10)

fm3 = Frame(width=150,height=80,relief=RIDGE, borderwidth=5)
fm3.pack(side=LEFT,padx=5,pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

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

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

tl = Toplevel()
Label(tl,text = 'I am a Toplevel').pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")

Label(tl,text = 'I am a Toplevel').pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

import random

window = Tk()
window.geometry("600x400")

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

button1 = Button(window,text='Click Me',command = MyAnswer)
button1.pack()

window.mainloop()

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
    
window = Tk()
window.geometry("600x400")

button1 = Button(window,text="Click me",command=buttonClicked)
button1.pack(anchor=W)

varPython = BooleanVar()
cbnPython = Checkbutton(window,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(window,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(window,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

window.mainloop()

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
                         
window = Tk()
window.geometry("600x400")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

entry = Entry()
entry.grid(row=0,column=0,padx=5,sticky=W+E)

button1 = Button(window,text="搜尋",command=mySearch)
button1.grid(row=0,column=1,padx=5,pady=5)

# 建立Text
text = Text(window,undo=True)
text.grid(row=1,column=0,columnspan=2,padx=3,pady=5,
          sticky=N+S+W+E)

text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("found", background="yellow")    # 定義未來找到的標籤定義

window.mainloop()

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
                            
window = Tk()
window.geometry("600x400")

# 建立工具列
toolbar = Frame(window,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

chkButton = Button(toolbar,text="拼字檢查",command=spellingCheck)
chkButton.pack(side=LEFT,padx=5,pady=5)

clrButton = Button(toolbar,text="清除",command=clrText)
clrButton.pack(side=LEFT,padx=5,pady=5)

# 建立Text
text = Text(window,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

text.tag_configure("spellErr", foreground="red")    # 定義未來找到的標籤定義
with open("myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")              # 自訂字典串列
    
window.mainloop()

print("------------------------------------------------------------")  # 60個

    
def saveFile():
    textContent = text.get("1.0",END)
    filename = "tmp_write_file.txt"
    with open(filename,"w") as output:
        output.write(textContent)
        window.title(filename)
                            
window = Tk()
window.geometry("600x400")

menubar = Menu(window)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=window.destroy)
window.config(menu=menubar)           # 顯示功能表物件

# 建立Text
text = Text(window,undo=True)
text.pack(fill=BOTH,expand=True)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

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
        self.day_is = tk.Button(self)
        
        #按鈕上欲顯示的文字
        self.day_is['text'] = '我是 按鈕\n(Click Me..)'
        
        #按下按鈕由command執行動作，此處呼叫方法display()
        self.day_is['command'] = self.display
        
        # 設定按鈕在主視窗左側，藍色文字，被按下後，關閉主視窗並做資源的釋放
        self.day_is.pack(side = 'left')
        self.QUIT = tk.Button(self, text = 'QUIT',
                fg = 'blue', command = window.destroy)
        # 設定按鈕在主視窗右側
        self.QUIT.pack(side = 'right')
        
    #方法三：按下按鈕後會以date類別呼叫today()顯示今天的日期
    def display(self):
        today = date.today()
        print('Day is', today)
        
window = tk.Tk()
window.geometry("600x400")

# 實體化wndApp類別，以主視窗物件為引數做初始化動作
# 然後加入Frame元件，再由Frame加入兩個按鈕
work = wndApp(ruler = window)
work.mainloop()

print('------------------------------------------------------------')	#60個


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

window = Tk()
window.geometry("600x400")

button1 = Button(window,text="列印訊息",width=15,command=msgShow)
button2 = Button(window,text="結束",width=15,command=window.destroy)
                     
button1.pack(side=tk.LEFT)                # 按鈕1
button2.pack(side=tk.RIGHT)               # 按鈕2

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("pack版面佈局")

taipei=tk.Button(window, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(window, width=20, text="高雄景點")
kaohsiung.pack(side="top")

print("------------------------------------------------------------")  # 60個
print(".bind")
print("------------------------------------------------------------")  # 60個

def fnEnter(event):
    labelTest['bg']='lightblue'

def fnLeave(event):
    labelTest.config(text='試試看',bg='gray')
    
def fnMotion(event):
    labelTest['text']='游標移動'

def fnClick(event):
    global mx,my	#宣告mx,my為全域變數
    mx=event.x	#紀錄按下時滑鼠游標的x坐標
    my=event.y	#紀錄按下時滑鼠游標的y坐標
    
def fnB1Motion(event):
    global mx,my	#宣告mx,my為全域變數
    labelX=labelTest.winfo_rootx()-window.winfo_rootx()	#計算labelTest在視窗的x坐標
    labelY=labelTest.winfo_rooty()-window.winfo_rooty()	#計算labelTest在視窗的y坐標
    labelTest['text']='拖曳中...'
    labelTest.place(x=labelX+(event.x-mx),y=labelY+(event.y-my))	#重設labelTest位置
    
window = tk.Tk()
window.geometry("600x400")
window.title('滑鼠事件測試')

mx=0
my=0
labelTest=tk.Label(window,text='試試看',width=8,height=2,relief='groove',bg='gray')
labelTest.place(x=80,y=100)
labelTest.bind('<Enter>',fnEnter) #<Enter>事件綁定fnEnter事件處理函式
labelTest.bind('<Leave>',fnLeave) #<Leave>事件綁定fnLeave事件處理函式
labelTest.bind('<Motion>',fnMotion) #<Motion>事件綁定fnMotion事件處理函式
labelTest.bind('<Button-1>',fnClick) #<Button-1>事件綁定fnClick事件處理函式
labelTest.bind('<B1-Motion>',fnB1Motion) #<B1-Motion>事件綁定fnB1Motion事件處理函式

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
    labelMsg.config(text=msg[iArea][iNM]) #重設標籤的文字內容
    
window = tk.Tk()
window.geometry("600x400")
window.title('台灣夜市簡介')

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
labelMsg=tk.Label(lfrmMsg,text=msg[0][0],font=(12),wraplength=120,justify='left')
labelMsg.pack(anchor='n')

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
    
window = Tk()
window.geometry("600x400")

button1 = Button(window,text="Click me")
button1.pack(anchor=W)
button1.bind("<Button-1>",buttonClicked)  # 按一下Click me綁定buttonClicked方法

varPython = BooleanVar()
cbnPython = Checkbutton(window,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(window,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(window,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def callback(event):                        # 事件處理程式
    print("滑鼠點擊位置 :", event.x, event.y)   # 列印座標
    
window = Tk()
window.geometry("600x400")

frame = Frame(window,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "滑鼠位置 : x:{}, y:{}".format(x,y)
    var.set(textvar)
    
window = Tk()
window.geometry("600x400")

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(window,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

window.bind("<Motion>",mouseMotion)   # 增加事件處理程式

window.mainloop()

print('------------------------------------------------------------')	#60個

def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
window = Tk()
window.geometry("600x400")

button1 = Button(window,text="離開",command=window.destroy)
button1.pack(pady=30)
button1.bind("<Enter>",enter)               # 進入綁定enter
button1.bind("<Leave>",leave)               # 離開綁定leave

x = StringVar()
lab = Label(window,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

window.mainloop()

print('------------------------------------------------------------')	#60個

def leave(event):                       # <Esc>事件處理程式
    print('你按了 ESC')
   
window = Tk()
window.geometry("600x400")

window.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = Label(window,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

window.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
window = Tk()
window.geometry("600x400")

window.bind("<Key>",key)              # <Key>鍵綁定key函數

window.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
window = Tk()
window.geometry("600x400")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
window = Tk()
window.geometry("600x400")

button1 = Button(window,text="tkinter")
button1.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()                  # 建立核取方塊
button2 = Checkbutton(window,text="bind/unbind",variable=var,
                   command=lambda:toggle(button1))
button2.pack(anchor=W,padx=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

def buttonClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def buttonClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter")
    
window = Tk()
window.geometry("600x400")

button1 = Button(window,text="tkinter",command=buttonClicked1)
button1.pack(anchor=W,padx=10,pady=10)
button1.bind("<Button-1>",buttonClicked2,add="+")  # 增加事件處理程式

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.tag_config(SEL,font=f)
      
window = Tk()
window.geometry("600x400")

# 建立工具列
toolbar = Frame(window,relief=RAISED,borderwidth=1)
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
text = Text(window)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                        # size family更新
    f=Font(size=sizeVar.get())                  # 取得新font size
    text.tag_config(SEL,font=f)
      
window = Tk()
window.geometry("600x400")

# 建立工具列
toolbar = Frame(window,relief=RAISED,borderwidth=1)
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
text = Text(window)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)

text.insert(END,"黃鶴樓送孟浩然之廣陵\t李白\n","a")     # 插入時同時設定Tag

text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

text.focus_set()
# 將Tag a設為置中,藍色,含底線
text.tag_config("a",foreground="blue",justify=CENTER,underline=True)

window.mainloop()

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


print('右鍵選單')

window = Tk()
window.geometry("600x400")

popupmenu = Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(window)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

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

window = Tk()
window.geometry("600x400")

popupmenu = Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(window)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

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

window = Tk()
window.geometry("600x400")

popupmenu = Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = Frame(window,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

# 建立Button
undoButton = Button(toolbar,text="Undo",command=undoJob)
undoButton.pack(side=LEFT,pady=2)
redoButton = Button(toolbar,text="Redo",command=redoJob)
redoButton.pack(side=LEFT,pady=2)

# 建立Text
text = Text(window,undo=True)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

print("------------------------------------------------------------")  # 60個
def paint(event):                           # 拖曳可以繪圖
    x1,y1 = (event.x, event.y)              # 設定左上角座標
    x2,y2 = (event.x, event.y)              # 設定右下角座標
    canvas.create_oval(x1,y1,x2,y2,fill="blue")

def cls():                                  # 清除畫面
    canvas.delete("all")
    
tk = Tk()
tk.geometry("600x400")

lab = Label(tk,text="拖曳滑鼠可以繪圖")     # 建立標題
lab.pack()
canvas = Canvas(tk,width=640, height=300)   # 建立畫布
canvas.pack()

button1 = Button(tk,text="清除",command=cls)    # 建立清除按鈕
button1.pack(pady=5)

canvas.bind("<B1-Motion>",paint)            # 滑鼠拖曳綁定paint

canvas.mainloop()

print("------------------------------------------------------------")  # 60個

""" 搬出


button1 = tk.Button(window, text='pack置中', width=20).pack()
button2 = tk.Button(window, text='pack左', width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text='pack右', width=20).pack(side=tk.RIGHT)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#設定視窗背景色
window.config(bg="red")
window.config(bg="green")
window.config(bg="blue")
    

# 將4個鈕包裝定位在右下方
button4.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button3.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button2.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button1.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

"""


from tkinter import *
print("------------------------------------------------------------")  # 60個
print("xxxxxx")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("xxxxxxx")
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個







"""
lab = Label(window,text="請選擇喜歡的運動",fg="blue",bg="lightyellow",width=30)
lab.grid(row=0)
"""



label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")








print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("pack版面佈局的示範")

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
window.geometry("600x400")

