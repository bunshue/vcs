import tkinter

def banmen():
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")

root = tkinter.Tk()
root.title("黑白棋")
root.resizable(False, False)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()
