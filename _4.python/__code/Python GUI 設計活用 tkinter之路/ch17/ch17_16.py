# ch17_16.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.tag_config(SEL,font=f)
      
root = Tk()
root.title("ch17_16")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()

root.mainloop()


