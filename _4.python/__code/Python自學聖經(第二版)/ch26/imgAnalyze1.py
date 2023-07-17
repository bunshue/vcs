import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"    #金鑰
endpoint = "你的電腦視覺資源端點網址"        #端點
analyze_url = endpoint + "/vision/v3.0/analyze"
image_url = "https://i.imgur.com/r9R6Dzt.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key }
params  = {'visualFeatures': 'Categories,Description,Color'}
data    = {'url': image_url}
response = requests.post(analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

#顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]  #取得圖片描述
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)  #顯示圖片描述