#将pygame库导入到python中
import pygame
#窗体大小
size=1000,484
#设置帧率（帧率就是每秒显示的帧数）
FPS=60

#定义背景颜色 
DARKBLUE=(73,119,142)
BG=DARKBLUE  #指定背景颜色 
#pygame初始化
pygame.init()
#设置窗体名称
pygame.display.set_caption('智能候车场车牌识别计费系统')
#图标
ic_launcher=pygame.image.load('ic_launcher.png')
#设置图标
pygame.display.set_icon(ic_launcher)
#设置窗体大小
screen=pygame.display.set_mode(size)
#设置背景颜色
screen.fill(BG)
#游戏循环帧率设置
clock=pygame.time.Clock()
#主线程
Running=True
while Running:
	for event in pygame.event.get():
		#关闭页面游戏退出
		if event.type==pygame.QUIT:
			#退出
			pygame.quit()
			exit()
	#更新界面
	pygame.display.flip()
	#控制游戏最大帧率为60
	clock.tick(FPS)
			
import btn
#定义颜色
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(72,61,139)
GRAY=(96,96,96)
RED-(220,20,60)
YELLOW=(255,255,0)	


#创建识别按钮
button_go=btn.Button(screen,(640,480),150,60,BLUE,WHITE,'识别',25)
#绘制创建的按钮
button_go.draw_button()
for event in pygame.event.get():
	#关闭页面系统退出
	if event.tytpe==pygame.QUIT:
		#退出
		pygame.quit()
		exit()
		#识别按钮
		if 492<=event.pos[0] and event.pos[0]<=642 and 422<=event.pos[1] and event.pos[1]<=482:
			print('点击识别')
			try:
				#获取车牌
				carnumber=ocrutil.getcn()
			except:
				print('识别错误')
				continue
			pass



#读取文件内容
pi_talbe=pd.read_excel(path+'停车场车辆表.xlsx',sheet_name='data')
pi_info_tabel=pd.read_excel(path+'停车场信息表.xlsx',sheet_name='data')
#停车场车辆
cars=pi_talbe[['carnumber','data','state']].values
#已进入车辆数量
carn=len(cars)


#停车场车辆信息
def text3(screen):
	#使用系统字体
	xtfont=pygame.font.SysFont('SimHei',12)
	#获取文档表信息
	cars=pi_table[['carnumber','data','state']].values
	#页面只绘制10辆车的信息
	if len(cars)>10:
		cars=pd.read_excel(path+'停车场车辆表.xlsx',skiprows=len(cars)-10,sheet_name='data').values
		#动态绘制y点变量
		n=0
		#循环文档信息
		for car in cars:
			n+=1
			#车辆车牌号，车辆进入时间
			textstart=xtfont.render(str(car[0])+    +str(car[1]),True,WHITE)
			#获取文字图像位置
			text_rect=textstart.get_rect()
			#设置文字图像中心点
			text_rect.centerx=820
			text_rect.cnteryy=70+20*n
			#绘制内容
			screen.blit(textstart,text_rect)
		pass
			
			
	
#满预警
kcar=pi_info_tabel[pi_info_tabel['state']==2]
kcars=kcar['data'].values
#周标记，0代表周一
week_number=0
for k in kcars:
	week_number=timeutil.get_week_number(k)
#转换当前时间
localtime=time.strftime('%Y-%m-%d %H:%M',time.localtime())
#根据时间返回周标记，0代表周一
week_localtime=timeutil.get_week_number(localtime)
if week_number==0:
	if week_localtime==6:
		text6(screen,'根据数据分析，明天可能出现车位紧张的情况，请提前做好调度！')
	elif week_localtime==0:
		text6(screen,'根据数据分析，今天可能出现车位紧张的情况，请做好调度！')
		
else:
	if week_localtime+1==week_number:
		text6(screen,'根据数据分析，明天可能出现车位紧张的情况，请提前做好调度！')
	elif week_localtime==week_number:
		text6(screen,'根据数据分析，今天可能出现车位紧张的情况，请做好调度！')
pass		



