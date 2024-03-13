import requests #滙入requests套件

addr = 'https://www.edu.tw/'    #教育部
addr = 'https://www.books.com.tw/'

res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    print('status_code= ',res.status_code)
    res.encoding='utf-8'
    print(res.text)
else:
    print('網頁無法開啟, status_code= ',res.status_code)


import base64
from io import BytesIO
from PIL import Image

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg'
resp = requests.get(url)
img3 = Image.open(BytesIO(resp.content))
img3.save('tmp_Uranus2.jpg')

print(base64.b64encode(resp.content))






print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


