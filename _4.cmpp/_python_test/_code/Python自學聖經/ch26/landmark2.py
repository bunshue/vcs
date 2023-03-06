import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
landmark_analyze_url = vision_base_url + "models/landmarks/analyze"
image_url = "https://i.imgur.com/sx3xwOq.jpg"  #歐巴馬
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'model': 'celebrities'}
data    = {'url': image_url}
response = requests.post(landmark_analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

if len(analysis["result"]["celebrities"]) > 0:  #如果有名人
    landmark_name = analysis["result"]["celebrities"][0]["name"]  #取得名人資訊
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  #未傳回地標
    print("無法辨識地標")
    