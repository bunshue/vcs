import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

import random

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = tk.Listbox(window, yscrollcommand = scrollbar.set )

for line in range(10):
   list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = list1.yview )


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個



import tkinter as tk

window = tk.Tk()

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

tkimage = tk.PhotoImage(file = filename)

canvas = tk.Canvas(window, width = 600, height = 600)
canvas.pack()
canvas.create_image(256, 256, image = tkimage)

window.mainloop()

print("------------------------------------------------------------")  # 60個


#只能用gif
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

import tkinter as tk
    
window = tk.Tk() # Create a root window

photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "blue").pack(fill = tk.BOTH, expand = 1)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
canvas = tk.Canvas(window,
			width = 600,					# 指定Canvas元件的寬度
			height = 480,					# 指定Canvas元件的高度
			bg = 'white')					# 指定Canvas元件的背景色

#只能開啟 gif 檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'
im = tk.PhotoImage(file=filename)				# 使用PhotoImage開啟圖片
canvas.create_image(300,250,image = im)					# 使用create_image將圖片新增到Canvas元件中

canvas.pack()								# 將Canvas新增到主視窗

window.mainloop()




print("------------------------------------------------------------")  # 60個



from tkinter import * # Import tkinter
    
window = Tk() # Create a window
window.title("Scroll Text Demo") # Set title

frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(frame1, width = 40, height = 10, wrap = WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

window.mainloop() # Create an event loop


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





