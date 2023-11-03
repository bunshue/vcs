# ch18_22.py
from tkinter import *
          
window = Tk()
window.title("ch18_22")             # 視窗標題

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)
text.pack()

window.mainloop()






