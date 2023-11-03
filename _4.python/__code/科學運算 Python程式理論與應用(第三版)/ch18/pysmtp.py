# -*- coding:utf-8 -*-
# file: pysmtp.py
#
import smtplib
import tkinter
class Window:
	def __init__(self, root):								# 建立元件
		label1 = tkinter.Label(root, text = 'SMTP')
		label2 = tkinter.Label(root, text = 'Port')
		label3 = tkinter.Label(root, text = '使用者名稱')
		label4 = tkinter.Label(root, text = '密碼')
		label5 = tkinter.Label(root, text = '收件人')
		label6 = tkinter.Label(root, text = '主旨')
		label7 = tkinter.Label(root, text = '發件人')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		label4.place(x = 5, y = 80)
		label5.place(x = 5, y = 105)
		label6.place(x = 5, y = 130)
		label7.place(x = 5, y = 155)
		self.entryPOP = tkinter.Entry(root)
		self.entryPort = tkinter.Entry(root)
		self.entryUser = tkinter.Entry(root)
		self.entryPass = tkinter.Entry(root, show = '*')
		self.entryTo = tkinter.Entry(root)
		self.entrySub = tkinter.Entry(root)
		self.entryFrom = tkinter.Entry(root)
		self.entryPort.insert(tkinter.END, '25')
		self.entryPOP.place(x = 50, y = 5)
		self.entryPort.place(x = 50, y = 30)
		self.entryUser.place(x = 50, y = 55)
		self.entryPass.place(x = 50, y = 80)
		self.entryTo.place(x = 50, y = 105)
		self.entrySub.place(x = 50, y = 130)
		self.entryFrom.place(x = 50, y = 155)
		self.get = tkinter.Button(root, text = '傳送信件', command = self.Get)
		self.get.place(x = 60, y = 180)
		self.text = tkinter.Text(root)
		self.text.place(y=220)
	def Get(self):										# 按鈕事件
		try:										# 例外處理
			host = self.entryPOP.get()						# 取得伺服器位址
			port = int(self.entryPort.get())					# 取得通訊埠
			user = self.entryUser.get()						# 取得使用者名稱
			pw = self.entryPass.get()						# 取得密碼
			fromaddr = self.entryFrom.get()						# 取得發件人
			toaddr = self.entryTo.get()						# 取得收件人
			subject = self.entrySub.get()						# 取得主旨
			text = self.text.get(1.0, tkinter.END)					# 取得信件內容
			msg = ("From: %s\nTo: %s\nSubject: %s\n\n"				# 產生信件頭
				% (fromaddr, toaddr, subject))
			msg = msg + text
			smtp = smtplib.SMTP(host,port)						# 連線伺服器
			smtp.set_debuglevel(1)							# 設定除錯等級
			smtp.login(user,pw)							# 登入伺服器
			smtp.sendmail(fromaddr, toaddr, msg)					# 傳送信件
			smtp.quit()								# 中斷伺服器
		except Exception as e:
			self.text.insert(tkinter.END, '傳送錯誤\n')
root = tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()
