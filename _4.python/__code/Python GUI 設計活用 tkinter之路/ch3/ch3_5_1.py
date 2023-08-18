# ch3_5_1.py
from tkinter import *

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

root = Tk()
root.title("ch3_5_1")

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()




