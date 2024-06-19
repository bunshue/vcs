
import tkinter as tk


print("------------------------------------------------------------")  # 60個

print('綁定鍵盤滑鼠事件 Combobox')

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.tag_config(tk.SEL,font=f)
      
window = tk.Tk()
window.geometry("600x800")

# 建立工具列
toolbar = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
toolbar.pack(side=tk.TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = tk.IntVar()
size = tk.Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

text.focus_set()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                        # size family更新
    f=Font(size=sizeVar.get())                  # 取得新font size
    text.tag_config(tk.SEL,font=f)
      
window = tk.Tk()
window.geometry("600x800")

# 建立工具列
toolbar = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
toolbar.pack(side=tk.TOP,fill=tk.X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = tk.IntVar()
size = tk.Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\t李白\n","a")     # 插入時同時設定Tag

text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

text.focus_set()
# 將Tag a設為置中,藍色,含底線
text.tag_config("a",foreground="blue",justify=CENTER,underline=True)

window.mainloop()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
