#coding:utf-8 
#file: PyOptimize4.py

import tkinter
import tkinter.messagebox
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
	
	#"搜尋大檔案"選單
	def MenuScanBigFile(self):
		result = tkinter.messagebox.askquestion("PyOptimize","掃描大檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始掃描大檔案！")
	
	#"按名稱搜尋檔案"選單
	def MenuSearchFile(self):
		result = tkinter.messagebox.askquestion("PyOptimize","按名稱搜尋檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始按名稱搜尋檔案！")
	
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
									fname = fname[:25] + '...' + fname[l-25:l]
								
								self.flist.insert(tkinter.END,fname + '\n')
								self.progress['text'] = fname
								total += 1	#計數
						except ValueError:
							pass
				except Exception as e:
					print(e)
					pass
		self.progress['text'] = "找到 %s 個垃圾檔案，共佔用 %.2f M 磁碟空間" % (total,filesize/1024/1024)
	
	
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