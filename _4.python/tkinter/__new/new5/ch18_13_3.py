# ch18_13_3.py
from tkinter import *

window = Tk()
window.title("ch18_13_2")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=lambda:window.config(bg="blue"))
yellowbtn = Button(window,text="Yellow",command=lambda:window.config(bg="yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()




