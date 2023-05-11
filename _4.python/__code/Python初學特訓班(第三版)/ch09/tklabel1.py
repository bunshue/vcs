import tkinter as tk
win = tk.Tk()
label1 = tk.Label(win, text="這是標籤元件！", fg="red", bg="yellow", font=("新細明體", 12), padx=20, pady=10)
label1.pack()
win.mainloop()