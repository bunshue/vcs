# -*- coding:utf-8 -*-
# file: GetImage.py
#
import tkinter
import urllib.request
from  html.parser import HTMLParser
class MyHTMLParser(HTMLParser):						# 建立HTML解析類別
	def __init__(self):
		HTMLParser.__init__(self)
		self.gifs = []								# 建立清單，儲存gif
		self.jpgs = []								# 建立清單，儲存jpg
	def handle_starttag(self, tags, attrs):						# 處理起始標示
		if tags == 'img':							# 處理圖片
			for attr in attrs:
				for t in attr:
					if 'gif' in t:
						self.gifs.append(t)			# 新增到gif清單
					elif 'jpg' in t:
						self.jpgs.append(t)			# 新增到jpg清單
					else:
						pass
	def get_gifs(self):								# 傳回gif清單
		return self.gifs
	def get_jpgs(self):								# 傳回jpg清單
		return self.jpgs
class Window:
	def __init__(self, root):
		self.root = root							# 建立元件
		self.label = tkinter.Label(root, text = '輸入URL:')
		self.label.place(x = 5, y = 15)
		self.entryUrl = tkinter.Entry(root,width = 30) 
		self.entryUrl.place(x = 65, y = 15)
		self.get = tkinter.Button(root, 
				text = '取得圖片', command = self.Get)
		self.get.place(x = 280, y = 15)
		self.edit = tkinter.Text(root,width = 470,height = 600)
		self.edit.place(y = 50)
	def Get(self):
		url = self.entryUrl.get()						# 取得URL
		page = urllib.request.urlopen(url)						# 開啟URL
		data = page.read()							# 讀取URL內容
		parser = MyHTMLParser()							# 產生案例物件
		parser.feed(data.decode())							# 處理HTML資料
		self.edit.insert(tkinter.END, '====GIF====\n')				# 輸出資料
		gifs = parser.get_gifs()
		for gif in gifs:
			self.edit.insert(tkinter.END, gif + '\n')
		self.edit.insert(tkinter.END, '===========\n')
		self.edit.insert(tkinter.END, '====JPG====\n')
		jpgs = parser.get_jpgs()
		for jpg in jpgs:
			self.edit.insert(tkinter.END, jpg + '\n')
		self.edit.insert(tkinter.END, '===========\n')
		page.close()
root = tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()
