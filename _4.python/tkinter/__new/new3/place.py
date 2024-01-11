import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=30, text="台北景點")
taipei.place(x=10, y=10)
kaohsiung=tk.Button(win, width=30, text="高雄景點")
kaohsiung.place(relx=0.5, rely=0.5, anchor="center")

win.mainloop()
