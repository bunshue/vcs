import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog

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

def popup():
    popupwindow = tk.Toplevel(window)
    popupwindow.title('新視窗')
    popupwindow.geometry('300x300')
    alert = tk.Label(popupwindow, text='已開啟新視窗')
    button1 = tk.Button(popupwindow, text = '離開此視窗', command = popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()
    
button = tk.Button(window, text='開啟新視窗', command = popup)
button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

def open_file():
    button_ofd_text.set("loading...")
    file = askopenfile(parent=window, mode='rb', title="選取檔案", filetypes=[("Text file", "*.txt")])
    if file:
        print('已選取檔案 : ', file.name)

    button_ofd_text.set("Browse")


#瀏覽檔案按鈕
button_ofd_text = tk.StringVar()
button_ofd = tk.Button(window, textvariable=button_ofd_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
#button_ofd = tk.Button(window, text='選取檔案', command = xxxxxxx)
button_ofd_text.set("Browse")
button_ofd.pack()
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


# Label測試
tk.Label(text='有背景色的Label測試').pack()
tk.Label(window, text='有背景色的Label 紅', bg='red',   width=20).pack()
tk.Label(        text='有背景色的Label 綠', bg='green', width=30).pack()
tk.Label(window, text='有背景色的Label 藍', bg='blue',  width=20).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

# CheckBox測試
tk.Label(text='CheckBox測試').pack(anchor=tk.W)
topping = {0:'海苔', 1:'水煮蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點菜', command=buy).pack(anchor=tk.W)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

# RadioButton測試
tk.Label(text='RadioButton測試').pack()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0:'A套餐',1:'B套餐',2:'C套餐'}
tk.Radiobutton(text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(text = lunch[2], variable = radio_value, value = 2).pack()
def buy():
	value = radio_value.get()
	print(lunch[value])

tk.Button(window, text='點菜', command=buy).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

# RadioButton測試
tk.Label(text='RadioButton測試').pack()

v = tk.IntVar()
tk.Radiobutton(window, text="One", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(window, text="Two", variable=v, value=2).pack(anchor=tk.W)

MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK"),
]

v = tk.StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode)
    b.pack(anchor=tk.W)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

# Entry與Label測試
tk.Label(text='Entry與Label測試').pack()
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

# Button測試
tk.Label(text='Button測試').pack()
def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")


labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable=btntext, command=clickme)
btntext.set("按我！")
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

window.mainloop()

#window.destroy()



