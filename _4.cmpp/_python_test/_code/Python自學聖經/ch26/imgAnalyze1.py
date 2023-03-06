import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
analyze_url = vision_base_url + "analyze"
image_url = "https://i.imgur.com/BO7tlY7.jpg"
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
