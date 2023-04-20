'''
import tkinter as tk
from tkinter import *

global root
root = Tk()
root.geometry('580x140')## Set window size#500
root.title("My first GUI")



root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
rectangle_1 = tk.Label(root, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0, ipadx=10, ipady=10)
rectangle_2 = tk.Label(root, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1, ipadx=10, ipady=10)


root.mainloop()



#window.mainloop()
'''



import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

rectangle_1 = tk.Label(root, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0,row=0, ipadx=10, ipady=10)

rectangle_2 = tk.Label(root, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1,row=0, ipadx=10, ipady=10)

root.mainloop()




