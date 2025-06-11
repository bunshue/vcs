print("------------------------------------------------------------")  # 60個

from tkinter.commondialog import Dialog


class Chooser(Dialog):
    "Ask for a color"

    command = "tk_chooseColor"

    def _fixoptions(self):
        print("1111")
        try:
            # make sure initialcolor is a tk color string
            color = self.options["initialcolor"]
            if isinstance(color, tuple):
                # assume an RGB triplet
                self.options["initialcolor"] = "#%02x%02x%02x" % color
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        print("2222")
        # result can be somethings: an empty tuple, an empty string or
        # a Tcl_Obj, so this somewhat weird check handles that
        if not result or not str(result):
            return None, None  # canceled

        # to simplify application code, the color chooser returns
        # an RGB tuple together with the Tk color string
        r, g, b = widget.winfo_rgb(result)
        return (r / 256, g / 256, b / 256), str(result)


def askcolor(color=None, **options):
    "Ask for a color"

    if color:
        options = options.copy()
        options["initialcolor"] = color

    return Chooser(**options).show()


choose_color = askcolor()
print("你選擇了顏色 : ", choose_color)


print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.colorchooser  # 匯入tkColorChooser模組


def ChooseColor():  # 按鈕事件處理函數
    r = tkinter.colorchooser.askcolor(title="Python Tkinter")  # 建立彩色選取交談視窗
    print(r)  # 輸出傳回值


window = tk.Tk()
button = tk.Button(
    window, text="Choose Color", command=ChooseColor  # 建立按鈕
)  # 指定按鈕事件處理函數
button.pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter.colorchooser import *


def bgUpdate():
    """更改視窗背景顏色"""
    myColor = askcolor()  # 列出色彩對話方塊
    print(type(myColor), myColor)  # 列印傳回值
    root.config(bg=myColor[1])  # 設定視窗背景顏色


root = Tk()
root.title("")
root.geometry("360x240")

btn = Button(text="Select Color", command=bgUpdate)
btn.pack(pady=5)

root.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
