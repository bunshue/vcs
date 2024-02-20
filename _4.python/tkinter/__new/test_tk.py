import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


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


save_dir = open_file_dialog()

print(save_dir)

 

window.mainloop()

