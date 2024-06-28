import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

"""
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")

# 單選按鈕
# 定義幾個顏色的全局變量
colors = ["Blue", "Gold", "Red"]


# 單選按鈕回調函數,就是當單選按鈕被點擊會執行該函數
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        window.configure(background=colors[0])  # 設置整個界面的背景顏色
        print(radVar.get())
    elif radSel == 1:
        window.configure(background=colors[1])
    elif radSel == 2:
        window.configure(background=colors[2])


radVar = tk.IntVar()  # 通過tk.IntVar(),獲取單選按鈕value參數對應的值
radVar.set(99)
for col in range(3):
    # 當該單選按鈕被點擊時，會觸發參數command對應的函數
    curRad = tk.Radiobutton(
        window, text=colors[col], variable=radVar, value=col, command=radCall
    )
    curRad.pack()

window.mainloop()
"""
print("------------------------------------------------------------")  # 60個

from tkinter import scrolledtext  # 導入滾動文本框的模塊

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")

# 滾動文本框
scrolW = 30  # 設置文本框的長度
scrolH = 3  # 設置文本框的高度
# wrap=tk.WORD這個值表示在行的末尾如果有一個單詞跨行，會將該單詞放到下一行顯示
scr = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


window.mainloop()

print("------------------------------------------------------------")  # 60個
