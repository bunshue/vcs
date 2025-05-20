import tkinter

root = tkinter.Tk()
root.title("在畫布顯示字串")
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.create_text(300, 200, text="Python", font=("Times New Roman", 40))
cvs.pack()
root.mainloop()
