# -*- coding:utf-8 -*-
# file: pypop.py
#
import poplib
import re
import tkinter
class Window:
	def __init__(self, root):								# 建立元件
		label1 = tkinter.Label(root, text = 'POP3')
		label2 = tkinter.Label(root, text = 'Port')
		label3 = tkinter.Label(root, text = '使用者名稱')
		label4 = tkinter.Label(root, text = '密碼')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		label4.place(x = 5, y = 80)
		self.entryPOP = tkinter.Entry(root)
		self.entryPort = tkinter.Entry(root)
		self.entryUser = tkinter.Entry(root)
		self.entryPass = tkinter.Entry(root, show = '*')
		self.entryPort.insert(tkinter.END, '110')
		self.entryPOP.place(x = 50, y = 5)
		self.entryPort.place(x = 50, y = 30)
		self.entryUser.place(x = 50, y = 55)
		self.entryPass.place(x = 50, y = 80)
		self.get = tkinter.Button(root, text = '收取信件', command = self.Get)
		self.get.place(x = 60, y = 120)
		self.text = tkinter.Text(root)
		self.text.place(y=150)
	def Get(self):										# 按鈕事件
		try:										# 例外處理
			host = self.entryPOP.get()						# 取得伺服器位址
			port = int(self.entryPort.get())					# 取得通訊埠
			user = self.entryUser.get()						# 取得使用者名稱
			pw = self.entryPass.get()						# 取得密碼
			pop = poplib.POP3(host)							# 建立POP3案例
			pop.user(user)								# 登入伺服器
			pop.pass_(pw)
			stat = pop.stat()							# 取得狀態
			self.text.insert(tkinter.END, 						# 輸出狀態
					'Status: %d message(s), %d bytes\n' % stat)
			rx_headers  = re.compile(r"^(From|To|Subject)")				# 編譯正則表達
			for n in range(stat[0]):
				response, lines, bytes = pop.top(n + 1, 10)			# 收取信件的前10行
				self.text.insert(tkinter.END, 
						"Message %d (%d bytes)\n" % (n+1, bytes))
				self.text.insert(tkinter.END, "-" * 30 + '\n')
				str_lines=[]
				for l in lines:									#將接收到的byte轉為str
					str_lines.append(l.decode(encoding='gbk'))	#這裡使用gbk解碼
				self.text.insert(tkinter.END, 					# 輸出比對到的內容
						"\n".join(filter(rx_headers.match, str_lines)))
				self.text.insert(tkinter.END, '\n')
				self.text.insert(tkinter.END, "-" * 30  + '\n')
		except Exception as e :
			self.text.insert(tkinter.END, '接受錯誤\n')
			print(e)
root = tkinter.Tk()
window = Window(root)
root.mainloop()
