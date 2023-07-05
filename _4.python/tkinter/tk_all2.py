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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def changeString():
    stringToCopy = entry.get()
    #stringToCopy = stringToCopy[::-1]
    #entry.delete(0, tk.END)
    entry.insert(0, stringToCopy)

entry = tk.Entry(window)
button = tk.Button(window, text = "Change", command = changeString)

entry.pack()
button.pack()

def say_hi():
    print("hi there, everyone!")

frame = tk.Frame()
frame.pack()

button = tk.Button(frame, text = "QUIT", fg = "red", command = frame.quit)
button.pack(side = tk.LEFT)

hi_there = tk.Button(frame, text = "Hello", command = say_hi)
hi_there.pack(side = tk.LEFT)

window.mainloop()

