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

def buttonClick():
    print('click')

print('用Frame做一個toolbar 1')
frame_toolbar1 = tk.Frame(window, relief = "raised", borderwidth = 1)
frame_toolbar1.pack(side = "top", fill = "x", padx = 2, pady = 1)

button1 = tk.Button(frame_toolbar1, text = "Function 1", command = buttonClick)
button1.pack(side = "left", pady = 2)
button2 = tk.Button(frame_toolbar1, text = "Function 2", command = buttonClick)
button2.pack(side = "left", pady = 2)
button3 = tk.Button(frame_toolbar1, text = "Function 3", command = buttonClick)
button3.pack(side = "left", pady = 2)
button4 = tk.Button(frame_toolbar1, text = "Function 4", command = buttonClick)
button4.pack(side = "left", pady = 2)
button5 = tk.Button(frame_toolbar1, text = "Function 5", command = buttonClick)
button5.pack(side = "left", pady = 2)
button6 = tk.Button(frame_toolbar1, text = "Function 6", command = buttonClick)
button6.pack(side = "left", pady = 2)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('用Frame做一個toolbar 2')
frame_toolbar2 = tk.Frame(window)
frame_toolbar2.pack(side = tk.TOP, fill = tk.X)

button1 = tk.Button(frame_toolbar2, text = "new", width = 6, command = buttonClick)
button1.pack(side = tk.LEFT, padx = 2, pady = 2)
button2 = tk.Button(frame_toolbar2, text = "open", width = 6, command = buttonClick)
button2.pack(side = tk.LEFT, padx = 2, pady = 2)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


print('將多個控件做在一個Frame上')

frame2 = tk.Frame(window, bg = 'yellow')  # 按鈕容器
frame2.pack()    
button1 = tk.Button(frame2, text = "播放", width = 8,command = '')
button1.grid(row = 0, column = 0, padx = 5, pady = 5)
button2 = tk.Button(frame2, text = "暫停", width = 8,command = '')
button2.grid(row = 0, column = 1, padx = 5, pady = 5)
button3 = tk.Button(frame2, text = "音量調大", width = 8,command = '')
button3.grid(row = 0, column = 2, padx = 5, pady = 5)
button4 = tk.Button(frame2, text = "音量調小", width = 8,command = '')
button4.grid(row = 0, column = 3, padx = 5, pady = 5)
button5 = tk.Button(frame2, text = "停止", width = 8,command = '')
button5.grid(row = 0, column = 4, padx = 5, pady = 5)
button6 = tk.Button(frame2, text = "結束", width = 8,command = '')
button6.grid(row = 0, column = 5, padx = 5, pady = 5)

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

width = 100
height = 100
frame = tk.Frame(window, bg = 'pink', width = width, height = height)
frame.pack()
frame = tk.Frame(window, bg = 'yellow', width = width, height = height)
frame.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

