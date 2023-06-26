import tkinter as tk

def buttonClick():
    global count
    count = count + 1
    print("Beep! " + str(count))
    button1.config(text = "Clicked " + str(count))

def buttonExit():
    print('離開, 看似無效')
    window.quit();

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

count = 0;

button5 = tk.Button(window, text = '指定按鍵大小', width = 20, height = 5)
button5.pack()  #pack無參數, 控件置中

button1 = tk.Button(window, text = "按鍵數次數, 不指定按鍵大小", command = buttonClick)
button1.pack(side = tk.LEFT)    #靠左對齊

button2 = tk.Button(window, text = "離開", command = buttonExit)
button2.pack(side = tk.RIGHT)   #靠右對齊

#side=tk.RIGHT


'''
btn0 = tk.Button(window, text = 'btn(0, 0)')
btn1 = tk.Button(window, text = 'btn(1, 0)')
btn2 = tk.Button(window, text = 'btn(0, 1)')
btn3 = tk.Button(window, text = 'btn(1, 1)')

btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 1, column = 0)
btn3.grid(row = 1, column = 1)
'''

button1 = tk.Button(window, text = '位置(0, 0)', width = 10, height = 2)
button2 = tk.Button(window, text = '位置(50, 50)', width = 10, height = 2)
button3 = tk.Button(window, text = '位置(100, 100)', width = 10, height = 2)

button1.place(x = 0, y = 0)
button2.place(x = 50, y = 50)
button3.place(x = 100, y = 100)


print("建立toolbar");

def callback():
    print("called the callback!")

# create a toolbar
toolbar = tk.Frame(window)

b = tk.Button(toolbar, text = "new", width = 6, command = callback)
b.pack(side = tk.LEFT, padx = 2, pady = 2)

b = tk.Button(toolbar, text = "open", width = 6, command = callback)
b.pack(side = tk.LEFT, padx = 2, pady = 2)

toolbar.pack(side = tk.TOP, fill = tk.X)


window.mainloop()

#window.destroy()    # 使用quit()離開上面的mainloop
