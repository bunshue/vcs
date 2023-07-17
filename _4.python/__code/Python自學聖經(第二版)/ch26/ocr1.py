import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"    #金鑰
endpoint = "你的電腦視覺資源端點網址"        #端點
ocr_url = endpoint + "/vision/v3.0/ocr"    #ocr功能
image_url = "https://i.imgur.com/ptMvd6w.png"  #遠端圖片
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk', 'detectOrientation': 'true'}  #自動偵測文字類別及方向
data    = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)  #列印結果

#line_infos串列儲存所有文字的坐標
line_infos = []
for region in analysis["regions"]:
    line_infos.append(region["lines"])
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
#框選所有文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    #text = word["text"]
    origin = (bbox[0], bbox[1])
    patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='r')
    ax.axes.add_patch(patch)
plt.axis("off")  #隱藏坐標軸
