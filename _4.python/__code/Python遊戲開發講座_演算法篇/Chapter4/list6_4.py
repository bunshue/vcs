import tkinter
import random

img = [None] * 14
card = [0] * 26
face = [0] * 26


def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 7) * 120 + 60
        y = int(i / 7) * 168 + 84
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        if face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])


def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]


def click(e):
    x = int(e.x / 120)
    y = int(e.y / 168)
    if 0 <= x and x <= 6 and 0 <= y and y <= 3:
        n = x + y * 7
        if n >= 26:
            return
        if face[n] == 0:
            face[n] = 1
        else:
            face[n] = 0
        draw_card()


root = tkinter.Tk()
root.title("翻牌配對遊戲")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    img[i] = tkinter.PhotoImage(file="card/" + str(i) + ".png")
shuffle_card()
draw_card()
root.mainloop()
