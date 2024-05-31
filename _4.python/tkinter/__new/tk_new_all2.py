# file: TkinterCanvas.py
#

import tkinter as tk

print("------------------------------------------------------------")  # 60個

root = tk.Tk()
canvas = tk.Canvas(root,
			width = 600,					# 指定Canvas元件的寬度
			height = 480,					# 指定Canvas元件的高度
			bg = 'white')					# 指定Canvas元件的背景色
im = tk.PhotoImage(file='python.gif')				# 使用PhotoImage開啟圖片
canvas.create_image(300,50,image = im)					# 使用create_image將圖片新增到Canvas元件中
canvas.create_text(302,77,						# 使用create_text方法在座標（302，77）處繪制文字
		text = 'Use Canvas'					# 所繪制文字的內容
		,fill = 'gray')						# 所繪制文字的彩色為灰色
canvas.create_text(300,75,
		text = 'Use Canvas',
		fill = 'blue')
canvas.create_polygon(290,114,316,114,330,130,				# 使用create_polygon方法繪制六邊形
		      310,146,284,146,270,130)
canvas.create_oval(280,120,320,140,					# 使用create_oval方法繪制橢圓
		fill = 'white')						# 設定橢圓用白色填充
canvas.create_line(250,130,350,130)					# 使用create_line繪制一條從（250,130）到（350,130）的直線
canvas.create_line(300,100,300,160)
canvas.create_rectangle(90,190,510,410,					# 使用create_rectangle繪制一個矩形
		width=5)						# 設定矩形線寬為5個像素
canvas.create_arc(100, 200, 500, 400, 					# 使用create_arc繪制圓弧
		start=0, extent=240, 					# 設定圓弧的起止角度
		fill="pink")						# 設定圓弧填充彩色
canvas.create_arc(103,203,500,400, 
		start=241, extent=118, 
		fill="red")
canvas.pack()								# 將Canvas新增到主視窗

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterCheck.py

root = tk.Tk()
r = tk.StringVar()						# 使用StringVar產生字串變數用於單選框元件
r.set('1')							# 起始化變數值
radio = tk.Radiobutton(root,				# 產生單選框元件
			variable = r, 				# 設定單選框關聯的變數
			value = '1',				# 設定勾選單選框時其所關聯的變數的值，即r的值
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '2',				# 當勾選該單選框時r的值為2
			text = 'Radio2' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '3',				# 當勾選該單選框時r的值為3
			text = 'Radio3' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '4',				# 當勾選該單選框時r的值為4
			text = 'Radio4' )
radio.pack()
c = tk.IntVar()						# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(root,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,				# 設定復選框關聯的變數
			onvalue = 1,				# 當勾選復選框時，c的值為1
			offvalue = 2)				# 當未勾選復選框時，c的值為2
check.pack()

root.mainloop()
print(r.get())							# 輸出r的值
print(c.get())						# 輸出c的值

print("------------------------------------------------------------")  # 60個

# tkinterColorChooser.py

import tkinter.colorchooser									# 匯入tkColorChooser模組

def ChooseColor():									# 按鈕事件處理函數
	r = tkinter.colorchooser.askcolor(title = 'Python Tkinter')				# 建立彩色選取交談視窗
	print(r)										# 輸出傳回值
root = tk.Tk()
button = tk.Button(root,text = 'Choose Color',					# 建立按鈕
		command = ChooseColor)							# 指定按鈕事件處理函數
button.pack()

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterDialog.py

import tkinter.messagebox									# 匯入tkMesageBox模組

class MyDialog:										# 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)					# 產生Toplevel元件
        label = tk.Label(self.top, text='Please Input')	# 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)					# 產生文字框元件
        self.entry.pack()
        self.entry.focus()							# 讓文字框獲得焦點
        button = tk.Button(self.top, text='Ok',command=self.Ok)					# 設定按鈕事件處理函數
        button.pack()
    def Ok(self):									# 定義按鈕事件處理函數
        self.input = self.entry.get()						# 取得文字框中內容，儲存為input
        self.top.destroy()							# 銷毀交談視窗
    def get(self):									# 傳回在文字框輸入的內容
        return self.input
