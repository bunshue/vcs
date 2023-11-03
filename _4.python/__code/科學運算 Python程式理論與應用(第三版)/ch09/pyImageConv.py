# -*- coding:utf-8 -*-
# file: pyImageConv.py
#
import os										# 匯入模組
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox	
class Window:										# 建立視窗
	def __init__(self):
		self.root = root = tkinter.Tk()						# 建立元件
		label = tkinter.Label(root, text = '選取目錄')
		label.place(x = 5, y = 5)
		self.entry = tkinter.Entry(root)
		self.entry.place(x=60, y = 5)
		self.buttonBrowser = tkinter.Button(root, text = '瀏覽',
				command = self.Browser)
		self.buttonBrowser.place(x=210, y = 5)
		frameF = tkinter.Frame(root)
		frameF.place(x = 5, y = 30)
		frameT = tkinter.Frame(root)
		frameT.place(x = 100, y = 30)
		self.fImage = tkinter.StringVar()					# 產生關聯變數
		self.tImage = tkinter.StringVar()
		self.status = tkinter.StringVar()
		self.fImage.set('.bmp')
		self.tImage.set('.bmp')
		labelFrom = tkinter.Label(frameF, text = 'From')
		labelFrom.pack(anchor='w')
		labelTo = tkinter.Label(frameT, text = 'To')
		labelTo.pack(anchor='w')
		frBmp = tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.bmp', text = 'BMP' )
		frBmp.pack(anchor='w')
		frJpg = tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.jpg', text = 'JPG' )
		frJpg.pack(anchor='w')
		frGif = tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.gif', text = 'GIF' )
		frGif.pack(anchor='w')
		frPng = tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.png', text = 'PNG' )
		frPng.pack(anchor='w')
		trBmp = tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.bmp', text = 'BMP' )
		trBmp.pack(anchor='w')
		trJpg = tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.jpg', text = 'JPG' )
		trJpg.pack(anchor='w')
		trGif = tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.gif', text = 'GIF' )
		trGif.pack(anchor='w')
		trPng = tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.png', text = 'PNG' )
		trPng.pack(anchor='w')
		self.buttonConv = tkinter.Button(root, text = '轉換',
				command = self.Conv)
		self.buttonConv.place(x=80, y = 160)
		self.labelStatus = tkinter.Label(root,textvariable=self.status)
		self.labelStatus.place(x=50, y = 195)
	def MainLoop(self):									# 進入訊息循環
		self.root.minsize(250,220)
		self.root.maxsize(250,220)
		self.root.mainloop()
	def Browser(self):									# 瀏覽目錄
		directory = tkinter.filedialog.askdirectory(title='Python')
		if directory:
			self.entry.delete(0, tkinter.END)
			self.entry.insert(tkinter.END, directory)
	def Conv(self):										# 轉換檔案格式
		n = 0
		t = self.tImage.get()
		f = self.fImage.get()
		path = self.entry.get()
		if path == '':
			tkinter.messagebox.showerror('Python tkinter','請輸入路徑')
			return
		filenames = os.listdir(path)
		os.mkdir(path + '/' + t[-3:])
		for filename in filenames:
			if filename[-4:] == f:
				Image.open(path + '/' +filename).save(path +
						'/' + t[-3:] + '/' + filename[:-4] + t)
				n = n + 1
		self.status.set('成功轉換%d張圖片' % n)
window = Window()
window.MainLoop()
