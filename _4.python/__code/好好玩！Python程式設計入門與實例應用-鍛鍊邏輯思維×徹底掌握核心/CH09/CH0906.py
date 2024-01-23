from tkinter import Tk, Label # step 1：匯入tkinter模組

# step 2: 產生Tkinter主視窗物件 - root
root = Tk()

# step 3: 主視窗加上一個標籤來顯示文字
lblShow = Label(root, text = 'Hello Python!!',
    width = 20, height = 4, fg = 'white', bg = 'gray')

# step 4: pack()方法做版面管理
lblShow.pack()
