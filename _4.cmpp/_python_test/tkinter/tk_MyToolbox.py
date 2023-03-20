import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "MyToolbox"
window.title(title)




window.mainloop()

window.destroy() # optional; see description below



