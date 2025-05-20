import tkinter
root = tkinter.Tk()
root.title("指定顏色的英文單字")
cvs = tkinter.Canvas(width=360, height=480, bg="black")

COL = [
 "maroon", "brown", "red", "orange", "gold", 
 "yellow", "lime", "limegreen", "green", "skyblue",
 "cyan", "blue", "navy", "indigo", "purple",
 "magenta", "white", "lightgray", "silver", "gray",
 "olive", "pink"
]
FNT = ("Times, New Roman", 24);
x = 120
y = 40
for c in COL:
    cvs.create_text(x, y, text=c, fill=c, font=FNT)
    y += 40
    if y>=480:
        y = 40
        x += 120

cvs.pack()
root.mainloop()
