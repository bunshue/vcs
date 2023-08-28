import tkinter
class mybutton:#定义按钮类
	#类初始化canvas1，label1是MyCanvals，mylabel的实例，因此可以使用类中的方法
	def __init__(self,root,canvas1,label1,type):
		self.root=root#保存引用值
		self.canvas1=canvas1
		self.label1=label1
		if type==0:#根据类型创建按钮
			button=tkinter.Button(root,text='画线',command=self.DrawLine)
		elif type==1:
			button=tkinter.Button(root,text='画扇形',command=self.DrawArc)
		elif type==2:
			button=tkinter.Button(root,text='画矩形',command=self.DrawRec)
		else:
			button=tkinter.Button(root,text='画椭圆',command=self.DrawOval)
		button.pack(side='left')
	def DrawLine(self):#DrawLine按钮事件处理函数
		self.label1.text.set('画直线')
		self.canvas1.SetStatus(0)#把status赋值，便于根据status的值进行画图
	def DrawArc(self):
		self.label1.text.set('画弧')
		self.canvas1.SetStatus(1)
	def DrawRec(self):
		self.label1.text.set('画矩形')
		self.canvas1.SetStatus(2)
	def DrawOval(self):
		self.label1.text.set('画椭圆')
		self.canvas1.SetStatus(3)
class MyCanvals:
	def __init__(self,root):
		self.status=0
		self.draw=0
		self.root=root
		self.canvas=tkinter.Canvas(root,bg='yellow',width=600,height=480)#生成canvas组件
		self.canvas.pack()
		self.canvas.bind('<ButtonRelease-1>',self.Draw)#绑定事件到左键
		self.canvas.bind('<Button-2>',self.Exit)#绑定事件到中键
		self.canvas.bind('<Button-3>',self.Del)#绑定事件到右键
		self.canvas.bind_all('<Delete>',self.Del)#绑定事件到delete键
		self.canvas.bind_all('<KeyPress-d>',self.Del)#绑定事件到d键
		self.canvas.bind_all('<KeyPress-e>',self.Exit)#绑定事件到e键
	def Draw(self,event):#绘图事件处理函数
		if self.draw==0:#判断是否绘图，先记录起始位置
			self.x=event.x
			self.y=event.y
			self.draw=1
		else:#根据self.status绘制不同的图形
			if self.status==0:
				self.canvas.create_line(self.x,self.y,event.x,event.y)
				self.draw=0
			elif self.status==1:
				self.canvas.create_arc(self.x,self.y,event.x,event.y)
				self.draw=0
			elif self.status==2:
				self.canvas.create_rectangle(self.x,self.y,event.x,event.y)
				self.draw=0
			else:
				self.canvas.create_oval(self.x,self.y,event.x,event.y)
				self.draw=0
	def Del(self,event):#按下右键或者d键删除图形
		items=self.canvas.find_all()
		for i in items:
			self.canvas.delete(i)
	def Exit(self,event):#按下中键或者e键退出
		self.root.quit()
	def SetStatus(self,status):#设置绘制的图形
		self.status=status
class mylabel:#定义标签类
	def __init__(self,root):
		self.root=root
		self.canvas1=canvas1
		self.text=tkinter.StringVar()#生成标签引用变量
		self.text.set('画线')
		self.label=tkinter.Label(root,textvariable=self.text,fg='blue',width=50)#生成标签
		self.label.pack(side='left')
root=tkinter.Tk()#生成主窗口
canvas1=MyCanvals(root)#生成实例
label1=mylabel(root)#生成实例
mybutton(root,canvas1,label1,0)
mybutton(root,canvas1,label1,1)
mybutton(root,canvas1,label1,2)
mybutton(root,canvas1,label1,3)
root.mainloop()#进入消息循环
