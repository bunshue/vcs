import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

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

def open_file():
    button_ofd_text.set("開啟檔案...")
    file = askopenfile(parent = window, mode = 'rb', title = "選取檔案", filetypes = [("Text file", "*.txt")])
    if file:
        print('已選取檔案 : ', file.name)

    button_ofd_text.set("開啟檔案")

def save_file():
    button_sfd_text.set("另存新檔...")
    file = asksaveasfile(parent = window, mode = 'w', title = "選取檔案", filetypes = [("Text file", "*.txt")])
    if file:
        print('另存新檔 : ', file.name)

    button_sfd_text.set("另存新檔")

#開啟檔案按鈕
button_ofd_text = tk.StringVar()
button_ofd = tk.Button(window, textvariable = button_ofd_text, command = lambda:open_file(), font = "Raleway", bg = "#20bebe", fg = "white", height = 2, width = 15)
#button_ofd = tk.Button(window, text = '選取檔案', command = xxxxxxx)
button_ofd_text.set("開啟檔案")
button_ofd.pack()

#另存新檔按鈕
button_sfd_text = tk.StringVar()
button_sfd = tk.Button(window, textvariable = button_sfd_text, command = lambda:save_file(), font = "Raleway", bg = "#20bebe", fg = "white", height = 2, width = 15)
#button_sfd = tk.Button(window, text = '選取檔案', command = xxxxxxx)
button_sfd_text.set("另存新檔")
button_sfd.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

button5 = tk.Button(window, text = '指定按鍵大小', width = 20, height = 5)
button5.pack()  #pack無參數, 控件置中

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Button測試
tk.Label(text = 'Button測試').pack()
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
label1 = tk.Label(window, fg = "red", textvariable = labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable = btntext, command = clickme)
btntext.set("按我！")
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def click1():
    textvar.set("我已經被按過了！")

textvar = tk.StringVar()
button1 = tk.Button(window, textvariable = textvar, command = click1)
textvar.set("按鈕")
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

button_exit = tk.Button(window, text = "關閉視窗", command = window.destroy)
button_exit.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def buttonClick():
    global count
    count = count + 1
    print("Beep! " + str(count))
    button1.config(text = "Clicked " + str(count))

count = 0;

button1 = tk.Button(window, text = "按鍵數次數, 不指定按鍵大小", command = buttonClick)
button1.pack(side = tk.LEFT)    #靠左對齊

button2 = tk.Button(window, text = "離開", command = '')
button2.pack(side = tk.RIGHT)   #靠右對齊

#side=tk.RIGHT



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
#frame0.grid(row = 1, column = 1, sticky = tk.W)
frame0.pack()

# Create images
plusImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/plus.gif")
minusImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/minus.gif")
timesImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/times.gif")
divideImage = tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/operation/divide.gif")

tk.Button(frame0, image = plusImage, command = '').grid(row = 1, column = 1, sticky = tk.W)
tk.Button(frame0, image = minusImage, command = '').grid(row = 1, column = 2)
tk.Button(frame0, image = timesImage, command = '').grid(row = 1, column = 3)
tk.Button(frame0, image = divideImage, command = '').grid(row = 1, column = 4)

# Add buttons to frame2
frame2 = tk.Frame(window) # Create and add a frame to window
#frame2.grid(row = 3, column = 1, pady = 10, sticky = tk.E)
frame2.pack()
tk.Button(frame2, text = "Add", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Subtract", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Multiply", command = '').pack(side = tk.LEFT)
tk.Button(frame2, text = "Divide", command = '').pack(side = tk.LEFT)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線





window.mainloop()
