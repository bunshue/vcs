'''
LabelFrame 就是 Groupbox.py

'''

import tkinter as tk

# 建立主視窗
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
title = "Groupbox測試"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# GroupBox測試
tk.Label(text = 'GroupBox測試').pack()

#GroupBox之大小, 若小於內附控件大小, 則會撐大
w = 10
h = 10
group = tk.LabelFrame(window, text = "Group", padx = w, pady = h)

#GroupBox之位置, 相較於目前表單位置
x_st = 0
y_st = 0
group.pack(padx = x_st, pady = y_st)

#GroupBox內 放幾個控件
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()
