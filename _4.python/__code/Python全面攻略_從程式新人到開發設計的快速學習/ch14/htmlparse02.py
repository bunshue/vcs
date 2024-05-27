import requests
urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)
response.encoding="utf-8"
print("網頁程式碼：%s" %(response.text))
