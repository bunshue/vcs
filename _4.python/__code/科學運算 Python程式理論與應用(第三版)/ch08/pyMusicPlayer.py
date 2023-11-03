# -*- coding:utf-8 -*-
# file: pyMusicPlayer.py
#
import tkinter										# 匯入tkinter模組
import tkinter.filedialog									# 匯入tkFileDialog模組
from win32com.client import Dispatch
class Window:
	def __init__(self):
		self.root = root = tkinter.Tk()						# 建立視窗
		buttonAdd = tkinter.Button(root, text = 'Add',
				command = self.add)
		buttonAdd.place(x = 150, y = 15)
		buttonPlay = tkinter.Button(root, text = 'Play',
				command = self.play)
		buttonPlay.place(x = 200, y = 15)
		buttonPause = tkinter.Button(root, text = 'Pause',
				command = self.pause)
		buttonPause.place(x= 250, y = 15)
		buttonStop = tkinter.Button(root, text = 'Stop',
				command = self.stop)
		buttonStop.place(x= 300, y = 15)
		buttonNext = tkinter.Button(root, text = 'Next',
				command = self.next)
		buttonNext.place(x = 350, y = 15)
		frame = tkinter.Frame(root, bd=2)
		self.playList = tkinter.Text(frame)
		scrollbar = tkinter.Scrollbar(frame)
		scrollbar.config(command=self.playList.yview)
		self.playList.pack(side = tkinter.LEFT)
		scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
		frame.place(y = 50)
		self.wmp = Dispatch('WMPlayer.OCX')					# 綁定WMPlayer.OCX
	def MainLoop(self):								# 進入訊息循環
		self.root.minsize(510,380)
		self.root.maxsize(510,380)
		self.root.mainloop()
	def add(self):									# 加入播放檔案
		file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
			filetypes=[('MP3', '*.mp3'), 
				('WMA', '*.wma'), ('WAV', '*.wav')])
		if file:
			media = self.wmp.newMedia(file)
			self.wmp.currentPlaylist.appendItem(media)
			self.playList.insert(tkinter.END, file + '\n')
	def play(self):
		self.wmp.controls.play()						# 播放檔案
	def pause(self):
		self.wmp.controls.pause()						# 暫停
	def next(self):
		self.wmp.controls.next()						# 下一首
	def stop(self):
		self.wmp.controls.stop()						# 停止
window = Window()
window.MainLoop()
