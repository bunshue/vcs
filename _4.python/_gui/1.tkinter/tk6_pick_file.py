"""



"""

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import tkinter as tk

import tkinter.filedialog

window = tk.Tk()

# 設定主視窗大小
W = 640
H = 480
x_st = 100
y_st = 100
# size = str(W)+'x'+str(H)
# size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title("選取檔案")

# 設定主視窗之背景色
# window.configure(bg = "#7AFEC6")


def open_file():
    button_ofd_text.set("開啟檔案...")
    file = tkinter.filedialog.askopenfile(
        parent=window, mode="rb", title="選取檔案", filetypes=[("Text file", "*.txt")]
    )
    if file:
        print("已選取檔案 : ", file.name)

    button_ofd_text.set("開啟檔案")


# 開啟檔案按鈕
button_ofd_text = tk.StringVar()

button_ofd = tk.Button(
    window,
    textvariable=button_ofd_text,
    command=lambda: open_file(),
    font="Raleway",
    bg="#20bebe",
    fg="white",
    height=2,
    width=15,
)
# button_ofd = tk.Button(window, text = "選取檔案", command=lambda: open_file())

button_ofd_text.set("選取檔案")
button_ofd.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
