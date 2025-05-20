import tkinter
root = tkinter.Tk()
root.title("在畫布顯示圖片")
cvs = tkinter.Canvas(width=540, height=720)
dog = tkinter.PhotoImage(file="shepherd.png")
cvs.create_image(270, 360, image=dog)
cvs.pack()
root.mainloop()
