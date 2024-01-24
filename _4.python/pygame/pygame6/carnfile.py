from pandas import DataFrame
import os
import pandas as pd
#获取文件的路径
cdir=os.getcwd()
#文件路径
path=cdir+'datafile/'
#读取路径
if not os.path.exists(path+'停车场车辆表.xlsx'):
	#根据路径建立文件夹
	os.makedirs(path)
	#车牌号、日期、时间、价格、状态
	carnfile=pd.DataFrame(column=['carnumber','date','price','state'])
	#生成.xlsx文件
	carnfile.to_excel(path+'停车场车辆表.xlsx',sheet_name='data')	
	carnfile.to_excel(path+'停车场车辆表.xlsx',sheet_name='data')	
