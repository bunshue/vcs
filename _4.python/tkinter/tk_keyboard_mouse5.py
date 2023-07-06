'''
綁定鍵盤滑鼠事件 Entry Text
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
title = "這是主視窗"
window.title(title)
#window.title('Event Binding')

def get_pos(event):
	print(f'x: {event.x} y: {event.y}')

# widgets 
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

#window.bind('<Motion>', get_pos)       #顯示目前的滑鼠位置, 很多

entry.bind('<FocusIn>', lambda event: print('Entry FocusIn'))
entry.bind('<FocusOut>', lambda event: print('Entry FocusOut'))

# exercise : 
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

window.mainloop()

