"""
import tkinter as tk

print("------------------------------------------------------------")  # 60個


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "Scrollbar 測試"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

frame1 = tk.Frame(window)
frame1.pack()
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text = tk.Text(frame1, width = 40, height = 10, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()
print("------------------------------------------------------------")  # 60個


"""


from tkinter import *

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

scrollbar = tk.Scrollbar(window)  # 卷軸物件
text = tk.Text(window, height=2, width=30)  # 文字區域物件
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # 靠右安置與父物件高度相同
text.pack(side=tk.LEFT, fill=tk.Y)  # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(tk.END, "我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(tk.END, str)

window.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

scrollbar = Scrollbar(root)  # 建立捲軸
scrollbar.pack(side=RIGHT, fill=Y)

# 建立Listbox, yscrollcommand指向scrollbar.set方法
lb = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(50):  # 建立50筆項目
    lb.insert(END, "Line " + str(i))
lb.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=lb.yview)

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

yscrollbar = Scrollbar(root)  # y軸scrollbar物件
text = Text(root, height=5, width=30)
yscrollbar.pack(side=RIGHT, fill=Y)  # y軸scrollbar包裝顯示
text.pack()
yscrollbar.config(command=text.yview)  # y軸scrollbar設定
text.config(yscrollcommand=yscrollbar.set)  # Text控件設定

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END, str)

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

xscrollbar = Scrollbar(root, orient=HORIZONTAL)  # x軸scrollbar物件
yscrollbar = Scrollbar(root)  # y軸scrollbar物件
text = Text(root, height=5, width=30, wrap="none")
xscrollbar.pack(side=BOTTOM, fill=X)  # x軸scrollbar包裝顯示
yscrollbar.pack(side=RIGHT, fill=Y)  # y軸scrollbar包裝顯示
text.pack()
xscrollbar.config(command=text.xview)  # x軸scrollbar設定
yscrollbar.config(command=text.yview)  # y軸scrollbar設定
text.config(xscrollcommand=xscrollbar.set)  # x軸scrollbar綁定text
text.config(yscrollcommand=yscrollbar.set)  # y軸scrollbar綁定text

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END, str)

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

xscrollbar = Scrollbar(root, orient=HORIZONTAL)  # x軸scrollbar物件
yscrollbar = Scrollbar(root)  # y軸scrollbar物件
text = Text(root, height=5, width=30, wrap="none", bg="lightyellow")
xscrollbar.pack(side=BOTTOM, fill=X)  # x軸scrollbar包裝顯示
yscrollbar.pack(side=RIGHT, fill=Y)  # y軸scrollbar包裝顯示
text.pack(fill=BOTH, expand=True)
xscrollbar.config(command=text.xview)  # x軸scrollbar設定
yscrollbar.config(command=text.yview)  # y軸scrollbar設定
text.config(xscrollcommand=xscrollbar.set)  # x軸scrollbar綁定text
text.config(yscrollcommand=yscrollbar.set)  # y軸scrollbar綁定text

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END, str)

root.mainloop()


print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.title("Scroll Text Demo")

frame1 = tk.Frame(window)
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text1 = tk.Text(frame1, width=40, height=10, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text1.pack()

scrollbar.config(command=text1.yview)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

wordlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list1 = tk.Listbox(window, yscrollcommand=scrollbar.set)

for line in range(10):
    list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=list1.yview)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("ScrollBar捲軸")

text = tk.Text(window, width="30", height="5")
text.pack()

scrollbar = tk.Scrollbar(command=text.yview, orient=tk.VERTICAL)
scrollbar.pack()

text.configure(yscrollcommand=scrollbar.set)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個




