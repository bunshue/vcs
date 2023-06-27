import tkinter as tk

def key(event):
    print("鍵碼 : ", repr(event.char))

def callback(event):
    frame.focus_set()
    print('滑鼠位置(' + str(event.x) + ', ' + str(event.y) + ')')

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
title = "取得滑鼠位置與鍵碼"
window.title(title)

frame = tk.Frame(window, width=300, height=300)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

