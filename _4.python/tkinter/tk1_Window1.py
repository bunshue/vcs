import sys

import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

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


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
# window.geometry("600x800")
window.wm_title("固定視窗大小")
window.maxsize(width=666, height=480)  # 可拉大之最大大小
window.minsize(width=666, height=480)  # 可拉小之最小大小
window.resizable(width=False, height=False)
# window.resizable(True,False)
# window.resizable(True, False)#可橫向擴展 不可直向擴展

# 設定視窗背景色
# window.configure(bg = "#7AFEC6")
window.configure(bg="yellow")  # 背景色
window.config(bg="green")

print("設定視窗背景顏色")
window["bg"] = "pink"  # 窗口背景色，其他背景色見：blog.csdn.net/chl0000/article/details/7657887

icon_filename = "D:/_git/vcs/_1.data/______test_files1/_material/ims.ico"
window.iconbitmap(icon_filename)  # 更改圖示

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
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

print("設定視窗透明度")
window.attributes("-alpha", 0.9)  # 虛化，值越小虛化程度越高

print("設定視窗最上層顯示")
window.attributes("-topmost", True)

# window.attributes('-disable', True)

# print('設定視窗全螢幕')
# window.attributes('-fullscreen', True)

# ???
# window.attributes("-transparent", True)

# security event
window.bind("<Escape>", lambda event: window.quit())

# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor="se")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Frame 測試")

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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
