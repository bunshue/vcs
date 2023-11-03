# -*- coding:utf-8 -*-
# file: httpurl.py
#
import tkinter
import urllib.request

class Window:
	def __init__(self, root):
		self.root = root
		self.entryUrl = tkinter.Entry(root) 					# 建立元件
		self.entryUrl.place(x = 5, y = 15)
		self.get = tkinter.Button(root, 
				text = '下載頁面', command = self.Get)
		self.get.place(x = 160, y = 12)
		self.edit = tkinter.Text(root)
		self.edit.place(x=5, y = 50)
	def Get(self):
		url = self.entryUrl.get()						# 取得URL
		page = urllib.request.urlopen(url)						# 開啟URL
		data = page.read()							# 讀取URL內容
		self.edit.insert(tkinter.END, data)					# 將內容輸出到文字框
		page.close()
root = tkinter.Tk()
window = Window(root)
root.minsize(580,380)
root.mainloop()

