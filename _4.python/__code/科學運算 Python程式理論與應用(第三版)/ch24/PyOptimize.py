#coding:utf-8 
#
import os,os.path,time
import tkinter
import tkinter.messagebox
import threading

p_file=[]

class Window:
	def __init__(self):
		self.root = tkinter.Tk()

		menu = tkinter.Menu(self.root)
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="關於...",command = self.MenuAbout)
		submenu.add_separator()	
		submenu.add_command(label="離開", command = self.MenuExit)
		menu.add_cascade(label="系統", menu=submenu)

		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="掃描垃圾檔案", command = self.MenuScanRubbish )
		submenu.add_command(label="移除垃圾檔案", command = self.MenuDelRubbish)
		menu.add_cascade(label="清理", menu=submenu)

		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="掃描大檔案", command = self.MenuScanBigFile)	
		submenu.add_separator()				
		submenu.add_command(label="查詢檔案", command = self.MenuSearchFile)
		menu.add_cascade(label="查詢", menu=submenu)

		self.root.config(menu=menu)
		
		self.progress = tkinter.Label(self.root,anchor = tkinter.W,text = '狀態',bitmap = 'hourglass',compound = 'left')
		self.progress.place(x=10,y=370,width = 480,height = 15)


		#清單框，顯示檔案清單
		self.flist = tkinter.Listbox(self.root)
		self.flist.place(x=10,y = 10,width = 480,height = 350)
		
		#為清單框加入垂直卷動條
		self.vscroll = tkinter.Scrollbar(self.flist)
		self.vscroll.pack(side = 'right',fill = 'y')
		self.flist['yscrollcommand'] = self.vscroll.set
		self.vscroll['command'] = self.flist.yview

	def MainLoop(self):
		self.root.title("PyOptimize")
		self.root.minsize(500,400)
		self.root.maxsize(500,400)
		self.root.mainloop()

	#“關於”選單
	def MenuAbout(self):
		tkinter.messagebox.showinfo("PyOptimize","這是使用Python撰寫的Windows改善程式。\n歡迎使用並提出寶貴意見！")


	#"離開"選單
	def MenuExit(self):
		self.root.quit();
	
	#"掃描垃圾檔案"選單
	def MenuScanRubbish(self):
		result = tkinter.messagebox.askquestion("提示","掃描垃圾檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		self.drives =GetDrives()
		t=threading.Thread(target=self.ScanRubbish,args=(self.drives,))
		t.start()


	#"移除垃圾檔案"選單
	def MenuDelRubbish(self):
		result = tkinter.messagebox.askquestion("提示","移除垃圾檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始移除垃圾檔案！")
		self.DelRubbish()
	
	#"掃描大檔案"選單
	def MenuScanBigFile(self):
		result = tkinter.messagebox.askquestion("提示","掃描大檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始掃描大檔案！")
		#檔案大小參考《Python標准庫》P202(6.1.4)
	
	#"查詢檔案"選單
	def MenuSearchFile(self):
		result = tkinter.messagebox.askquestion("提示","查詢檔案將需要較長的時間，是否繼續?")
		if result == 'no':
			return
		tkinter.messagebox.showinfo("PyOptimize","馬上開始查詢檔案！")
		#檔案時間參考《Python標准庫》P202(6.1.4)
	
	def ScanRubbish(self,scanpath):
		filenumber = 0;	#檔案數量
		filesize = 0;	#檔案大小
		for drive in scanpath:
			for root,dirs,files in os.walk(drive):
				for file in files:
					try:
						fname = os.path.join(os.path.abspath(root),file)
						l = len(fname)
						if l>60:
							self.progress['text'] = fname[:30] + '...' + fname[l-30:l]
						else:
							self.progress['text'] = fname
						filenumber += 1
						filesize += os.path.getsize(fname)
					except:
						pass
		self.flist.insert(tkinter.END,"檔案數量:"+str(filenumber))
		self.flist.insert(tkinter.END,"檔案大小:"+str(filesize))


	def DelRubbish(self):
		pass
	
	def AddStrToEdit(self,s):
		pass
		#self.edit.insert(tkinter.END, 
		#title_small + twitter['message']+'\n')

	def threadtest(self):
		p_file.append("1")
		p_file.append("2")
		time.sleep(5)

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



'''
若果不使用這個方法,檢查同樣能達到效果.不過使用 os.walk 方便很多了.這個方法傳回的是一個三元tupple(dirpath, dirnames, filenames),
其中第一個為起始路徑，
第二個為起始路徑下的資料夾,
第三個是起始路徑下的檔案.
dirpath是一個string，代表目錄的路徑,
dirnames是一個list，包括了dirpath下所有子目錄的名字,
filenames是一個list，包括了非目錄檔案的名字.這些名字不包括路徑訊息,若果需要得到全路徑,需要使用 os.path.join(dirpath, name).


下面是我是自己用遞歸實現的檢查檔案方法.
程式碼:
def listdir(leval,path):
    for i in os.listdir(path):
        print('|  '*(leval + 1) + i) 
        if os.path.isdir(path+i):
            listdir(leval+1, path+i)

path = 'c:'+os.sep+'ant'
#或是直接 path='C:/ant' 
print(path+os.sep)
listdir(0, path+os.sep)

'''