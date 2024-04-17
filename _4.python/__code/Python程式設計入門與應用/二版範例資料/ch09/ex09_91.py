import tkinter as tk
import tkinter.messagebox as tkmessagebox
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")

tkmessagebox.askokcancel(title="對話方塊", message="askokcancel")

win.mainloop()
