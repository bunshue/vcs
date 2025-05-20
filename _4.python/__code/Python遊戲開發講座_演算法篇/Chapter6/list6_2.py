import tkinter

img = [None]*14
card = [0]*26

def draw_card():
    for i in range(26):
        x = (i%7)*120+60
        y = int(i/7)*168+84
        cvs.create_image(x, y, image=img[card[i]])

def shuffle_card():
    for i in range(26):
        card[i] = 1+i%13

root = tkinter.Tk()
root.title("翻牌配對遊戲")
root.resizable(False, False)
cvs = tkinter.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    img[i] = tkinter.PhotoImage(file="card/"+str(i)+".png")
shuffle_card()
draw_card()
root.mainloop()
