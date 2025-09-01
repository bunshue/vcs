import sys

import tkinter as tk

print("------------------------------------------------------------")  # 60個


import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改標籤上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 確認退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('溫馨提示', '確定要退出嗎?'):
            top.quit()

    # 創建頂層窗口
    top = tkinter.Tk()
    # 設置窗口大小
    top.geometry('240x160')
    # 設置窗口標題
    top.title('小遊戲')
    # 創建標籤對象並添加到頂層窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 創建一個裝按鈕的容器
    panel = tkinter.Frame(top)
    # 創建按鈕對象 指定添加到哪個容器中 通過command參數綁定事件回調函數
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 開啟主事件循環
    tkinter.mainloop()


if __name__ == '__main__':
    main()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