#获取车牌号列数据
carsk=pi_table['carnumber'].values
#判断当前识别的车是否为停车场车辆
if carnumber in carsk:
	txt1='车牌号： '+carnumber
	#时间差
	y=0
	#获取行数用
	kcar=0
	#获取文档内容
	cars=pi_talbe[['carnumber','date','state']].values
	#循环数据
	for car in cars:
		#判断当前车辆根据当前车辆获取时间
		if carnumber==car[0]:
			#计算时间差0，1，2，...
			y=timeutil.DtCalc(car[1],localtime)
			break
		#行数+1
		kcar=kcar+1
	#判断停车时间，如果时间小于1，让其为1
	if y==0:
		y=1
	txt2='停车费：'+str(3*y)+"元"
	txt3='出停车场时间：'+localtime
	#删除停车场车辆表信息
	pi_talbe=pi_talbe.drop([kcar],axis=0)
	#更新停车场信息
	pi_info_tabel=pi_info_tabel.append({'carnumber':carnumber,'date':localtime,'price':3*y,'state':1},ignore_index=True)
	#保存信息更新.xlsx文件
	DataFrame(pi_talbe).to_excel(path+'停车场车辆表'+'.xlsx',sheet_name='data',index=False,header=True)
	DataFrame(pi_info_tabel).to_excel(path+'停车场信息表'+'.xlsx',sheet_name='data',index=False,header=True)
	#停车场车辆
	carn-=1
else:
	if carn<=Total:
		#添加到信息到文档['carnumber','date','price','state']
		pi_talbe=pi_talbe.append({'carnumber':carnumber,'date':localtime,'state':0},ignore_index=True)
		#生成.xlsx文件
		DataFrame(pi_talbe).to_excel(path+'停车场车辆表'+'.xlsx',sheet_name='data',index=False,header=True)
		if carn<Total:
			#state等于0时为停车场有车位的时候
			pi_info_tabel=pi_info_tabel.append({'carnumber':carnumber,'date':localtime,'state':0},ignore_index=True)
			#车辆数量+1
			carn+=1
		else:
			#state等于2时为停车场没有车位的时候
			pi_info_tabel=pi_info_tabel.append({'carnumber':carnumber,'date':localtime,'state':2},ignore_index=True)
			DataFrame(pi_info_tabel).to_excel(path+'停车场信息表'+'.xlsx',sheet_name='data',index=False,header=True)
						


import matplotlib.pyplot as plt

#创建“收入统计”按钮
button_go1=btn.Button(screen,(990,480),100,40,RED,WHITE,"收入统计",18)
#绘制创建的按钮
button_go1.draw_button()

#判断点击
if event.type==pygame.MOUSEBUTTONDOWN:
	#输出鼠标点击位置
	print(str(event.pos[0])+':'+str(event.pos[1]))
	#判断是否点击了“识别”按钮位置
	#“收入统计”按钮
	if 890<=event.pos[0] and event.pos[0]<=990 and 400<=event.pos[1] and event.pos[1]<=480:
		print('收入统计按钮')
		if income_switch:
			income_switch=False
			#设置窗体大小
			size=1000,484
			screen=pygame.display.set_mode(size)
			screen.fill(BG)
		else:
			income_switch=True
			#设置窗体大小
			size=1500,484
			screen=pygame.display.set_mode(size)
			screen=fill(BG)
			attr=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
			v1=[]
			#循环添加数据
			for i in range(1,13):
				k=i
				if i<10:
					k='0'+str(k)
					#筛选每月数据
					kk=pi_info_tabel[pi_info_tabel['date'].str.contains('2020-'+str(k))]
					#计算价格和
					kk=kk['price'].sum()
					v1.append(kk)
					#设置字体可以显示中文
					plt.rcParams['font.sans-serif']=['SimHei']
					#设置生成柱状图图片大小
					plt.figure(figsize=(3.9,4.3))
					#设置柱状图属性attr为x轴内容，v1为x轴内容相对的数据
					plt.bar(attr,v1,0.5,color='green')
					#设置数字标签
					for a,b in zip(attr,v1):
						plt.text(a,b,'%.0f' % b, ha='center',va='bottom',fontsize=7.5)
						#设置柱状图标题
						plt.title('每月收入统计')
						#设置y轴范围
						plt.ylim((0,max(v1)+50))
						#生成图片
						plt.savefig('file/ncome.png')
					pass
			

