# Filename: ex09_04.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ptext = tk.Text(win)
ptext.insert(tk.INSERT, "床前明月光\n")
ptext.insert(tk.INSERT, "疑是地上霜\n")
ptext.insert(tk.INSERT, "舉頭望明月\n")
ptext.insert(tk.INSERT, "低頭思故鄉\n")
ptext.pack()
ptext.config(state=tk.DISABLED)
win.mainloop()