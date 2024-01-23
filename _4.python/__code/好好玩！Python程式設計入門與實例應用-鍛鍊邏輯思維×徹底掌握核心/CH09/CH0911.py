from tkinter import *

# 呼叫Tk()建構式產生主視窗
root = Tk()
# 方法title()顯示主視窗標題列的文字
root.title('秒數計算中...')
# 呼叫geometry()設視窗大小
root.geometry('100x100+150+150')

counter = 0 #儲存數值

# 自訂函式一：顯示標籤(Label)元件
def display(label):
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      label.config(text = str(counter),
         bg = 'pink', width = 20, height = 2)
      label.after(1000, count)
   count()
   
#設定標籤並把它放入主視窗
show = Label(root, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = Button(root, text = 'Stop',
    width = 20, command = root.destroy)
btnStop.pack()
root.mainloop()
