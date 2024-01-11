import tkinter as tk
win = tk.Tk()
win.geometry("400x100")
win.title("pack版面佈局")

taipei=tk.Button(win, width=30, text="台北景點")
taipei.grid(column=0,row=0)
kaohsiung=tk.Button(win, width=30, text="高雄景點")
kaohsiung.grid(column=0,row=1)
ilan=tk.Button(win, width=30, text="宜蘭景點")
ilan.grid(column=1,row=0)
tainan=tk.Button(win, width=30, text="台南景點")
tainan.grid(column=1,row=1)
	
win.mainloop()
