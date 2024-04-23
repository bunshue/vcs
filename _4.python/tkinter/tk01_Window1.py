import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('More on the window')

# exercise:
# start window in the middle of the screen 
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

print("螢幕解析度 : " + str(display_width) + "*" + str(display_height))

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

'''
window_width = 200
window_height = 200
left = 100
top = 100
window.geometry(f'{window_width}x{window_height}+{left}+{top}')
'''

# window sizes 
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True,False)

print('設定視窗透明度')
window.attributes('-alpha', 0.9) #虛化，值越小虛化程度越高

print('設定視窗最上層顯示')
window.attributes('-topmost', True)

#window.attributes('-disable', True)

#print('設定視窗全螢幕')
#window.attributes('-fullscreen', True)

# security event 
window.bind('<Escape>', lambda event: window.quit())

# title bar 
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

window.mainloop()
