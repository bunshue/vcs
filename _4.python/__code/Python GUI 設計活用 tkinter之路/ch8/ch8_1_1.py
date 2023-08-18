# ch8_1_1.py
from tkinter import *

root = Tk()
root.title("ch8_1")

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(bg=fm,height=50,width=250).pack()

root.mainloop()








