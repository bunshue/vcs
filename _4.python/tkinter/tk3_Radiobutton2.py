"""

Radiobutton


"""

import sys
import glob
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image


def printSelection():
    label.config(text="你選的是" + var.get())


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"


window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 4")

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()  # 選項紐綁定的變數
var.set("星星")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rbStar = tk.Radiobutton(
    window, image=tk_image1, variable=var, value="星星", command=printSelection  # 星星選項鈕
)
rbStar.pack()

rbMoon = tk.Radiobutton(
    window, image=tk_image2, variable=var, value="月亮", command=printSelection  # 月亮選項鈕
)
rbMoon.pack()

rbSun = tk.Radiobutton(
    window, image=tk_image3, variable=var, value="太陽", command=printSelection  # 太陽選項鈕
)
rbSun.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printSelection():
    label.config(text="你選的是" + var.get())


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 5")


# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()  # 選項紐綁定的變數
var.set("星星")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rbStar = tk.Radiobutton(
    window,
    image=tk_image1,  # 星星選項鈕
    text="星星",
    compound=tk.RIGHT,
    variable=var,
    value="星星",
    command=printSelection,
)
rbStar.pack()

rbMoon = tk.Radiobutton(
    window,
    image=tk_image2,  # 月亮選項鈕
    text="月亮",
    compound=tk.RIGHT,
    variable=var,
    value="月亮",
    command=printSelection,
)
rbMoon.pack()

rbSun = tk.Radiobutton(
    window,
    image=tk_image3,  # 太陽選項鈕
    text="太陽",
    compound=tk.RIGHT,
    variable=var,
    value="太陽",
    command=printSelection,
)
rbSun.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



