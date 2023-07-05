import tkinter as tk
import random

# Choose four random cards
def shuffle():
    random.shuffle(imageList)
    for i in range(4):
        labelList[i]["image"] = imageList[i]
        

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = 'Pick Four Cards Randomly'
window.title(title)

imageList = [] # Store images for cards
for i in range(1, 53):
    imageList.append(tk.PhotoImage(file = "C:/_git/vcs/_1.data/______test_files1/__pic/_poker_card/card/" + str(i) + ".gif"))

frame = tk.Frame(window) # Hold four labels for cards
frame.pack()

labelList = [] # A list of four labels
for i in range(4):
    labelList.append(tk.Label(frame, image = imageList[i]))
    labelList[i].pack(side = tk.LEFT)

tk.Button(window, text = "Shuffle", command = shuffle).pack()

window.mainloop()


