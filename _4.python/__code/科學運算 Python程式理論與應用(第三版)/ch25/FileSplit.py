#coding:utf-8 
#file: FileSplit.py

import os,os.path,time

def FileSplit(sourceFile, targetFolder):
	sFile = open(sourceFile, 'r')
	number = 100000		#每個小檔案中儲存100000條資料
	dataLine = sFile.readline()
	tempData = []	#快取清單
	fileNum = 1
	if not os.path.isdir(targetFolder):  #若果目的目錄不存在，則建立
		os.mkdir(targetFolder)
	while dataLine:	#有資料
		for row in range(number): 
			tempData.append(dataLine)	#將一行資料新增到清單中
			dataLine = sFile.readline()
			if not dataLine :
				break
		tFilename = os.path.join(targetFolder,os.path.split(sourceFile)[1] + str(fileNum) + ".txt")
		tFile = open(tFilename, 'a+')	#建立小檔案
		tFile.writelines(tempData)	#將清單儲存到檔案中
		tFile.close()  
		tempData = []	#清理快取清單
		print(tFilename + " 建立於: " + str(time.ctime()))
		fileNum += 1		#檔案編號
			
	sFile.close()

if __name__ == "__main__" :
	FileSplit("access.log","access")
