'''
Grid 測試
'''
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
title = "Grid 測試"
window.title(title)

#window.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = tk.Frame(window, bg = 'cyan', width = 450, height = 50, pady = 3)
center = tk.Frame(window, bg = 'gray2', width = 50, height = 40, padx = 3, pady = 3)

#layout all of the main containers
window.grid_rowconfigure(1, weight = 2)
window.grid_columnconfigure(0, weight = 1)

top_frame.grid(row = 0, sticky = "ew")
center.grid(row = 1, sticky = "nsew")

# create the widgets for the top frame
model_label = tk.Label(top_frame, text = 'Model Dimensions')
width_label = tk.Label(top_frame, text = 'Width:')
length_label = tk.Label(top_frame, text = 'Length:')
entry_W = tk.Entry(top_frame, background = "pink")
entry_L = tk.Entry(top_frame, background = "orange")

# layout the widgets in the top frame
model_label.grid(row = 0, columnspan = 3)
width_label.grid(row = 1, column = 0)
length_label.grid(row = 1, column = 2)
entry_W.grid(row = 1, column = 1)
entry_L.grid(row = 1, column = 3)

# create the center widgets
center.grid_rowconfigure(0, weight = 1)
center.grid_columnconfigure(1, weight = 1)

ctr_left = tk.Frame(center, bg = 'blue', width = 100, height = 190)
ctr_mid = tk.Frame(center, bg = 'yellow', width = 250, height = 190, padx = 3, pady = 3)
ctr_right = tk.Frame(center, bg = 'green', width = 100, height = 190, padx = 3, pady = 3)

ctr_left.grid(row = 0, column = 0, sticky = "ns")
ctr_mid.grid(row = 0, column = 1, sticky = "nsew")
ctr_right.grid(row = 0, column = 2, sticky = "ns")

window.mainloop()


