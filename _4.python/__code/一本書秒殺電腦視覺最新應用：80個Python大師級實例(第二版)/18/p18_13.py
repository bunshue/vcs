from tkinter import *
root = Tk()
text1 = Text(root,width=100,height=30)
text1.pack()
photo = PhotoImage(file='bg1.gif')
def show():
     #添加图片用image_create
     text1.image_create(END,image=photo)
b1 = Button(text1,text='点我点我',command=show)
     #添加插件用window_create
text1.window_create(INSERT,window=b1)
mainloop()
