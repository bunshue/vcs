import tkinter as tk
import tkinter.messagebox

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

def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
tk.Label(window, 
      text = "請問您的最高學歷: ", font = ft,
      justify = tk.LEFT, padx = 20).pack()
place = [('博士', 1), ('碩士', 2),('大學', 3),
          ('高中', 4),('國中', 5),('國小', 6)]
var = tk.IntVar()
var.set(2)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = tk.W)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def first():
    tk.messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    tk.messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

tk.Button(window, text='顯示類對話方塊', command = first).pack(side = 'left', padx = 10)
tk.Button(window, text='詢問類對話方塊', command = second).pack(side = 'left')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

sentences="玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"

text = tk.Text(window, width = 30, height = 14, bg = "yellow", wrap=tk.WORD)
text.insert(tk.END,sentences)
text.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print("ScrollBar捲軸")

text = tk.Text(window, width = "30", height = "5")
#text.grid(row = 0, column = 0)
text.pack()
scrollbar = tk.Scrollbar(command = text.yview, orient = tk.VERTICAL)
#scrollbar.grid(row = 0, column = 1, sticky = "ns")
scrollbar.pack()
text.configure(yscrollcommand = scrollbar.set)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
tk.Label(window,
         text = "請選擇精通的程式語言: ", font = ft,
         justify = tk.LEFT, padx = 20).pack()
place = [('Python語言', 1), ('C語言', 2),
         ('C++語言', 3),('Java語言', 4)]
var = tk.IntVar()
var.set(3)

for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
                   font = ft, variable = var, padx = 20,
                   command = select).pack(anchor = tk.NW)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print("密碼資料")

label = tk.Label(window, text = "請輸入密碼: ")
label.pack()
entry = tk.Entry(window,bg='yellow',fg='red',show='*')
entry.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def check(): #回應核取方塊變數狀態
   print('這學期預定選修的科目包括:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '選修的科目：', font = ft1).pack()
item1 = '人工智慧'
var1 = tk.StringVar()
chk1 = tk.Checkbutton(window, text = item1, font = ft1,
                      variable = var1, onvalue = item1, offvalue = '')
chk1.pack()
item2 = '程式語言'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
                   variable = var2, onvalue = item2, offvalue = '')
chk2.pack()
item3 = '數位行銷'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
                      variable = var3, onvalue = item3, offvalue = '')
chk3.pack()
btnShow = tk.Button(window, text = '列出選修結果', font = ft2,
                 command = check)
btnShow.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

button = tk.Button(window, text = "Press", underline=0)
button.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



window.mainloop()

