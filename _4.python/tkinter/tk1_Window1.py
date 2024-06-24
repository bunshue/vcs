print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()
window.wm_title("固定視窗大小")
window.minsize(width=666, height=480)
window.maxsize(width=666, height=480)
window.resizable(width=False, height=False)
window.configure(bg="pink")

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("More on the window")

# exercise:
# start window in the middle of the screen
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

print("螢幕解析度 : " + str(display_width) + "*" + str(display_height))

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{left}+{top}")

"""
window_width = 200
window_height = 200
left = 100
top = 100
window.geometry(f'{window_width}x{window_height}+{left}+{top}')
"""

# window sizes
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True,False)

print("設定視窗透明度")
window.attributes("-alpha", 0.9)  # 虛化，值越小虛化程度越高

print("設定視窗最上層顯示")
window.attributes("-topmost", True)

# window.attributes('-disable', True)

# print('設定視窗全螢幕')
# window.attributes('-fullscreen', True)

# security event
window.bind("<Escape>", lambda event: window.quit())

# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor="se")

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
# size = str(w)+'x'+str(h)
# size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

print("設定視窗背景顏色")
window["bg"] = "pink"  # 窗口背景色，其他背景色見：blog.csdn.net/chl0000/article/details/7657887
print("設定視窗透明度")
window.attributes("-alpha", 0.9)  # 虛化，值越小虛化程度越高

# window.attributes("-transparent", True)


def popup():
    popupwindow = tk.Toplevel(window)
    popupwindow.title("新視窗")
    popupwindow.geometry("300x300")
    alert = tk.Label(popupwindow, text="已開啟新視窗")
    button1 = tk.Button(popupwindow, text="離開此視窗", command=popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()


button = tk.Button(window, text="開啟新視窗", command=popup)
button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
# size = str(w)+'x'+str(h)
# size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Frame 測試"
window.title(title)

# frame1
frame1 = tk.Frame(
    window, bg="pink", width=200, height=200, borderwidth=10, relief=tk.GROOVE
)
frame1.pack_propagate(False)
# frame1.pack(side = 'left')
frame1.pack()

# master setting
label = tk.Label(frame1, text="Frame1內之Label")
label.pack()

button = tk.Button(frame1, text="Frame1內之Button")
button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

label2 = tk.Label(window, text="Frame1外之Label")
# label2.pack(side = 'left')
label2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

# frame2
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets
frame2 = tk.Frame(window, bg="yellow")
tk.Label(frame2, text="Frame2內之Label").pack()
tk.Button(frame2, text="Frame2內之Button").pack()
tk.Entry(frame2).pack()
# frame2.pack(side = 'left')
frame2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


window.mainloop()


print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk

extra_window = None


def button1_click():
    print("你按了子視窗的Button")


class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("extra window")
        self.geometry("300x400")
        ttk.Label(self, text="A label").pack()
        ttk.Button(self, text="A button", command=button1_click).pack()
        ttk.Label(self, text="another label").pack(expand=True)


def create_window():
    global extra_window
    print("開啟子視窗")
    extra_window = Extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('extra window')
    # extra_window.geometry('300x400')
    # ttk.Label(extra_window, text = 'A label').pack()
    # ttk.Button(extra_window, text = 'A button').pack()
    # ttk.Label(extra_window, text = 'another label').pack(expand = True)


def close_window():
    print("關閉子視窗")
    if extra_window != None:
        extra_window.destroy()
        print("已關閉子視窗")
    else:
        print("無子視窗可關閉")


# window
window = tk.Tk()
window.geometry("600x400")
window.title("Multiple windows")

button1 = ttk.Button(window, text="開啟子視窗", command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text="關閉子視窗", command=close_window)
button2.pack(expand=True)

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


"""
window.resizable(True, False)#可橫向擴展 不可直向擴展
window.iconbitmap('first.ico')
window.maxsize(500,200) # 可拉大之最大大小
window.minsize(100,200) # 可拉小之最小大小

window.configure(bg='yellow')#背景色

icon_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/ims.ico'
window.iconbitmap(icon_filename)   # 更改圖示


"""
