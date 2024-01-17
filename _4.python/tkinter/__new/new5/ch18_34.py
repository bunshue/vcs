# ch18_34.py
from tkinter import *
    
window = Tk()
window.title("ch18_34")             # 視窗標題

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL).pack()

window.mainloop()






