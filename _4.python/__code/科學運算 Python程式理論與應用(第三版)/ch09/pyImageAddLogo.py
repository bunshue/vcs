# -*- coding:utf-8 -*-
# file: pyImageAddLogo.py
#
import os										# 匯入模組
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
	def __init__(self):
		self.root = root = tkinter.Tk()						# 建立視窗
		self.Image = tkinter.StringVar()
		self.status = tkinter.StringVar()
		self.mstatus = tkinter.IntVar()
		self.fstatus = tkinter.IntVar()
		self.pstatus = tkinter.IntVar()
		self.Image.set('bmp')
		self.mstatus.set(0)
		self.fstatus.set(0)
		self.pstatus.set(0)
		label = tkinter.Label(root, text = 'Logo')
		label.place(x = 5, y = 5)
		self.entryLogo = tkinter.Entry(root)
		self.entryLogo.place(x = 50, y = 5)
		self.buttonBrowserLogo = tkinter.Button(root, text = '瀏覽',
				command = self.BrowserLogo)
		self.buttonBrowserLogo.place(x = 200, y = 5)
		self.checkM = tkinter.Checkbutton(root, text ='批次轉換',
				command = self.OnCheckM,
				variable = self.mstatus,
				onvalue = 1,
				offvalue = 0)
		self.checkM.place(x = 5, y = 30)
		label = tkinter.Label(root, text = '選取檔案')
		label.place(x = 5, y = 55)
		self.entryFile = tkinter.Entry(root)
		self.entryFile.place(x = 60, y = 55)
		self.buttonBrowserFile = tkinter.Button(root, text = '瀏覽',
				command = self.BrowserFile)
		self.buttonBrowserFile.place(x=200, y = 55)
		label = tkinter.Label(root, text = '選取目錄')
		label.place(x = 5, y = 80)
		self.entryDir = tkinter.Entry(root,
				state = tkinter.DISABLED)
		self.entryDir.place(x=60, y = 80)
		self.buttonBrowserDir = tkinter.Button(root, text = '瀏覽',
				command = self.BrowserDir,
				state = tkinter.DISABLED)
		self.buttonBrowserDir.place(x=200, y = 80)

		self.checkF = tkinter.Checkbutton(root, text ='改變檔案格式',
				command = self.OnCheckF,
				variable = self.fstatus,
				onvalue = 1,
				offvalue = 0)
		self.checkF.place(x = 5, y = 110)
		frame = tkinter.Frame(root)
		frame.place(x = 10, y = 130)
		labelTo = tkinter.Label(frame, text = '格式')
		labelTo.pack(anchor='w')
		self.rBmp = tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'bmp', text = 'BMP',
				state = tkinter.DISABLED)
		self.rBmp.pack(anchor='w')
		self.rJpg = tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'jpg', text = 'JPG',
				state = tkinter.DISABLED)
		self.rJpg.pack(anchor='w')
		self.rGif = tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'gif', text = 'GIF',
				state = tkinter.DISABLED)
		self.rGif.pack(anchor='w')
		self.rPng = tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'png', text = 'PNG',
				state = tkinter.DISABLED) 
		self.rPng.pack(anchor='w')
		pframe = tkinter.Frame(root)
		pframe.place(x = 70, y = 130)
		labelPos = tkinter.Label(pframe, text = '位置')
		labelPos.pack(anchor = 'w')
		self.rLT = tkinter.Radiobutton(pframe, variable = self.pstatus,
				value = 0, text = '左上角')
		self.rLT.pack(anchor = 'w')
		self.rRT = tkinter.Radiobutton(pframe, variable = self.pstatus,
				value = 1, text = '右上角')
		self.rRT.pack(anchor = 'w')
		self.rLB = tkinter.Radiobutton(pframe, variable = self.pstatus,
				value = 2, text = '左下角')
		self.rLB.pack(anchor = 'w')
		self.rRB = tkinter.Radiobutton(pframe, variable = self.pstatus,
				value = 3, text = '右下角')
		self.rRB.pack(anchor = 'w')
		self.buttonAdd = tkinter.Button(root, text = '加入',
				command = self.Add)
		self.buttonAdd.place(x=180, y = 175)
		self.labelStatus = tkinter.Label(root,textvariable=self.status)
		self.labelStatus.place(x=150, y = 205)
	def MainLoop(self):									# 進入訊息循環
		self.root.minsize(250,270)
		self.root.maxsize(250,270)
		self.root.mainloop()
	def BrowserLogo(self):
		file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
			filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
				('GIF', '*.gif'), ('PNG', '*.png')])
		if file:
			self.entryLogo.delete(0, tkinter.END)
			self.entryLogo.insert(tkinter.END, file)
	def BrowserDir(self):									# 選取路徑
		directory = tkinter.filedialog.askdirectory(title='Python')
		if directory:
			self.entryDir.delete(0, tkinter.END)
			self.entryDir.insert(tkinter.END, directory)
	def BrowserFile(self):									# 選取檔案
		file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
			filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
				('GIF', '*.gif'), ('PNG', '*.png')])
		if file:
			self.entryFile.delete(0, tkinter.END)
			self.entryFile.insert(tkinter.END, file)
	def OnCheckM(self):									# 設定元件狀態
		if not self.mstatus.get():
			self.entryDir.config(state = tkinter.DISABLED)
			self.entryFile.config(state = tkinter.NORMAL)
			self.buttonBrowserDir.config(state = tkinter.DISABLED)
			self.buttonBrowserFile.config(state = tkinter.NORMAL)
		else:
			self.entryDir.config(state = tkinter.NORMAL)
			self.entryFile.config(state = tkinter.DISABLED)
			self.buttonBrowserDir.config(state = tkinter.NORMAL)
			self.buttonBrowserFile.config(state = tkinter.DISABLED)
	def OnCheckF(self):									# 設定元件狀態
		if not self.fstatus.get():
			self.rBmp.config(state = tkinter.DISABLED)
			self.rJpg.config(state = tkinter.DISABLED)
			self.rGif.config(state = tkinter.DISABLED)
			self.rPng.config(state = tkinter.DISABLED)
		else:
			self.rBmp.config(state = tkinter.NORMAL)
			self.rJpg.config(state = tkinter.NORMAL)
			self.rGif.config(state = tkinter.NORMAL)
			self.rPng.config(state = tkinter.NORMAL)
	def Add(self):										# 處理圖片
		n = 0
		if self.mstatus.get():
			path = self.entryDir.get()
			if path == '':
				tkinter.messagebox.showerror('Python tkinter','請輸入路徑')
				return
			filenames = os.listdir(path)
			if self.fstatus.get():
				f = self.Image.get()
				for filename in filenames:
					if filename[-3:] in ('bmp','jpg','gif','png'):
						self.addlogo(path + '/' + filename, f)
						n = n + 1
			else:
				for filename in filenames:
					if filename[-3:] in ('bmp','jpg','gif','png'):
						self.addlogo(path + '/' + filename)
						n = n + 1
		else:
			file = self.entryFile.get()
			if file == '':
				tkinter.messagebox.showerror('Python tkinter','請選取檔案')
				return
			if self.fstatus.get():
				f = self.Image.get()
				self.addlogo(file, f)
				n = n + 1
			else:
				self.addlogo(file)
				n = n + 1
		self.status.set('成功加入%d張圖片' % n)
	def addlogo(self, file, format = None):							# 向圖片加入Logo
		logo = self.entryLogo.get()
		if logo == '':
			tkinter.messagebox.showerror('Python tkinter','請選取Logo')
			return
		im = Image.open(file)
		lo = Image.open(logo)
		imwidth = im.size[0]
		imheight = im.size[1]
		lowidth = lo.size[0]
		loheight = lo.size[1]
		pos = self.pstatus.get()
		if pos == 0:
			left = 0
			top = 0
			right = lowidth
			bottom = loheight
		elif pos == 1:
			left = imwidth - lowidth
			top = 0
			right = imwidth
			bottom = loheight
		elif pos == 2:
			left = 0
			top = imheight - loheight
			right = lowidth
			bottom = imheight
		else:
			left = imwidth - lowidth
			top = imheight - loheight
			right = imwidth
			bottom = imheight
		im.paste(lo, (left, top, right, bottom))
		if format:
			im.save(file[:(len(file) - 4)] + '_logo.' + format)
		else:
			im.save(file[:(len(file) - 4)] + '_logo' + file[-4:])
window = Window()
window.MainLoop()

