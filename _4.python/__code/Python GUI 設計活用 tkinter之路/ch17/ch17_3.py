# ch17_3.py
from tkinter import *

root = Tk()
root.title("ch17_3")

text = Text(root,height=3,width=30)
text.pack()
str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()


