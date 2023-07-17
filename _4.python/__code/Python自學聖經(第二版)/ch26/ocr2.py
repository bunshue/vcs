import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"    #金鑰
endpoint = "你的電腦視覺資源端點網址"        #端點
text_recognition_url = endpoint + "/vision/v3.0/read/analyze"  #文字辨識功能
image_url = "https://i.imgur.com/VYLTAUV.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
data    = {'url': image_url}
response = requests.post(text_recognition_url, headers=headers, json=data)
     
analysis = {}
flag = True  #記錄是否辨識完成,False為辨識完成
while (flag):
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()  #取得回傳值
    #print(analysis)  #顯示回傳值
    if ("analyzeResult" in analysis): flag= False  #回傳值有「analyzeResult」表示完成
    if ("status" in analysis and analysis['status'] == 'failed'): flag= False  #辨識失敗
    time.sleep(1)  #辨識需時間,每1秒讀一次回傳值        

polygons=[]  #取得每列坐標
if ("analyzeResult" in analysis):
    polygons = []
    for line in analysis["analyzeResult"]["readResults"][0]["lines"]:
        polygons.append((line["boundingBox"], line["text"]))

#框選及列印每列文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image)
for polygon in polygons:
    vertices = []
    for i in range(0, len(polygon[0]), 2):
        vertices.append((polygon[0][i], polygon[0][i+1]))
    text = polygon[1]  #取得文字
    patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='r')
    ax.axes.add_patch(patch)
    plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top", color='b')  #列印文字
plt.axis("off")