import tkinter

def masume():
    cvs.create_line(200, 0, 200, 600, fill="gray", width=8)
    cvs.create_line(400, 0, 400, 600, fill="gray", width=8)
    cvs.create_line(0, 200, 600, 200, fill="gray", width=8)
    cvs.create_line(0, 400, 600, 400, fill="gray", width=8)

root = tkinter.Tk()
root.title("井字遊戲")
root.resizable(False, False)
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()
