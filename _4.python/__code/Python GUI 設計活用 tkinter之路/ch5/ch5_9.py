# ch5_9.py
from tkinter import *
def cal():                          # 執行數學式計算
    out.configure(text = "結果 : " + str(eval(equ.get())))
    
root = Tk()
root.title("ch5_9")
label = Label(root, text="請輸入數學表達式:")
label.pack()
equ = Entry(root)                   # 在此輸入表達式
equ.pack(pady=5)                    
out = Label(root)                   # 存放計算結果
out.pack()                          
btn = Button(root,text="計算",command=cal)    # 計算按鈕
btn.pack(pady=5)

root.mainloop()





