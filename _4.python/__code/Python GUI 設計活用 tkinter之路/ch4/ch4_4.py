# ch4_4.py
from tkinter import *

counter = 0                                 # 計數的全域變數
def run_counter(digit):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        global counter
        counter += 1                        # 定義這是全域變數
        digit.config(text=str(counter))     # 列出標籤數字內容
        digit.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

root = Tk()
root.title("ch4_4")
digit=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=10,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
digit.pack()
run_counter(digit)                          # 呼叫數字更動方法
Button(root,text="結束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()




