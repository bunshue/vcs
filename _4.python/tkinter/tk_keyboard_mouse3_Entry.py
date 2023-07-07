'''
綁定鍵盤滑鼠事件 Entry
'''
import tkinter as tk
from tkinter import ttk

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
title = '綁定鍵盤滑鼠事件 Entry'
window.title(title)

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('Entry FocusIn'))
entry.bind('<FocusOut>', lambda event: print('Entry FocusOut'))

window.mainloop()

