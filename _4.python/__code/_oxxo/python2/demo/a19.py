import requests

rep = requests.get('https://www.oxxostudio.tw/img/articles/201803/css-animation-01.gif')

with open("demo/test.gif", 'wb') as f:
  f.write(rep.content)