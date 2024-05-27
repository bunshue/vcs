import requests

urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)

print("網址：%s" %(response.url))
print("狀態：%s" %(response.status_code))
print("表頭：%s" %(response.headers))

