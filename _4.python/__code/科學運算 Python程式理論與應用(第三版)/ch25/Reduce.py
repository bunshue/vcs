#coding:utf-8 
#file: Reduce.py

import os,os.path,re

def Reduce(sourceFolder, targetFile):
	tempData = {}	#快取清單
	p_re = re.compile(r'(.*?)(\d{1,}$)',re.IGNORECASE) #用正規表示法解析資料
	for root,dirs,files in os.walk(sourceFolder):
		for fil in files:
			if fil.endswith('_map.txt'):	#是reduce檔案
				sFile = open(os.path.abspath(os.path.join(root,fil)), 'r')
				dataLine = sFile.readline()
	
				while dataLine:	#有資料
					subdata = p_re.findall(dataLine) #用空格分割資料
					#print(subdata[0][0],"  ",subdata[0][1])
					if subdata[0][0] in tempData:
						tempData[subdata[0][0]] += int(subdata[0][1])
					else:
						tempData[subdata[0][0]] = int(subdata[0][1])
					dataLine = sFile.readline()	#讀入下一行資料
	
				sFile.close()

	tList = []
	for key,value in sorted(tempData.items(),key = lambda k:k[1],reverse = True):
		tList.append(key + " " + str(value) + '\n')

	
	tFilename = os.path.join(sourceFolder,targetFile + "_reduce.txt")
	tFile = open(tFilename, 'a+')	#建立小檔案
	tFile.writelines(tList)	#將清單儲存到檔案中
	tFile.close()
	

if __name__ == "__main__" :
	Reduce("access","access")
