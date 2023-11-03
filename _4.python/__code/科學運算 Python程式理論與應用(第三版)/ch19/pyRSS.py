# -*- coding:utf-8 -*-
# file: pyRSS.py
#
import tkinter
import urllib.request
import xml.parsers.expat
class MyXML:									# XML解析類別
	def __init__(self, edit):
		self.parser = xml.parsers.expat.ParserCreate()			# 產生XMLParser
		self.parser.StartElementHandler = self.start			# 起始標示處理方法
		self.parser.EndElementHandler = self.end			# 結束標示處理方法
		self.parser.CharacterDataHandler = self.data			# 字元資料處理方法
		self.title = False						# 狀態標志
		self.date = False
		self.edit = edit						# 多行文字框物件
	def start(self, name, attrs):						# 起始標示處理方法
		if name == 'title':						# 判斷是否為title元素
			self.title = True					# 標志設為真
		elif name == 'pubDate':						# 判斷是否為pubDate
			self.date = True					# 標志設為真
		else:
			pass
	def end(self, name):							# 結束標示處理
		if name == 'title':
			self.title = False					# 標志設為假
		elif name == 'pubDate':
			self.date = False					# 標志設為假
		else:
			pass
	def data(self,data):							# 字元資料處理方法
		if self.title:							# 根據標志狀態輸出資料
			self.edit.insert(tkinter.END,
					'******************************\n')
			self.edit.insert(tkinter.END, 'Title: ')
			self.edit.insert(tkinter.END, data + '\n')
		elif self.date:
			self.edit.insert(tkinter.END, 'Date: ')
			self.edit.insert(tkinter.END, data + '\n')
		else:
			pass
	def feed(self, data):
		self.parser.Parse(data, 0)
class Window:
	def __init__(self, root):
		self.root = root							# 建立元件
		self.get = tkinter.Button(root,
				text = '取得RSS', command = self.Get)
		self.get.place(x = 280, y = 15)
		self.frame = tkinter.Frame(root, bd=2)
		self.scrollbar = tkinter.Scrollbar(self.frame)
		self.edit = tkinter.Text(self.frame,yscrollcommand = self.scrollbar.set,
				width = 96, height = 32)
		self.scrollbar.config(command=self.edit.yview)
		self.edit.pack(side = tkinter.LEFT)
		self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
		self.frame.place(y = 50)
	def Get(self):
		url = 'http://www.python.org/channews.rdf'
		page = urllib.request.urlopen(url)						# 開啟URL
		data = page.read()							# 讀取URL內容
		parser = MyXML(self.edit)						# 產生案例物件
		parser.feed(data)							# 處理XML資料
root = tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.maxsize(600,480)
root.mainloop()
