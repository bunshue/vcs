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

def popup():
    popupwindow = tk.Toplevel(window)
    popupwindow.title('新視窗')
    popupwindow.geometry('300x300')
    alert = tk.Label(popupwindow, text='已開啟新視窗')
    button1 = tk.Button(popupwindow, text = '離開此視窗', command = popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()
    
button = tk.Button(window, text='開啟新視窗', command = popup)
button.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線

window.mainloop()

#window.destroy()



