import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
analyze_url = vision_base_url + "analyze"
image_path = "street.jpg"  #本機圖片檔路徑
image_data = open(image_path, "rb").read()  #讀取圖片檔
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
analysis = response.json()
#print(analysis)

#顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
