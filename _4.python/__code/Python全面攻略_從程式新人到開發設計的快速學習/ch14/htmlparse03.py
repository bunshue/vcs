import requests
# 指定圖片網址
imgUrl='http://www.drmaster.com.tw/Cover/MP22030.png'
imgName=imgUrl.split('/')[-1]
response= requests.get(imgUrl) 
f=open(imgName,'wb')  	# 指定開啟檔案路徑
# 將response.content二進位內容寫入為MP22030.png
f.write(response.content)  			
print('%s 下載完畢' %(imgName))
f.close()

