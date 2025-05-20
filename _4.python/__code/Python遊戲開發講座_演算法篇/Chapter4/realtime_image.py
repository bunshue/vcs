import tkinter

x = 300
y = 100
xp = 10
def animation():
    global x, xp
    x = x + xp
    if x <= 30: xp = 5
    if x >= 770: xp = -5
    cvs.delete("all")
    cvs.create_image(400, 200, image=bg)
    if xp<0:
        cvs.create_image(x, y, image=ap1)
    if xp>0:
        cvs.create_image(x, y, image=ap2)
    root.after(50, animation)

root = tkinter.Tk()
root.title("即時處理２")
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()
ap1 = tkinter.PhotoImage(file="airplane1.png")
ap2 = tkinter.PhotoImage(file="airplane2.png")
bg = tkinter.PhotoImage(file="bg.png")
animation()
root.mainloop()
