import tkinter
import random

pi = 0
rp = 0
cp = 0
def main():
    global pi, rp, cp
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    rp += 1
    col = "red"
    if (x-200)*(x-200)+(y-200)*(y-200) <= 200*200:
        cp += 1
        col = "blue"
    ca.create_rectangle(x, y, x+1, y+1, fill=col, width=0)
    ca.update()
    pi = 4*cp/rp
    root.title("圓周率 "+str(pi))
    if rp < 10000:
        root.after(1, main)

root = tkinter.Tk()
ca = tkinter.Canvas(width=400, height=400, bg="black")
ca.pack()
main()
root.mainloop()
