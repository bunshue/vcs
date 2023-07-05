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

button1 = tk.Button(window, text="按鈕視窗最右邊", width=20)
button1.pack(padx=20, pady=5, side="right")
button2 = tk.Button(window, text="按鈕視窗最左邊", width=20)
button2.pack(padx=20, pady=5, side="left")
button3 = tk.Button(window, text="按鈕視窗最下邊", width=20)
button3.pack(padx=20, pady=5, side="bottom")
button4 = tk.Button(window, text="按鈕視窗最上邊", width=20)
button4.pack(padx=20, pady=5)

button1 = tk.Button(window, text="按鈕一排一個A", width=20)
button1.pack(padx=20, pady=5)
button2 = tk.Button(window, text="按鈕一排一個B", width=20)
button2.pack(padx=20, pady=5)
button3 = tk.Button(window, text="按鈕一排一個C", width=20)
button3.pack(padx=20, pady=5)
button4 = tk.Button(window, text="按鈕一排一個D", width=20)
button4.pack(padx=20, pady=5)

button1 = tk.Button(window, text="這是按鈕正中央", width=20)
button1.place(relx=0.5, rely=0.5, anchor="center")
button2 = tk.Button(window, text="這是按鈕左上", width=20)
button2.place(relx=0.1, rely=0.1, anchor="nw")
button3 = tk.Button(window, text="這是按鈕左下", width=20)
button3.place(relx=0.1, rely=0.8, anchor="w")

window.mainloop()
