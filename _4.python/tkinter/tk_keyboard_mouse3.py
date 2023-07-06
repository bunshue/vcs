'''
綁定鍵盤滑鼠事件 Text
'''
import tkinter as tk

def get_pos(event):
	print(f'x: {event.x} y: {event.y}')

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

# widgets 
text = tk.Text(window)
text.pack()

# exercise : 
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

#window.bind('<Motion>', get_pos)       #顯示目前的滑鼠位置, 很多

window.mainloop()

