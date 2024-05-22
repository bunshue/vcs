# -*- coding:utf-8 -*-
# file: TkinterFileDialog.py
#
import tkinter										# 匯入Tkinter模組
import tkinter.filedialog									# 匯入tkFileDialog模組
def FileOpen():										# 按鈕事件處理函數
	r = tkinter.filedialog.askopenfilename(title = 'Python Tkinter',			# 建立開啟檔案交談視窗
			filetypes=[('Python', '*.py *.pyw'),('All files', '*')]	)	# 指定檔案型態為Python指令稿
	print(r)									# 輸出傳回值
def FileSave():										# 按鈕事件處理函數
	r = tkinter.filedialog.asksaveasfilename(title = 'Python Tkinter',			# 建立儲存檔案交談視窗
			initialdir=r'E:\Python\code',					# 指定起始化目錄
			initialfile = 'test.py')					# 指定起始化檔案
	print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root,text = 'File Open',					# 建立按鈕
		command = FileOpen)							# 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tkinter.Button(root,text = 'File Save',
		command = FileSave)							# 指定按鈕事件處理函數
button2.pack(side='left')
root.mainloop()										# 進入訊息循環

