#coding:utf-8 
#file: pyOptimize1.py

import tkinter
import tkinter.messagebox

class Window:
	def __init__(self):
		self.root = tkinter.Tk()
		
		#建立選單
		menu = tkinter.Menu(self.root)

		#建立“系統”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="關於...")
		submenu.add_separator()	
		submenu.add_command(label="離開")
		menu.add_cascade(label="系統", menu=submenu)
		
		#建立“清理”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="掃描垃圾檔案")
		submenu.add_command(label="移除垃圾檔案")
		menu.add_cascade(label="清理", menu=submenu)

		#建立“查詢”子選單
		submenu = tkinter.Menu(menu, tearoff=0)	
		submenu.add_command(label="搜尋大檔案")	
		submenu.add_separator()				
		submenu.add_command(label="按名稱搜尋檔案")
		menu.add_cascade(label="搜尋", menu=submenu)

		self.root.config(menu=menu)
		
		#建立標簽，用於顯示狀態訊息
		self.progress = tkinter.Label(self.root,anchor = tkinter.W,
			text = '狀態',bitmap = 'hourglass',compound = 'left')
		self.progress.place(x=10,y=370,width = 480,height = 15)

		#建立清單框，顯示檔案清單
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

if __name__ == "__main__" :
	window = Window()
	window.MainLoop()