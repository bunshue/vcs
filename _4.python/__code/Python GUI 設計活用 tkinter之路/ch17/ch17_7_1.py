# ch17_7_1.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
      
root = Tk()
root.title("ch17_7_1")
root.geometry("300x180")

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(root,familyVar,*familyFamily,command=familyChanged)
family.pack(pady=2)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()


