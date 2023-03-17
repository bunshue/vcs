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


'''

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

window = Tk()

#w = Spinbox(window, from_=0, to=10)
w = Spinbox(window, values=(1, 2, 4, 8))
w.pack()

'''



scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
for i in range(10):
    listbox.insert(tk.END, str(i))
    
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)



#w = tk.Scale(window, from_=0, to=100)
w = tk.Scale(window, from_=0, to=100, resolution=0.1)
w.pack()

w = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

print(w.get())


window.mainloop()

