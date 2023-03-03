# _*_ coding: utf-8 _*_
# 程式 12-5 (Python 2 Version)

import facebook, shutil, requests

token = 'CAACEdEose0cBAHxsHGbrRJZBX5phLGcewZB26BWMklCiDccgPZBvGAg4eZA2mpFWdZC7eTPMgtZAgJjRti84hRJrTYwYVTLRzUrinAjUsgqc4hRuzg46cvOKGnYXiLW6hCJVu3rUQLaYtr9aVj0otDvAdx3a5xmbJZAUtT5SgS2GPQ4BxZAkZBQcSmPjPY14VpH3VELzZBqZAzJPjOreG6oXDVt'

g = facebook.GraphAPI(access_token=token)

photos = g.get_connections(id='me', connection_name='photos')

photos = photos['data']

for p in photos:
	image = p['images'][0]
 	filename = image['source'].split('/')[-1].split('?')[0]
 	print filename
	fp = open('fb-images/'+filename, 'wb')
	pic = requests.get(image['source'], stream=True)
	shutil.copyfileobj(pic.raw, fp)
	fp.close()
