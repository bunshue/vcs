import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"    #金鑰
endpoint = "你的電腦視覺資源端點網址"        #端點
landmark_analyze_url = endpoint + "/vision/v3.0/models/landmarks/analyze"
image_url = "https://i.imgur.com/xZHkCDm.jpg"  #台北101
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'model': 'landmarks'}
data    = {'url': image_url}
response = requests.post(landmark_analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

if len(analysis["result"]["landmarks"]) > 0:  #如果有地標
    landmark_name = analysis["result"]["landmarks"][0]["name"]  #取得地標名稱
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  #未傳回地標
    print("無法辨識地標")