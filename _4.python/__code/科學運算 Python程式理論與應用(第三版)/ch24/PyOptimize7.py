#coding:utf-8 
#file: PyOptimize7.py

import tkinter
import tkinter.messagebox,tkinter.simpledialog
import os,os.path
import threading

rubbishExt=['.tmp','.bak','.old','.wbk','.xlk','._mp','.log','.gid','.chk','.syd','.$$$','.@@@','.~*']

class Window:
	def __init__(self):
		self.root = tkinter.Tk()
		
		#建立選單
		menu = tkinter.Menu(self.root)

		#建立“系統”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="關於...",command = self.MenuAbout)
		submenu.add_separator()	
		submenu.add_command(label="離開", command = self.MenuExit)
		menu.add_cascade(label="系統", menu=submenu)
		
		#建立“清理”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="掃描垃圾檔案", command = self.MenuScanRubbish)
		submenu.add_command(label="移除垃圾檔案", command = self.MenuDelRubbish)
		menu.add_cascade(label="清理", menu=submenu)

		#建立“查詢”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="搜尋大檔案", command = self.MenuScanBigFile)	
		submenu.add_separator()				
		submenu.add_command(label="按名稱搜尋檔案", command = self.MenuSearchFile)
		menu.add_cascade(label="搜尋", menu=submenu)

		self.root.config(menu=menu)
		
		#建立標簽，用於顯示狀態訊息
		self.progress = tkinter.Label(self.root,anchor = tkinter.W,
			text = '狀態',bitmap = 'hourglass',compound = 'left')
		self.progress.place(x=10,y=370,width = 480,height = 15)

		#建立清單框，顯示檔案清單
		self.flist = tkinter.Text(self.root)
		self.flist.place(x=10,y = 10,width = 480,height = 350)
		
		#為清單框加入垂直卷動條
		self.vscroll = tkinter.Scrollbar(self.flist)
		self.vscroll.pack(side = 'right',fill = 'y')
		self.flist['yscrollcommand'] = self.vscroll.set
		self.vscroll['command'] = self.flist.yview

	#“關於”選單
	def MenuAbout(self):
		tkinter.messagebox.showinfo("PyOptimize",
			"這是使用Python撰寫的Windows改善程式。\n歡迎使用並提出寶貴意見！")

	#"離開"選單
	def MenuExit(self):
		self.root.quit();

	#"掃描垃圾檔案"選單
	def MenuScanRubbish(self):
		result = tkinter.messagebox.askquestion("PyOptimize","掃描垃圾檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始掃描垃圾檔案！")
		#self.ScanRubbish()
		self.drives =GetDrives()
		t=threading.Thread(target=self.ScanRubbish,args=(self.drives,))
		t.start()

	#"移除垃圾檔案"選單
	def MenuDelRubbish(self):
		result = tkinter.messagebox.askquestion("PyOptimize","移除垃圾檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始移除垃圾檔案！")
		self.drives =GetDrives()
		t=threading.Thread(target=self.DeleteRubbish,args=(self.drives,))
		t.start()		
	
	#"搜尋大檔案"選單
	def MenuScanBigFile(self):
		s = tkinter.simpledialog.askinteger('PyOptimize','請設定大檔案的大小(M)')
		t=threading.Thread(target=self.ScanBigFile,args=(s,))
		t.start()	
	
	#"按名稱搜尋檔案"選單
	def MenuSearchFile(self):
		s = tkinter.simpledialog.askstring('PyOptimize','請輸入檔名的部分字元')
		t=threading.Thread(target=self.SearchFile,args=(s,))
		t.start()	
	
	#掃描垃圾檔案
	def ScanRubbish(self,scanpath):
		global rubbishExt
		total = 0
		filesize = 0
		for drive in scanpath:
			for root,dirs,files in os.walk(drive):
				try:
					for fil in files:
						filesplit = os.path.splitext(fil)
						if filesplit[1] == '':	#若檔案無副檔名
							continue
						try:
							if rubbishExt.index(filesplit[1]) >=0:	#副檔名在垃圾檔案副檔名清單中
								fname = os.path.join(os.path.abspath(root),fil)
								filesize += os.path.getsize(fname)
								if total % 15 == 0:
									self.flist.delete(0.0,tkinter.END)
								
								l = len(fname)
								if l > 50:
									fname = name[:25] + '...' + fname[l-25:l]
								self.flist.insert(tkinter.END,fname + '\n')
								self.progress['text'] = fname
								total += 1	#計數
						except ValueError:
							pass
				except Exception as e:
					print(e)
					pass
		self.progress['text'] = "找到 %s 個垃圾檔案，共佔用 %.2f M 磁碟空間" % (total,filesize/1024/1024)

	#移除垃圾檔案
	def DeleteRubbish(self,scanpath):
		global rubbishExt
		total = 0
		filesize = 0
		for drive in scanpath:
			for root,dirs,files in os.walk(drive):
				try:
					for fil in files:
						filesplit = os.path.splitext(fil)
						if filesplit[1] == '':	#若檔案無副檔名
							continue
						try:
							if rubbishExt.index(filesplit[1]) >=0:	#副檔名在垃圾檔案副檔名清單中
								fname = os.path.join(os.path.abspath(root),fil)
								filesize += os.path.getsize(fname)

								try:
									os.remove(fname)	#移除檔案
									l = len(fname)
									if l > 50:
										fname = fname[:25] + '...' + fname[l-25:l]
									
									if total % 15 == 0:
										self.flist.delete(0.0,tkinter.END)

									self.flist.insert(tkinter.END,'Deleted '+ fname + '\n')
									self.progress['text'] = fname
									
									total += 1	#計數
								except:					#不能移除，則略過
									pass								
						except ValueError:
							pass
				except Exception as e:
					print(e)
					pass
		self.progress['text'] = "移除 %s 個垃圾檔案，收回 %.2f M 磁碟空間" % (total,filesize/1024/1024)	
	
	#搜尋大檔案
	def ScanBigFile(self,filesize):
		total = 0
		filesize = filesize * 1024 * 1024
		for drive in GetDrives():
			for root,dirs,files in os.walk(drive):
				for fil in files:
					try:
						fname = os.path.abspath(os.path.join(root,fil))						
						fsize = os.path.getsize(fname)

						self.progress['text'] = fname	#在狀態標簽中顯示每一個檢查的檔案
						if fsize >= filesize:							
							total += 1						
							self.flist.insert(tkinter.END, '%s，[%.2f M]\n' % (fname,fsize/1024/1024))							
					except:
						pass
		self.progress['text'] = "找到 %s 個超過 %s M 的大檔案" % (total,filesize/1024/1024)
	
	#按名稱搜尋檔案
	def SearchFile(self,fname):
		total = 0
		fname = fname.upper()
		for drive in GetDrives():
			for root,dirs,files in os.walk(drive):
				for fil in files:
					try:
						fn = os.path.abspath(os.path.join(root,fil))	
						l = len(fn)
						if l > 50:
							self.progress['text'] = fn[:25] + '...' + fn[l-25:l]	#在狀態標簽中顯示每一個檢查的檔案
						else:
							self.progress['text'] = fn			

						if fil.upper().find(fname) >= 0 :						
							total += 1						
							self.flist.insert(tkinter.END, fn + '\n')							
					except:
						pass
		self.progress['text'] = "找到 %s 個檔案" % (total)

	def MainLoop(self):
		self.root.title("PyOptimize")
		self.root.minsize(500,400)
		self.root.maxsize(500,400)
		self.root.mainloop()

#取得目前電腦的磁碟代號
def GetDrives():
	drives=[]
	for i in range(65,91):
		vol = chr(i) + ':/'
		if os.path.isdir(vol):
			drives.append(vol)
	return tuple(drives)


if __name__ == "__main__" :
	window = Window()
	window.MainLoop()