import tkinter as tk

def key(event):
    print("鍵碼 : ", repr(event.char))

def callback(event):
    frame.focus_set()
    print('滑鼠位置(' + str(event.x) + ', ' + str(event.y) + ')')

window = tk.Tk()

# 設定主視窗大小
w = 400
h = 400
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "取得滑鼠位置與鍵碼"
window.title(title)

frame = tk.Frame(window, width=300, height=300)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

