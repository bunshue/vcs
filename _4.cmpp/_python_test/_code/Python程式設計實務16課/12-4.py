# _*_ coding: utf-8 _*_
# 程式 12-4 (Python 2 Version)

import facebook

token = 'CAACEdEose0cBAFTD3DB8NrkDrVmQTH9esEZBTECpxInfKQTric2BNDDv3YgwdhfxfCZAXNfQy5gY0k8obkptR1K9RnQG1PwGMu4zqsltxHLcm5zPZBLbQInmEUHjtOhV4qxt5fFmAd0vtWMJjh0JZCoS5vj7ZBDIUe7AjnqRhosqZBfhszZAHZBgyJc3FxZCvDhZAsb3PokhzAiSuBZBl1KdmcH'

g = facebook.GraphAPI(access_token=token)

posts = g.get_connections(id='me', connection_name='posts')

posts = posts['data']

for p in posts:
	print p['id'], 
	g.put_like(p['id'])
	print " -> ok..."
