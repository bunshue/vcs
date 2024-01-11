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