class MyButton():									# 定義按鈕類別
    def __init__(self, root, type):							# 按鈕起始化
        self.root = root							# 儲存父視窗參考
        if type == 0:								# 根據型態建立不同按鈕
            self.button = tk.Button(root, text='Create',command = self.Create)				# 設定Create按鈕的事件處理函數
        else:
            self.button = tk.Button(root, text='Quit',command = self.Quit)				# 設定Quit按鈕的事件處理函數
        self.button.pack()
    def Create(self):								# Create按鈕的事件處理函數
        d = MyDialog(self.root)							# 產生交談視窗
        self.button.wait_window(d.top)						# 等待交談視窗結束
        tk.messagebox.showinfo('Python','You input:\n' + d.get())		# 取得交談視窗中輸入值，並輸出
    def Quit(self):									# Quit按鈕的事件處理函數
        self.root.quit()							# 離開主視窗
root = tk.Tk()									# 產生主視窗
MyButton(root,0)									# 產生Create按鈕
MyButton(root,1)									# 產生Quit按鈕

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterDraw.py


class MyButton:											# 定義按鈕類別
	def __init__(self,root,canvas,label,type):						# 類別起始化
		self.root = root								# 儲存參考值
		self.canvas = canvas
		self.label = label
		if type == 0:									# 根據型態建立按鈕
			button = tk.Button(root,text = 'DrawLine',
					command = self.DrawLine)
		elif type == 1:
			button = tk.Button(root,text = 'DrawArc',
					command = self.DrawArc)
		elif type == 2:
			button = tk.Button(root,text = 'DrawRec',
					command = self.DrawRec)
		else :
			button = tk.Button(root,text = 'DrawOval',
					command = self.DrawOval)
		button.pack(side = 'left')

	def DrawLine(self):									# DrawLine按鈕事件處理函數
		self.label.text.set('Draw Line')
		self.canvas.SetStatus(0)
	def DrawArc(self):									# DrawArc按鈕事件處理函數
		self.label.text.set('Draw Arc')
		self.canvas.SetStatus(1)
	def DrawRec(self):									# DrawRec按鈕事件處理函數
		self.label.text.set('Draw Rectangle')
		self.canvas.SetStatus(2)
	def DrawOval(self):									# DrawOval按鈕事件處理函數
		self.label.text.set('Draw Oval')
		self.canvas.SetStatus(3)
