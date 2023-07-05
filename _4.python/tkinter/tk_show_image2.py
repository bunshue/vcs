import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = 'Display Image'
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival.gif'

photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "gray").pack(fill = tk.BOTH, expand = 1)

window.mainloop()
