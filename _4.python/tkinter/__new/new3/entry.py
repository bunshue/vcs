import tkinter as tk
win = tk.Tk()
win.title("密碼資料")
win.geometry('300x200')

label = tk.Label(win, text = "請輸入密碼: ")
label.pack()
entry = tk.Entry(win,bg='yellow',fg='red',show='*')
entry.pack()

win.mainloop()
