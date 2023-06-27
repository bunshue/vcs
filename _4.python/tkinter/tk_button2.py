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

button1 = tk.Button(window, text = "這是按鈕一a 右", width = 20)
button1.pack(padx=20, pady=5, side="right")
button2 = tk.Button(window, text = "這是按鈕二a 左", width = 20)
button2.pack(padx=20, pady=5, side="left")
button3 = tk.Button(window, text = "這是按鈕三a 下", width = 20)
button3.pack(padx=20, pady=5, side="bottom")
button4 = tk.Button(window, text = "這是按鈕四a 上", width = 20)
button4.pack(padx=20, pady=5)

button1 = tk.Button(window, text = "這是按鈕一b", width = 20)
button1.pack(padx=20, pady=5)
button2 = tk.Button(window, text = "這是按鈕二b", width = 20)
button2.pack(padx=20, pady=5)
button3 = tk.Button(window, text = "這是按鈕三b", width = 20)
button3.pack(padx=20, pady=5)
button4 = tk.Button(window, text = "這是按鈕四b", width = 20)
button4.pack(padx=20, pady=5)

button1 = tk.Button(window, text = "這是按鈕一c", width = 20)
button1.pack()
button2 = tk.Button(window, text = "這是按鈕二c", width = 20)
button2.pack()
button3 = tk.Button(window, text = "這是按鈕三c", width = 20)
button3.pack()
button4 = tk.Button(window, text = "這是按鈕四c", width = 20)
button4.pack()

window.mainloop()


