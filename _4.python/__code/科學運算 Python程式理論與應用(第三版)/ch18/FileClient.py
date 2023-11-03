# -*- coding:utf-8 -*-
# file: FileClient.py
#
import tkinter
import tkinter.filedialog
import socket
import os
class Window:
	def __init__(self, root):								# 建立元件
		label1 = tkinter.Label(root, text = 'IP')
		label2 = tkinter.Label(root, text = 'Port')
		label3 = tkinter.Label(root, text = '檔案')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		self.entryIP = tkinter.Entry(root)
		self.entryIP.insert(tkinter.END, '127.0.0.1')
		self.entryPort = tkinter.Entry(root)
		self.entryPort.insert(tkinter.END, '1051')
		self.entryData = tkinter.Entry(root)
		self.entryData.insert(tkinter.END, 'Hello')
		self.entryIP.place(x = 40, y = 5)
		self.entryPort.place(x = 40, y = 30)
		self.entryData.place(x = 40, y = 55)
		self.send = tkinter.Button(root, text = '傳送檔案', command = self.Send)
		self.openfile = tkinter.Button(root, text = '瀏覽', command = self.Openfile)
		self.send.place(x = 40, y = 80)
		self.openfile.place( x = 170, y = 55)
	def Send(self):										# 按鈕事件
		try:										# 例外處理
			ip = self.entryIP.get()							# 取得IP
			port = int(self.entryPort.get())					# 取得通訊埠
			filename = self.entryData.get()						# 取得傳送資料
			tt = filename.split('/')
			name = tt[len(tt)-1]
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 建立socket物件
			client.connect((ip,port))						# 連線服務端
			client.send(name.encode())							# 傳送檔名
			
			file = os.open(filename, os.O_RDONLY | os.O_EXCL|os.O_BINARY)		# 開啟檔案
			while 1:								# 傳送檔案
				data = os.read(file,1024)
				if not data:
					break
				client.send(data)
			os.close(file)								# 關閉檔案
			client.close()								# 關閉連線
		except Exception as e :
			print('傳送錯誤',e)
	def Openfile(self):
		r = tkinter.filedialog.askopenfilename(title = 'Python tkinter',			# 建立開啟檔案交談視窗
			filetypes=[('All files', '*'),('Python', '*.py *.pyw')])
		if r:
			self.entryData.delete(0, tkinter.END)
			self.entryData.insert(tkinter.END, r)
		
root = tkinter.Tk()
window = Window(root)
root.mainloop()

