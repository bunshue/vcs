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

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('用Frame做一個toolbar')
frame_toolbar = tk.Frame(window, relief = "raised", borderwidth = 1)
frame_toolbar.pack(side = "top", fill = "x", padx = 2, pady = 1)

button1 = tk.Button(frame_toolbar, text = "Function 1")
button1.pack(side = "left", pady = 2)
button2 = tk.Button(frame_toolbar, text = "Function 2")
button2.pack(side = "left", pady = 2)
button3 = tk.Button(frame_toolbar, text = "Function 3")
button3.pack(side = "left", pady = 2)
button4 = tk.Button(frame_toolbar, text = "Function 4")
button4.pack(side = "left", pady = 2)
button5 = tk.Button(frame_toolbar, text = "Function 5")
button5.pack(side = "left", pady = 2)
button6 = tk.Button(frame_toolbar, text = "Function 6")
button6.pack(side = "left", pady = 2)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

'''
width:設置框架寬度，默認值是 0。
height:框架的高度，默認值是 0。
bg:框架背景顏色
bd:框架的大小，默認為 2 個像素
relief:邊框樣式，可選的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默認為 FLAT。
cursor:鼠標移動到框架時，光標的形狀，可以設置為 arrow, circle, cross, plus 等。
highlightbackground:框架沒有獲得焦點時，高亮邊框的顏色，默認由系統指定。
highlightcolor:框架獲得焦點時，高亮邊框的顏色
highlightthickness:指定高亮邊框的寬度，默認值為 0不帶高亮邊框）
takefocus:指定該組件是否接受輸入焦點（用戶可以通過 tab 鍵將焦點轉移上來），默認為 false。

'''

separator = tk.Frame(width = 30, height = 80, bg = 'pink', bd = 5, relief = tk.GROOVE).pack(fill = tk.X, padx = 5, pady = 5)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

