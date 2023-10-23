from tkinter import *
from tkinter import messagebox

def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        messagebox.showinfo("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        messagebox.showinfo("deer的簡介",str2)
    
win = Tk()
lb=Label(win,text="請點選想了解的動物簡介:").pack()
choice=IntVar()
choice.set(0)
pic1=PhotoImage(file="cattle.gif")
pic2=PhotoImage(file="deer.gif")
Radiobutton(win,image=pic1,variable=choice,value=0).pack()
Radiobutton(win,image=pic2,variable=choice,value=1).pack()
Button(win,text="進一步了解", command=more).pack()

win.mainloop()
