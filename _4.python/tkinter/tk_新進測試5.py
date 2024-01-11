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
