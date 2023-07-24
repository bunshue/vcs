import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
menu1 = tk.Menu(menu, tearoff = False)
menu1.add_command(label = 'New', command = lambda: print('New file'))
menu1.add_command(label = 'Open', command = lambda: print('Open file'))
menu1.add_separator()
menu.add_cascade(label = 'File', menu = menu1)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = False)
menu2.add_command(label = 'Help entry', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
menu2.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = menu2)

#第3排功能選單
# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
menu3 = tk.Menu(menu, tearoff = False)
menu3.add_command(label = 'exercise test 1')
menu.add_cascade(label = 'Exercise', menu = menu3)

menu3b = tk.Menu(menu, tearoff = False)
menu3b.add_command(label = 'some more stuff')
menu3.add_cascade(label = 'more stuff', menu = menu3b)

# menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
# menu_button.configure(menu = button_sub_menu)
menu_button['menu']= button_sub_menu

window.mainloop()

