# _*_ coding: utf-8 _*_
# 程式 12-1 (Python 3 Version)

import requests, json

url = "https://graph.facebook.com/v2.5/me/posts?limit=50&since=1420070400&until=%C2%A01451606400&access_token=CAACEdEose0cBAHG7vhqsepqvLrFXWq4HSeCD03XejbXCDPijRP0sGpkZCyKsx2a31lZCqtpiCmPnjWXHWvUZCdwxw2PakjWQnm20FZBLs5Bse2WmlQhbqAunplewE0cZCo1vZAU9AalBb53awVrZBFhQhm9WmcLABpdrbVxcK4Deb0hmipZAibDf90Y2SVnVui57ITmA6ZC6hBXf9W9iiMQhZB"
res = requests.get(url)

data = json.loads(res.text)
for d in data['data']:
	if 'message' in d:
		print (d['created_time'], ':', d['message'])
		print('----------------------------------')
