# -*- coding:utf-8 -*-
# file: client.py
#
import tkinter
import socket
class Window:
	def __init__(self, root):								# 建立元件
		label1 = tkinter.Label(root, text = 'IP')
		label2 = tkinter.Label(root, text = 'Port')
		label3 = tkinter.Label(root, text = 'Data')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		self.entryIP = tkinter.Entry(root)
		self.entryIP.insert(tkinter.END, '127.0.0.1')
		self.entryPort = tkinter.Entry(root)
		self.entryPort.insert(tkinter.END, '1051')
		self.entryData = tkinter.Entry(root)
		self.entryData.insert(tkinter.END, 'Hello')
		self.Recv = tkinter.Text(root)
		self.entryIP.place(x = 40, y = 5)
		self.entryPort.place(x = 40, y = 30)
		self.entryData.place(x = 40, y = 55)
		self.Recv.place(y = 115)
		self.send = tkinter.Button(root, text = '傳送資料', command = self.Send)
		self.send.place(x = 40, y = 80)
	def Send(self):										# 按鈕事件
		try:										# 例外處理
			ip = self.entryIP.get()							# 取得IP
			port = int(self.entryPort.get())					# 取得通訊埠
			data = self.entryData.get()						# 取得傳送資料
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 建立socket物件
			client.connect((ip,port))						# 連線服務端
			s = str(data).encode()
			client.send(s)							# 傳送資料
			rdata = client.recv(1024)						# 結束資料
			self.Recv.insert(tkinter.END, 'Server:' + rdata.decode()+ '\n')			# 輸出接受的資料
			client.close()								# 關閉連線
		except:
			self.Recv.insert(tkinter.END, '傳送錯誤\n')
root = tkinter.Tk()
window = Window(root)
root.mainloop()
