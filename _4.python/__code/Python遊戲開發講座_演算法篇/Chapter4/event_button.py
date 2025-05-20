import tkinter

n = 0
def click(e):
    global n
    n = n + 1
    if n==3: n = 0
    cvs.delete("all")
    if n==0:
        cvs.create_oval(200, 100, 400, 300, fill="green")
    if n==1:
        cvs.create_rectangle(200, 100, 400, 300, fill="gold")
    if n==2:
        cvs.create_polygon(300, 100, 200, 300, 400, 300, fill="red")

root = tkinter.Tk()
root.title("取得滑鼠點擊事件")
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.create_text(300, 200, text="請點選視窗內部任何一個位置")
cvs.pack()
root.mainloop()
