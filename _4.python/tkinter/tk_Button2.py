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

#使用side
button1 = tk.Button(window, text = "按鈕 視窗最右邊", width = 20)
button1.pack(padx = 20, pady = 5, side = "right")
button2 = tk.Button(window, text = "按鈕 視窗最左邊", width = 20)
button2.pack(padx = 20, pady = 5, side = "left")
button3 = tk.Button(window, text = "按鈕 視窗最下邊", width = 20)
button3.pack(padx = 20, pady = 5, side = "bottom")
button4 = tk.Button(window, text = "按鈕 視窗最上邊", width = 20)
button4.pack(padx = 20, pady = 5)

#使用anchor
button1 = tk.Button(window, text = "按鈕 視窗正中央", width = 20)
button1.place(relx = 0.5, rely = 0.5, anchor = "center")
button2 = tk.Button(window, text = "按鈕 視窗左上", width = 20)
button2.place(relx = 0.1, rely = 0.1, anchor = "nw")
button3 = tk.Button(window, text = "按鈕 視窗左下", width = 20)
button3.place(relx = 0.1, rely = 0.8, anchor = "w") #???

#使用pad
button1 = tk.Button(window, text = "這是按鈕一b 有 pad", width = 20)
button1.pack(padx = 20, pady = 5)
button2 = tk.Button(window, text = "這是按鈕二b 有 pad", width = 20)
button2.pack(padx = 20, pady = 5)
button3 = tk.Button(window, text = "這是按鈕三b 有 pad", width = 20)
button3.pack(padx = 20, pady = 5)
button4 = tk.Button(window, text = "這是按鈕四b 有 pad", width = 20)
button4.pack(padx = 20, pady = 5)

#直接pack, 無參數
button1 = tk.Button(window, text = "這是按鈕一c 無 pad", width = 20)
button1.pack()
button2 = tk.Button(window, text = "這是按鈕二c 無 pad", width = 20)
button2.pack()
button3 = tk.Button(window, text = "這是按鈕三c 無 pad", width = 20)
button3.pack()
button4 = tk.Button(window, text = "這是按鈕四c 無 pad", width = 20)
button4.pack()

#使用place
x_st = 600
y_st = 50
dx = 120;
dy = 80;
w = 12
h = 3

button0 = tk.Button(window, text = "用place 0", width = w, height = h, command = '')
button0.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button1 = tk.Button(window, text = "用place 1", width = w, height = h, command = '')
button1.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button2 = tk.Button(window, text = "用place 2", width = w, height = h, command = '')
button2.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button3 = tk.Button(window, text = "用place 3", width = w, height = h, command = '')
button3.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

button0.place(x = x_st + dx * 0, y = y_st + dy * 0)
button1.place(x = x_st + dx * 0, y = y_st + dy * 1)
button2.place(x = x_st + dx * 0, y = y_st + dy * 2)
button3.place(x = x_st + dx * 0, y = y_st + dy * 3)

window.mainloop()


