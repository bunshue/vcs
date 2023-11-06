import requests
	
url = "https://www.taifex.com.tw/cht/3/totalTableDate"
post_data = "queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2020%2F08%2F07"
r = requests.post(url, data=post_data)
print(r.text)

