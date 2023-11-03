#coding:utf-8 
#file: Map.py

import os,os.path,re

def Map(sourceFile, targetFolder):
	sFile = open(sourceFile, 'r')
	dataLine = sFile.readline()
	tempData = {}	#快取清單
	if not os.path.isdir(targetFolder):  #若果目的目錄不存在，則建立
		os.mkdir(targetFolder)
	while dataLine:	#有資料
		p_re = re.compile(r'(GET|POST)\s(.*?)\sHTTP/1.[01]',re.IGNORECASE) #用正規表示法解析資料
		match = p_re.findall(dataLine)
		if match:
			visitUrl = match[0][1]
			if visitUrl in tempData:
				tempData[visitUrl] += 1
			else:
				tempData[visitUrl] = 1
		dataLine = sFile.readline()	#讀入下一行資料
	
	sFile.close()

	tList = []
	for key,value in sorted(tempData.items(),key = lambda k:k[1],reverse = True):
		tList.append(key + " " + str(value) + '\n')

	
	tFilename = os.path.join(targetFolder,os.path.split(sourceFile)[1] + "_map.txt")
	tFile = open(tFilename, 'a+')	#建立小檔案
	tFile.writelines(tList)	#將清單儲存到檔案中
	tFile.close()
	

if __name__ == "__main__" :
	Map("access\\access.log1.txt","access")
	Map("access\\access.log2.txt","access")
	Map("access\\access.log3.txt","access")
