# -*- coding:utf-8 -*-
# file: FileServer.py
#
import tkinter
import threading
import socket
import os
class ListenThread(threading.Thread):							# 建立監聽執行緒
	def __init__(self,edit,server):
		threading.Thread.__init__(self)
		self.edit = edit							# 儲存視窗中的多行文字框
		self.server = server
		self.file = 'receive.txt'
	def run(self):									# 進入監聽狀態
		while 1:								# 使用while循環不停監聽
			try:								# 捕捉例外
				self.client, addr = self.server.accept()  			# 等待連線
				self.edit.insert(tkinter.END,				# 向文字框中輸出狀態
						'連線來自:%s:%d\n' % addr)
				self.edit.insert(tkinter.END, 				# 向文字框中輸出資料
						'開始接收資料:')
				file = os.open(self.file, os.O_WRONLY|os.O_CREAT		# 建立檔案
						|os.O_EXCL|os.O_BINARY)
				while 1:
					rdata = self.client.recv(1024)			# 接受資料
					if not rdata:
						break
					os.write(file,rdata)				# 將資料寫入檔案
					self.edit.insert(tkinter.END,'......') 				# 向文字框中輸出進度
				os.close(file)						# 關閉檔案
				self.client.close()					# 關閉同用戶端的連線
				self.edit.insert(tkinter.END,				# 向文字框中輸出狀態
						'\n接收完畢,關閉用戶端\n')
			except:								# 例外處理
				self.edit.insert(tkinter.END,				# 向文字框中輸出狀態
						'\n網路錯誤,關閉連線\n')
				break							# 結束循環
class Control(threading.Thread):							# 控制執行緒
	def __init__(self, edit):
		threading.Thread.__init__(self)
		self.edit = edit							# 儲存視窗中的多行文字框
		self.event = threading.Event()						# 建立Event物件
		self.event.clear()							# 清楚event標志
	def run(self):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 建立socket連線
		server.bind(('', 1051))							# 綁定本機1051通訊埠
		server.listen(1)							# 開始監聽
		self.edit.insert(tkinter.END,'正在等待連線\n')				# 向文字框中輸出狀態
		self.lt = ListenThread(self.edit,server)				# 建立監聽執行緒物件
		self.lt.setDaemon(True)
		self.lt.start()								# 執行監聽執行緒
		self.event.wait()							# 進入等待狀態
		server.close()								# 關閉連線
	def stop(self):									# 結束控制執行緒
		self.event.set()							# 設定event標志
class Window:										# 主視窗
	def __init__(self, root):
		self.root = root
		self.butlisten = tkinter.Button(root, 					# 建立元件
				text = '開始監聽', command = self.Listen)
		self.butlisten.place(x = 20, y = 15)
		self.butclose = tkinter.Button(root, 
				text = '停止監聽', command = self.Close)
		self.butclose.place(x = 120, y = 15)
		self.edit = tkinter.Text(root)
		self.edit.place(y = 50)
	def Listen(self):								# 處理按鈕事件
		self.ctrl = Control(self.edit)						# 建立控制執行緒物件
		self.ctrl.setDaemon(True)
		self.ctrl.start()							# 執行控制執行緒
	def Close(self):
		self.ctrl.stop()							# 結束控制執行緒
root = tkinter.Tk()
window = Window(root)
root.mainloop()
