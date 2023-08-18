# ch17_4.py
from tkinter import *

root = Tk()
root.title("ch17_4")

yscrollbar = Scrollbar(root)                # y軸scrollbar物件
text = Text(root,height=5,width=30)         
yscrollbar.pack(side=RIGHT,fill=Y)          # y軸scrollbar包裝顯示
text.pack()
yscrollbar.config(command=text.yview)       # y軸scrollbar設定
text.config(yscrollcommand=yscrollbar.set)  # Text控件設定

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


