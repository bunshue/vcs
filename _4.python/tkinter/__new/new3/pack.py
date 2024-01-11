import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=20, text="台北景點")
taipei.pack(side="top")
kaohsiung=tk.Button(win, width=20, text="高雄景點")
kaohsiung.pack(side="top")

win.mainloop()
