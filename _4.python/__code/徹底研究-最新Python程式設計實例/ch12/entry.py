import tkinter as tk

win = tk.Tk()
win.title("GUI介面-entry")

entry = tk.Entry(win, bg="#ffff00", font = "新細明體 16 bold" ,borderwidth = 3)
entry.insert(0,"天天")
entry.insert("2","青春永駐")
entry.insert("end"," 莫忘初心")
entry.delete(0, 2)  #刪除前面兩個字元
entry.pack(padx=20, pady=10)

win.mainloop()
