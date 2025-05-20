import tkinter

FNT = ("Times New Roman", 40)


def move(e):
    cvs.delete("all")
    s = "({}, {})".format(e.x, e.y)
    cvs.create_text(300, 200, text=s, font=FNT)


root = tkinter.Tk()
root.title("滑鼠游標的座標")
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=600, height=400)
cvs.create_text(300, 200, text="請在視窗之內移動滑鼠游標")
cvs.pack()
root.mainloop()
