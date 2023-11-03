# -*- coding:utf-8 -*-
# file: pyftp.py
#
from ftplib import FTP							# 從ftplib模組中匯入FTP
bufsize = 1024									# 設定緩沖區大小
def Get(filename):								# 下載檔案
	command = 'RETR ' + filename
	ftp.retrbinary(command, open(filename,'wb').write, bufsize)
	print('下載成功')
def Put(filename):								# 上傳檔案
	command = 'STOR ' + filename
	filehandler = open(filename,'rb')
	ftp.storbinary(command,filehandler,bufsize)
	filehandler.close()
	print('上傳成功')
def PWD():									# 取得目前目錄
	print(ftp.pwd())
def Size(filename):								# 取得檔案大小
	print(ftp.size(filename))
def Help():									# 輸出幫助
	print('''
	==================================
		Simple Python FTP 
	==================================
	cd		進入資料夾
	delete		移除檔案
	dir		取得目前檔案清單
	get		下載檔案
	help		幫助
	mkdir		建立資料夾
	put		上傳檔案
	pwd		取得目前目錄
	rename		更名檔案
	rmdir		移除資料夾
	size		取得檔案大小
	''')
server = input('請輸入FTP伺服器位址:')					# 取得伺服器位址
ftp = FTP(server)								# 連線到伺服器位址
username = input('請輸入使用者名稱:')						# 取得使用者名稱
password = input('請輸入密碼:')						# 取得字典
ftp.login(username,password)              					# 登入FTP
print(ftp.getwelcome())							# 取得歡迎訊息
actions  = {'dir':ftp.dir, 'pwd': PWD, 'cd':ftp.cwd, 'get':Get,			# 指令與對應的函數字典
		'put':Put, 'help':Help, 'rmdir': ftp.rmd, 
		'mkdir': ftp.mkd, 'delete':ftp.delete,
		'size':Size, 'rename':ftp.rename}
while True:									# 指令循環
	print('pyftp>',	)							# 輸出提示符
	cmds = input()							# 取得輸入
	cmd = str.split(cmds)						# 將輸入按空格分割
	try:									# 例外處理
		if len(cmd) == 1:						# 判斷指令是否有參數
			if str.lower(cmd[0]) == 'quit':			# 若果指令為quit則離開循環
				break
			else:
				actions[str.lower(cmd[0])]()			# 呼叫與指令對應的函數
		elif len(cmd) == 2:						# 處理指令有一個參數的情況
			actions[str.lower(cmd[0])](cmd[1])			# 呼叫與指令對應的函數
		elif len(cmd) == 3:						# 處理指令有兩個參數的情況
			actions[str.lower(cmd[0])](cmd[1],cmd[2])		# 呼叫與指令對應的函數
		else:
			print('輸入錯誤')
	except:
		print('指令出錯')
ftp.quit()									# 通訊埠連線
