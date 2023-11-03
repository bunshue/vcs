from tkinter import *

Window = Tk()
scrollbar = Scrollbar(Window)
scrollbar.pack( side = RIGHT, fill = Y )

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = Listbox(Window, yscrollcommand = scrollbar.set )

for line in range(26):
   list1.insert(END, "字母: " + wordlist[line])

list1.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = list1.yview )

mainloop()
