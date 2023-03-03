# _*_ coding: utf-8 _*_
# 程式 12-3 (Python 2 Version)

import facebook

token = 'CAACEdEose0cBAFTD3DB8NrkDrVmQTH9esEZBTECpxInfKQTric2BNDDv3YgwdhfxfCZAXNfQy5gY0k8obkptR1K9RnQG1PwGMu4zqsltxHLcm5zPZBLbQInmEUHjtOhV4qxt5fFmAd0vtWMJjh0JZCoS5vj7ZBDIUe7AjnqRhosqZBfhszZAHZBgyJc3FxZCvDhZAsb3PokhzAiSuBZBl1KdmcH'

g = facebook.GraphAPI(access_token=token)

attachment =  {
	'name': '新聞直播台網址分享', 
	'link': 'http://drho.tw/news',
	'caption': '新聞直播台',
	'description': '在Youtube上已有許多的新聞台提供直播的功能，而這個網路就找出8個品質較佳的，做一個簡單的介面讓大家方便使用。',
	'picture': 'http://static.ettoday.net/web_2011/images/logo_ettoday.gif'
}

g.put_wall_post(message='這是使用 Python facebook-sdk 測試張貼的範例', attachment=attachment)

