# ch2_22.py
from tkinter import *

root = Tk()
root.title("ch2_22")
sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="center")
label.pack()

root.mainloop()




