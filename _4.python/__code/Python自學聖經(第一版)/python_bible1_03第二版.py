"""
Python自學聖經(第二版) 24~

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個


# ch26\faceRecog1.py

from io import BytesIO
from PIL import Image
from matplotlib import patches
import requests
import matplotlib.pyplot as plt

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
face_url = face_base_url + "detect"
image_url = "https://image.freepik.com/free-photo/group-asian-male-female-friends-posing-together_1098-20702.jpg"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {
    "returnFaceId": "true",
    "returnFaceLandmarks": "false",
    "returnFaceAttributes": "age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise",
}
data = {"url": image_url}
response = requests.post(face_url, headers=headers, params=params, json=data)
result = response.json()
# print(result)

# 框選臉部及顯示部分資訊
image_file = BytesIO(requests.get(image_url).content)
image = Image.open(image_file)
plt.figure(figsize=(8, 8))
ax = plt.imshow(image)
for face in result:
    fr = face["faceRectangle"]  # 取得臉部坐標
    fa = face["faceAttributes"]  # 取得臉部屬性
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color="b"
    )  # 畫出矩形
    ax.axes.add_patch(p)
    plt.text(
        origin[0],
        origin[1],
        "%s, %d" % (fa["gender"], fa["age"]),
        fontsize=20,
        weight="bold",
        va="bottom",
        color="r",
    )  # 顯示資訊
plt.axis("off")

print("------------------------------------------------------------")  # 60個

# ch26\faceVerify1.py


def getFaceId(image_url):  # 取得臉部Id
    face_url = face_base_url + "detect"
    params = {
        "returnFaceId": "true",
        "returnFaceLandmarks": "false",
        "returnFaceAttributes": "age",
    }
    data = {"url": image_url}
    response = requests.post(face_url, headers=headers, params=params, json=data)
    faces = response.json()
    return faces[0]["faceId"]


def verifyFace(faceid1, faceid2):  # 比對臉部是否相同
    face_url = face_base_url + "verify"
    data = {
        "faceId1": faceid1,
        "faceId2": faceid2,
    }
    response = requests.post(face_url, headers=headers, json=data)
    result = response.json()
    # print(result)
    if result["isIdentical"] == True:  # 臉部相同
        return "兩張相片為同一人！"
    else:  # 臉部不同
        return "兩張相片為不同人！"


import requests

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}

girl1 = getFaceId("https://i.imgur.com/ZmeJH08.png")  # girl照片一
girl2 = getFaceId("https://i.imgur.com/RBpYZSQ.png")  # girl照片二
girl3 = getFaceId("https://i.imgur.com/HtoGSA2.png")  # girl照片三
print("傳入相同人員的不同照片：" + verifyFace(girl1, girl2))
print("\n傳入不同人員的照片：" + verifyFace(girl1, girl3))

print("------------------------------------------------------------")  # 60個

# ch26\imgAnalyze1.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
analyze_url = endpoint + "/vision/v3.0/analyze"
image_url = "https://i.imgur.com/r9R6Dzt.jpg"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"visualFeatures": "Categories,Description,Color"}
data = {"url": image_url}
response = requests.post(analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
# print(analysis)

# 顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]  # 取得圖片描述
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)  # 顯示圖片描述

print("------------------------------------------------------------")  # 60個

# ch26\imgAnalyze2.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
analyze_url = endpoint + "/vision/v3.0/analyze"
image_path = "media/street.jpg"  # 本機圖片檔路徑
image_data = open(image_path, "rb").read()  # 讀取圖片檔
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream",
}
params = {"visualFeatures": "Categories,Description,Color"}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
analysis = response.json()
# print(analysis)

# 顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)

print("------------------------------------------------------------")  # 60個

# ch26\landmark1.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
landmark_analyze_url = endpoint + "/vision/v3.0/models/landmarks/analyze"
image_url = "https://i.imgur.com/xZHkCDm.jpg"  # 台北101
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"model": "landmarks"}
data = {"url": image_url}
response = requests.post(
    landmark_analyze_url, headers=headers, params=params, json=data
)
analysis = response.json()
# print(analysis)

if len(analysis["result"]["landmarks"]) > 0:  # 如果有地標
    landmark_name = analysis["result"]["landmarks"][0]["name"]  # 取得地標名稱
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  # 未傳回地標
    print("無法辨識地標")

print("------------------------------------------------------------")  # 60個

# ch26\landmark2.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
landmark_analyze_url = endpoint + "/vision/v3.0/models/celebrities/analyze"
image_url = "https://i.imgur.com/mjxKiO8.jpg"  # 歐巴馬
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"model": "celebrities"}
data = {"url": image_url}
response = requests.post(
    landmark_analyze_url, headers=headers, params=params, json=data
)
analysis = response.json()
# print(analysis)

if len(analysis["result"]["celebrities"]) > 0:  # 如果有名人
    landmark_name = analysis["result"]["celebrities"][0]["name"]  # 取得名人資訊
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  # 未傳回名人資訊
    print("無法辨識名人資訊")

print("------------------------------------------------------------")  # 60個

# ch26\language1.py

import requests

subscription_key = "你的翻譯文字資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + "detect?api-version=3.0"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
while True:
    textinput = input("輸入文句 (直接按 Enter 鍵就結束程式)：")
    if textinput != "":
        data = [{"text": textinput}]
        response = requests.post(trans_url, headers=headers, json=data)
        result = response.json()
        print("輸入文句語言：" + result[0]["language"])
        # print(result)
    else:
        break

print("------------------------------------------------------------")  # 60個

# ch26\ocr1.py

import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
ocr_url = endpoint + "/vision/v3.0/ocr"  # ocr功能
image_url = "https://i.imgur.com/ptMvd6w.png"  # 遠端圖片
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"language": "unk", "detectOrientation": "true"}  # 自動偵測文字類別及方向
data = {"url": image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
analysis = response.json()
# print(analysis)  #列印結果

# line_infos串列儲存所有文字的坐標
line_infos = []
for region in analysis["regions"]:
    line_infos.append(region["lines"])
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
# 框選所有文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    # text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color="r")
    ax.axes.add_patch(patch)
plt.axis("off")  # 隱藏坐標軸

print("------------------------------------------------------------")  # 60個

# ch26\ocr2.py

import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源金鑰"  # 金鑰
endpoint = "你的電腦視覺資源端點網址"  # 端點
text_recognition_url = endpoint + "/vision/v3.0/read/analyze"  # 文字辨識功能
image_url = "https://i.imgur.com/VYLTAUV.jpg"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
data = {"url": image_url}
response = requests.post(text_recognition_url, headers=headers, json=data)

analysis = {}
flag = True  # 記錄是否辨識完成,False為辨識完成
while flag:
    response_final = requests.get(
        response.headers["Operation-Location"], headers=headers
    )
    analysis = response_final.json()  # 取得回傳值
    # print(analysis)  #顯示回傳值
    if "analyzeResult" in analysis:
        flag = False  # 回傳值有「analyzeResult」表示完成
    if "status" in analysis and analysis["status"] == "failed":
        flag = False  # 辨識失敗
    time.sleep(1)  # 辨識需時間,每1秒讀一次回傳值

polygons = []  # 取得每列坐標
if "analyzeResult" in analysis:
    polygons = []
    for line in analysis["analyzeResult"]["readResults"][0]["lines"]:
        polygons.append((line["boundingBox"], line["text"]))

# 框選及列印每列文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image)
for polygon in polygons:
    vertices = []
    for i in range(0, len(polygon[0]), 2):
        vertices.append((polygon[0][i], polygon[0][i + 1]))
    text = polygon[1]  # 取得文字
    patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color="r")
    ax.axes.add_patch(patch)
    plt.text(
        vertices[0][0], vertices[0][1], text, fontsize=20, va="top", color="b"
    )  # 列印文字
plt.axis("off")

print("------------------------------------------------------------")  # 60個

# ch26\translate1.py

import requests

subscription_key = "你的翻譯文字資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + "translate?api-version=3.0"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = "&to=en"  # 翻譯為英文
while True:
    textinput = input("輸入文句 (直接按 Enter 鍵就結束程式)：")
    if textinput != "":
        data = [{"text": textinput}]
        response = requests.post(trans_url, headers=headers, params=params, json=data)
        result = response.json()
        print("翻譯結果：" + result[0]["translations"][0]["text"])
        # print(result)
    else:
        break

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
