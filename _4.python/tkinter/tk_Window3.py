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
title = "Frame 測試"
window.title(title)

# frame1
frame1 = tk.Frame(window, bg = 'pink', width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame1.pack_propagate(False)
#frame1.pack(side = 'left')
frame1.pack()

# master setting
label = tk.Label(frame1, text = 'Frame1內之Label')
label.pack()

button = tk.Button(frame1, text = 'Frame1內之Button')
button.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

label2 = tk.Label(window, text = 'Frame1外之Label')
#label2.pack(side = 'left')
label2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# frame2
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets 
frame2 = tk.Frame(window, bg = 'yellow')
tk.Label(frame2, text = 'Frame2內之Label').pack()
tk.Button(frame2, text = 'Frame2內之Button').pack()
tk.Entry(frame2).pack()
#frame2.pack(side = 'left')
frame2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()


