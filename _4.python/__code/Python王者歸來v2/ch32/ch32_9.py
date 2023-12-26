# ch32_9.py
import facebook
import os
import shutil
import requests

token = "EAAIZCihE7RSkBANrFuCjLGvzXurRpF3VZASyM5XOsKc8Ek3ZAF9jazB4x8YQSpKDabaTCzfLXcgZBbvJkuNWFEcs7pnrZCDMiXvxBImlXGmAh0NhXPnsYRyBqYGNHpHhS3FtbsgFZB0N0yBXgTTZAHAvBLBLhOHpYHqoHHIbj3uXs8EXynmBW6KbZCRrn518lxviw0DterMlpAZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.1')

picture = graph.get_connections(id='me',connection_name='photos?fields=images')

photos = picture['data']

mydir = "out32_9"
if not os.path.exists(mydir):
    os.mkdir(mydir)
n = 0
for p in photos:
    imageList = p['images']
    n += 1
    if n > 10:
        break
    for pict in imageList:
        filename = pict['source'].split('/')[-1].split('?')[0]
        dst = open(mydir+'/'+filename, 'wb')
        fig = requests.get(pict['source'], stream=True)
        shutil.copyfileobj(fig.raw, dst)
        dst.close()

















