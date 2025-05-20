import tkinter

BLACK = 1
WHITE = 2
board = [
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 1, 0, 0, 0],
 [0, 0, 0, 1, 2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
]

def click(e):
    mx = int(e.x/80)
    my = int(e.y/80)
    if mx>7: mx = 7
    if my>7: my = 7
    if board[my][mx]==0:
        board[my][mx] = BLACK
    elif board[my][mx]==BLACK:
        board[my][mx] = WHITE
    elif board[my][mx]==WHITE:
        board[my][mx] = 0
    banmen()

def banmen():
    cvs.delete("all")
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")
            if board[y][x]==BLACK:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
            if board[y][x]==WHITE:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)

root = tkinter.Tk()
root.title("黑白棋")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()
