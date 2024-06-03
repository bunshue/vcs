import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Spin 測試"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.1)
spinbox.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#w = ttk.Spinbox(window, from_=0, to=10)
w = ttk.Spinbox(window, values=(1, 2, 4, 8))
w.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
	window, 
	from_ = 3, 
	to = 20, 
	increment = 3, 
	command = lambda: print(spin_int.get()),
	textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5)
spin.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# create a spinbox that contains the letters A B C D E 
# and print the value whenever the value is decreased

exercise_letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin = ttk.Spinbox(window, textvariable = exercise_string, values = exercise_letters)
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)    

print("試題與測驗分析程式")

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox = tk.Spinbox(window, from_=1, to=12, textvariable=month, command=spinbox_select, font=default_font)
spinbox.pack(padx=10, pady=10)
lab_result = tk.Label(window, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

