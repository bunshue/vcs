#右鍵選單

import tkinter as tk
        
def popup(event):
    menu.post(event.x_root, event.y_root)

def menu_function1():
    print('你按了 右鍵選單 第 1 項')

def menu_function2():
    print('你按了 右鍵選單 第 2 項')

def menu_function3():
    print('你按了 右鍵選單 第 3 項')

def menu_function4():
    print('你按了 右鍵選單 第 4 項')

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
title = "右鍵選單"
window.title(title)

#右鍵選單
menu = tk.Menu(window, tearoff = 0)
menu.add_command(label = "右鍵選單 第 1 項", command = menu_function1)
menu.add_command(label = "右鍵選單 第 2 項", command = menu_function2)
menu.add_command(label = "右鍵選單 第 3 項", command = menu_function3)
menu.add_command(label = "右鍵選單 第 4 項", command = menu_function4)

# Place canvas in window
canvas = tk.Canvas(window, width = 200, height = 100, bg = 'white')
canvas.pack()

# Bind popup to canvas
canvas.bind("<Button-3>", popup)

window.mainloop()



