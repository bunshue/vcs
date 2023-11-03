# -*- coding:utf-8 -*-
# file: TkinterDialog.py
#
import tkinter										# 匯入Tkinter模組
import tkinter.messagebox									# 匯入tkMesageBox模組
class MyDialog:										# 定義交談視窗類別
    def __init__(self, root):
        self.top = tkinter.Toplevel(root)					# 產生Toplevel元件
        label = tkinter.Label(self.top, text='Please Input')	# 產生標簽元件
        label.pack()
        self.entry = tkinter.Entry(self.top)					# 產生文字框元件
        self.entry.pack()
        self.entry.focus()							# 讓文字框獲得焦點
        button = tkinter.Button(self.top, text='Ok',command=self.Ok)					# 設定按鈕事件處理函數
        button.pack()
    def Ok(self):									# 定義按鈕事件處理函數
        self.input = self.entry.get()						# 取得文字框中內容，儲存為input
        self.top.destroy()							# 銷毀交談視窗
    def get(self):									# 傳回在文字框輸入的內容
        return self.input
class MyButton():									# 定義按鈕類別
    def __init__(self, root, type):							# 按鈕起始化
        self.root = root							# 儲存父視窗參考
        if type == 0:								# 根據型態建立不同按鈕
            self.button = tkinter.Button(root, text='Create',command = self.Create)				# 設定Create按鈕的事件處理函數
        else:
            self.button = tkinter.Button(root, text='Quit',command = self.Quit)				# 設定Quit按鈕的事件處理函數
        self.button.pack()
    def Create(self):								# Create按鈕的事件處理函數
        d = MyDialog(self.root)							# 產生交談視窗
        self.button.wait_window(d.top)						# 等待交談視窗結束
        tkinter.messagebox.showinfo('Python','You input:\n' + d.get())		# 取得交談視窗中輸入值，並輸出
    def Quit(self):									# Quit按鈕的事件處理函數
        self.root.quit()							# 離開主視窗
root = tkinter.Tk()									# 產生主視窗
MyButton(root,0)									# 產生Create按鈕
MyButton(root,1)									# 產生Quit按鈕
root.mainloop()										# 進入訊息循環
