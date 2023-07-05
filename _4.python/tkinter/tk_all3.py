import tkinter as tk

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


'''

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

'''


tk.Label(text='Scale測試').pack()
#w = tk.Scale(window, from_=0, to=100)
w = tk.Scale(window, from_=0, to=100, resolution=0.1)
w.pack()

w = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

print(w.get())


window.mainloop()

