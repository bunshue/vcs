import tkinter

COL = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet"]
bc = 0
bx = 0
by = 0
mx = 0
my = 0

def click(e):
    global bc
    bc = bc + 1
    if bc==7: bc=0

def move(e):
    global mx, my
    mx = e.x
    my = e.y

def main():
    global bx, by
    if bx < mx: bx += 5
    if mx < bx: bx -= 5
    if by < my: by += 5
    if my < by: by -= 5
    cvs.delete("all")
    cvs.create_oval(bx-40, by-60, bx+40, by+60, fill=COL[bc])
    cvs.create_oval(bx-30, by-45, bx-5, by-20, fill="white", width=0)
    cvs.create_line(bx, by+60, bx-10, by+100, bx+10, by+140, bx, by+180, smooth=True)
    root.after(50, main)

root = tkinter.Tk()
root.title("即時讓氣球移動")
root.bind("<Button>", click)
root.bind("<Motion>", move)
cvs = tkinter.Canvas(width=900, height=600, bg="skyblue")
cvs.pack()
main()
root.mainloop()
