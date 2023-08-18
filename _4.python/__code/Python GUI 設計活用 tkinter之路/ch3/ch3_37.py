# ch3_37.py
from tkinter import *

root = Tk()
root.title("ch3_37")
root.geometry("640x480")

night = PhotoImage(file="night.png")    # 影像night
lab1 = Label(root,image=night)
lab1.place(x=20,y=30,width=200,height=120)
snow = PhotoImage(file="snow.png")      # 影像snow
lab2 = Label(root,image=snow)
lab2.place(x=200,y=200,width=400,height=240)

root.mainloop()




