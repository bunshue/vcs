import tkinter as tk
win = tk.Tk()
text=tk.Text(win)
text.insert(tk.INSERT, "從入門到精通\n")
text.insert(tk.CURRENT, "Illustrator CC\n")
text.insert(tk.END, "玩轉 Ai 設計風華的16堂課")
text.pack()
text.config(state=tk.DISABLED)
win.mainloop()
