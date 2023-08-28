from aip import AipOcr
import os
#百度识别车牌
"""请将申请的key写到项目根目录下的key.txt文件中，并且按照相应的内容进行填写"""
filename='file/key.txt'  #记申请的key的文件位置
if os.path.exists(filename):   #判断文件是否存在
	with open(filename,'r') as file:  #打开文件
		dictkey=eval(file.readlines()[0])  #读取全部内容转换为字典
		#以下获取的三个key是进入百度AI开放平台的撺掇中的应用到列表里创建应用得来的
		API_ID=dictkey['APP_ID'] #获取申请的APIID
		API_KEY=dictkey['API_KEY']   #获取申请的APIKEY
		SECRET_KEY=dictkey['SECRET_KEY']  #获取申请的SECRETKEY
else:
	print("请先在file目录下创建key.txt，并且写入申请的key!格式如下：" "\n{'API_ID',:'申请的APIID','API_KEY':'申请的APIKEY','SECRET_KEY':'申请的SECRETKEY'}")
#初始化AipOcr对象
client=AipOcr(API_ID,API_KEY,SECRET_KEY)
#读取文件
def get_file_content(filePath):
	with open(filePath,'rb') as fp:
		return fp.read()
	
#根据图片返回车牌呈
def getcn():
	#读取图片
	image=get_file_content('file/test.jpg')
	#调用车牌识别
	results=client.licensePlate(image)["words_result"]['number']
	#输出车牌号
	print(results)
	return results