class MyCanvas:											# 定義Canvas類別
	def __init__(self,root):
		self.status = 0									# 儲存參考值
		self.draw = 0
		self.root = root
		self.canvas = tk.Canvas(root,bg = 'white',					# 產生Canvas元件
				width = 600,
				height = 480)
		self.canvas.pack()
		self.canvas.bind('<ButtonRelease-1>',self.Draw)					# 綁定事件到左鍵
		self.canvas.bind('<Button-2>',self.Exit)					# 綁定事件到中鍵
		self.canvas.bind('<Button-3>',self.Del)						# 綁定事件到右鍵
		self.canvas.bind_all('<Delete>',self.Del)					# 綁定事件到Delete鍵
		self.canvas.bind_all('<KeyPress-d>',self.Del)					# 綁定事件到d鍵
		self.canvas.bind_all('<KeyPress-e>',self.Exit)					# 綁定事件到e鍵
	def Draw(self,event):									# 繪圖事件處理函數
		if self.draw == 0: 								# 判斷是否繪圖
			self.x = event.x
			self.y = event.y
			self.draw = 1
		else:										# 根據self.status繪制不同圖形
			if self.status == 0:
				self.canvas.create_line(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 1:
				self.canvas.create_arc(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 2:
				self.canvas.create_rectangle(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			else:
				self.canvas.create_oval(self.x,self.y,
						event.x,event.y)
				self.draw = 0
	def Del(self,event):									# 當按下右鍵或d鍵則移除圖形
		items = self.canvas.find_all()
		for item in items:
			self.canvas.delete(item)
	def Exit(self,event):									# 當按下中鍵或e鍵則離開
		self.root.quit()
	def SetStatus(self,status):								# 設定繪制的圖形
		self.status = status
class MyLabel:											# 定義標簽類別
	def __init__(self,root):								# 類別起始化
		self.root = root								# 儲存參考
		self.canvas = canvas
		self.text = tk.StringVar()							# 產生標簽參考變數
		self.text.set('Draw Line')
		self.label = tk.Label(root,textvariable = self.text,			# 產生標簽
				fg = 'red',width = 50)
		self.label.pack(side = 'left')
root = tk.Tk()										# 產生主視窗
canvas = MyCanvas(root)										# 產生繪圖元件
label = MyLabel(root)										# 產生標簽
MyButton(root,canvas,label,0)									# 產生按鈕
MyButton(root,canvas,label,1)
MyButton(root,canvas,label,2)
MyButton(root,canvas,label,3)

root.mainloop()											# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterEntry.py

root = tk.Tk()
entry1 = tk.Entry(root,						# 產生單行文字框元件
			show = '*',)					# 輸入文字框中的字元被顯示為“*”
entry1.pack()								# 將文字框新增到視窗中
entry2 = tk.Entry(root,
			show = '#',					# 輸入文字框中的字元被顯示為“#”
			width = 50)					# 將文字框的寬度設定為50
entry2.pack()
entry3 = tk.Entry(root,
			bg = 'red',					# 將文字框的背景色設定為紅色
			fg = 'blue')					# 將文字框的前景色設定為藍色
entry3.pack()
entry4 = tk.Entry(root,
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
entry4.pack()
entry5 = tk.Entry(root,
			state = tk.DISABLED)			# 將文字框設定為禁用
entry5.pack()
edit1 = tk.Text(root,						# 產生多行文字框元件
			selectbackground = 'red',			# 將勾選文字的背景色設定為紅色
			selectforeground = 'gray')			# 將勾選文字的前景色設定為灰色
edit1.pack()

root.mainloop()								# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterLabel.py


root = tk.Tk()

label1 = tk.Label(root,
			anchor = tk.E,				# 設定文字的位置
			bg = 'blue',					# 設定標簽背景色
			fg = 'red',					# 設定標簽前景色
			text = 'Python',				# 設定標簽中的文字
			width = 30,					# 設定標簽的寬度為30
			height = 5)					# 設定標簽的的高度為5
label1.pack()
label2 = tk.Label(root,
			text = 'Python GUI\nTkinter',			# 設定標簽中的文字，在字串中使用換行符
			justify = tk.LEFT,				# 設定多行文字為齊左
			width = 30,
			height = 5)
label2.pack()
label3 = tk.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tk.RIGHT,			# 設定多行文字為齊右
			width = 30,
			height = 5)
label3.pack()
label4 = tk.Label(root,
			text = 'Python GUI\nTkinter',
			justify = tk.CENTER,			# 設定多行文字為劇中對齊
			width = 30,
			height = 5)
label4.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterMenu.py

root = tk.Tk()

menu = tk.Menu(root)						# 產生選單
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Open")					# 向下拉選單中加入Open指令
submenu.add_command(label="Save")					# 向下拉選單中加入Save指令
submenu.add_command(label="Close")					# 向下拉選單中加入Close指令
menu.add_cascade(label="File", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Copy")					# 向下拉選單中加入Copy指令
submenu.add_command(label="Paste")					# 向下拉選單中加入Paste指令
submenu.add_separator()							# 向下拉選單中加入分隔符
submenu.add_command(label="Cut")					# 向下拉選單中加入Cut指令
menu.add_cascade(label="Edit", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="About")					# 向下拉選單中加入About指令
menu.add_cascade(label="Help", menu=submenu)				# 將下拉選單新增到選單中
root.config(menu=menu)

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterMessageBox.py


import tkinter.messagebox									# 匯入tkMessageBox模組

def cmd():										# 按鈕訊息處理函數
	global n									# 使用全局變數n
	global buttontext								# 使用全局變數buttontext
	n = n + 1
	if n == 1:									# 判斷n的值，顯示不同的訊息框
		tkinter.messagebox.askokcancel('Python Tkinter','askokcancel')		# 使用askokcancel函數
		buttontext.set('skquestion')						# 變更按鈕上的文字
	elif n == 2:
		tk.messagebox.askquestion('Python Tkinter','skquestion')			# 使用askquestion函數
		buttontext.set('askyesno')
	elif n == 3:
		tk.messagebox.askyesno('Python Tkinter','askyesno')			# 使用askyesno函數
		buttontext.set('showerror')
	elif n == 4:
		tk.messagebox.showerror('Python Tkinter','showerror')			# 使用showerror函數
		buttontext.set('showinfo')
	elif n == 5:
		tk.messagebox.showinfo('Python Tkinter','showinfo')			# 使用showinfo函數
		buttontext.set('showwarning')
	else :
		n = 0									# 將n給予值為0重新開始循環
		tk.messagebox.showwarning('Python Tkinter','showwarning')		# 使用showwarning函數
		buttontext.set('askokcancel')
n = 0											# 為n賦初值
root = tk.Tk()
buttontext = tk.StringVar()							# 產生關聯按鈕文字的變數
buttontext.set('askokcancel')								# 設定buttontext值
button = tk.Button(root,								# 產生按鈕
		textvariable = buttontext,						# 設定關聯變數
		command = cmd)								# 設定事件處理函數
button.pack()

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個

# tkinterPopupmenu.py

root = tk.Tk()

menu = tk.Menu(root, tearoff=0)				# 建立選單
menu.add_command(label="Copy")					# 向出現式選單中加入Copy指令
menu.add_command(label="Paste")					# 向出現式選單中加入Paste指令
menu.add_separator()						# 向出現式選單中加入分隔符
menu.add_command(label="Cut")					# 向出現式選單中加入Cut指令
def popupmenu(event):						# 定義右鍵事件處理函數
    menu.post(event.x_root, event.y_root)			# 顯示選單
root.bind("<Button-3>", popupmenu)				# 在主視窗中綁定右鍵事件

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterRCButton.py

root = tk.Tk()

r = tk.StringVar()						# 使用StringVar產生字串變數用於單選框元件
r.set('1')							# 起始化變數值
radio = tk.Radiobutton(root,				# 產生單選框元件
			variable = r, 				# 設定單選框關聯的變數
			value = '1',				# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '2',				# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '3',				# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()
radio = tk.Radiobutton(root,
			variable = r,
			value = '4',				# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()
c = tk.IntVar()						# 使用IntVar產生整數變數用於復選框
c.set(1)
check = tk.Checkbutton(root,
			text = 'Checkbutton',			# 設定復選框的文字
			variable = c,				# 設定復選框關聯的變數
			indicatoron = 0,			# 將復選框繪製成按鈕型態
			onvalue = 1,				# 當勾選復選框時，c的值為1
			offvalue = 2)				# 當未勾選復選框時，c的值為2
check.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

# tkinterSimpleDialog.py

import tkinter.simpledialog									# 匯入tkSimpleDialog模組

def InStr():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askstring('Python Tkinter',					# 建立字串輸入交談視窗
			'Input String',							# 指定提示字元
			initialvalue='Tkinter')						# 指定起始化文字
	print(r)									# 輸出傳回值
def InInt():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askinteger('Python Tkinter','Input Integer')			# 建立整數輸入交談視窗
	print(r)
def InFlo():										# 按鈕事件處理函數
	r = tkinter.simpledialog.askfloat('Python Tkinter','Input Float')			# 建立浮點數輸入交談視窗
	print(r)
root = tk.Tk()
button1 = tk.Button(root,text = 'Input String',					# 建立按鈕
		command = InStr)							# 指定按鈕事件處理函數
button1.pack(side='left')
button2 = tk.Button(root,text = 'Input Integer',
		command = InInt)							# 指定按鈕事件處理函數
button2.pack(side='left')
button2 = tk.Button(root,text = 'Input Float',
		command = InFlo)							# 指定按鈕事件處理函數
button2.pack(side='left')

root.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個

