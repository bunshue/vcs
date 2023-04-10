import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

def popup():
    popupwindow = tk.Toplevel(window)
    popupwindow.title('Alert')
    popupwindow.geometry('200x200')
    alert = tk.Label(popupwindow, text='Is it right?')
    button1 = tk.Button(popupwindow, text = 'OK', command = popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()
    
button = tk.Button(window, text='Open', command = popup)
button.pack()
     

window.mainloop()

