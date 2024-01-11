from tkinter import *
sentences="玉階生白露，夜久侵羅襪。\n卻下水晶簾，玲瓏望秋月。"
win = Tk()
win.title("Text多行文字")
win.geometry('300x200')
text = Text(win, width = 30, height = 14, bg = "yellow", wrap=WORD)
text.insert(END,sentences)
text.pack()
win.mainloop()
