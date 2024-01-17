# ch18_23.py
from tkinter import *
          
window = Tk()
window.title("ch18_23")                 # 視窗標題
scrollbar = Scrollbar(window)           # 卷軸物件
text = Text(window,height=2,width=30)   # 文字區域物件
scrollbar.pack(side=RIGHT,fill=Y)       # 靠右安置與父物件高度相同
text.pack(side=LEFT,fill=Y)             # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)

window.mainloop()






