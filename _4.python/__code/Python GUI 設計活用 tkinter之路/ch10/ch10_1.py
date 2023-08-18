# ch10_1.py
from tkinter import *

root = Tk()
root.title("ch10_1")

myText = "2016年12月,我一個人訂了機票和船票,開始我的南極旅行"
msg = Message(root,bg="yellow",text=myText,
              font="times 12 italic")
msg.pack(padx=10,pady=10)

root.mainloop()








