import sys

import requests, json

print("------------------------------------------------------------")  # 60個
print('azure 01')

# 指定電腦視覺分析的金鑰
subscriptionKey = 'e32a3adf441e4d678b37553f7ce7b437'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = 'https://davidimsazuretest.cognitiveservices.azure.com/'
analyzeUrl = endpoint + 'vision/v3.1/analyze'

# 指定 filename 為分析圖像的本地路徑。
filename = 'C:/_git/vcs/_4.python/_data/lena_color.jpg'

# 將圖像讀入位元組陣列
imageData = open(filename, 'rb').read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey, 'Content-Type': 'application/octet-stream'}

# 指定分析影像描述(Description)
params = {'visualFeatures': 'Description'}
response = requests.post(analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果

strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
print(strJson)  # 以JSON字串資料印出分析結果

print("------------------------------------------------------------")  # 60個
print('azure 02')

import requests, json

# 指定電腦視覺分析的金鑰
subscriptionKey = 'e32a3adf441e4d678b37553f7ce7b437'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = 'https://davidimsazuretest.cognitiveservices.azure.com/'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定 filename 為分析圖像的本地路徑。
filename = 'C:/_git/vcs/_4.python/_data/lena_color.jpg'

# 將圖像讀入位元組陣列
imageData = open(filename, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定分析影像描述(Description)
params = {'visualFeatures': 'Description'}
response = requests.post(
    analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)  # 印出分析結果

#strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
#print(strJson);  # 以JSON字串資料印出分析結果

imgTags = dictAnalysis['description']['tags']
print('影像標籤：', end='')
for tag in imgTags:
    print(tag, end=', ')
print()
imgCaption = dictAnalysis['description']['captions'][0]['text']
imgConfidence = dictAnalysis['description']['captions'][0]['confidence']
print('影像描述：%s'%(imgCaption))
print('分析信度：%f'%(imgConfidence))

print("------------------------------------------------------------")  # 60個
print('azure 03')

import requests, json, os
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# 指定電腦視覺分析的金鑰
subscriptionKey = 'e32a3adf441e4d678b37553f7ce7b437'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = 'https://davidimsazuretest.cognitiveservices.azure.com/'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定 filename 為分析圖像的本地路徑。
filename = 'C:/_git/vcs/_4.python/_data/lena_color.jpg'

# 將圖像讀入位元組陣列
imageData = open(filename, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定分析影像描述(Description)
params = {'visualFeatures': 'Description'}
response = requests.post(
    analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果

strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
print(strJson);  # 以JSON字串資料印出分析結果

imgTags = dictAnalysis['description']['tags']
print('影像標籤： ', end='')
for tag in imgTags:
    print(tag, end=', ')
print()
imgCaption = dictAnalysis['description']['captions'][0]['text']
imgConfidence = dictAnalysis['description']['captions'][0]['confidence']
print('影像描述：',imgCaption)
print('分析信度：',imgConfidence)

image = Image.open(BytesIO(imageData))
plt.imshow(image)
plt.axis("off")
plt.title(imgCaption, size="x-large", y=-0.15)

plt.savefig('azure03.png', dpi=300)  # 存圖

print("------------------------------------------------------------")  # 60個
print('azure 04')

import requests, json, os
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# 指定電腦視覺分析的金鑰
subscriptionKey = 'e32a3adf441e4d678b37553f7ce7b437'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = 'https://davidimsazuretest.cognitiveservices.azure.com/'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定 filename 為分析圖像的本地路徑。
filename = "images/台北101.jpg"
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_scenery/ggb6.jpg"

# 將圖像讀入位元組陣列
imageData = open(filename, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定影像視覺特徵
params = {'visualFeatures': 'Description,Categories,Adult,Tags,Faces,Color,ImageType,Objects,Brands'}
response = requests.post(analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果

strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
#print(strJson);  # 以JSON字串資料印出分析結果

if ('people_' in dictAnalysis['categories'][0]['name'] and
    'celebrities' in dictAnalysis['categories'][0]['detail']):
    celebrities=dictAnalysis['categories'][0]['detail']['celebrities'][0]['name']
    confidence=dictAnalysis['categories'][0]['detail']['celebrities'][0]['confidence']
    print('名人：%s' %(celebrities))
    print('信度：%f' %(confidence))
elif ('building_' in dictAnalysis['categories'][0]['name'] and
      'landmarks' in dictAnalysis['categories'][0]['detail']):   
    landmarks=dictAnalysis['categories'][0]['detail']['landmarks'][0]['name']
    confidence=dictAnalysis['categories'][0]['detail']['landmarks'][0]['confidence']
    print('地標：%s' %(landmarks))
    print('信度：%f' %(confidence))  

tags=dictAnalysis['description']['tags']
imgCaption=dictAnalysis['description']['captions'][0]['text']
confidence=dictAnalysis['description']['captions'][0]['confidence']
print('影像標籤：%s' %(tags))
print('影像描述：%s' %(imgCaption))
print('描述信度：%f' %(confidence))

print("------------------------------------------------------------")  # 60個
print('azure 05')

import requests, json
import matplotlib.pyplot as plt
from matplotlib import patches
from PIL import Image
from io import BytesIO

# 指定電腦視覺分析的金鑰
subscriptionKey = 'e32a3adf441e4d678b37553f7ce7b437'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = 'https://davidimsazuretest.cognitiveservices.azure.com/'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定 filename 為分析圖像的本地路徑。
filename = 'C:/_git/vcs/_4.python/_data/lena_color.jpg'

# 將圖像讀入位元組陣列
imageData = open(filename, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定影像視覺特徵
params = {'visualFeatures': 'Description,Categories,Adult,Tags,Faces,Color,ImageType,Objects,Brands'}
response = requests.post(analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果

strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
#print(strJson);  # 以JSON字串資料印出分析結果

tags=dictAnalysis['description']['tags']
imgCaption=dictAnalysis['description']['captions'][0]['text']
confidence=dictAnalysis['description']['captions'][0]['confidence']
print('影像標籤：%s' %(tags))
print('影像描述：%s' %(imgCaption))
print('描述信度：%f' %(confidence))
print()

image = Image.open(BytesIO(imageData))
plt.figure(figsize=(7,7))
plt.title(imgCaption, size="x-large", y=-0.1)
ax = plt.imshow(image)
plt.axis("off")

print('影像人物資訊：')
for face in dictAnalysis['faces']:
    origin=(face['faceRectangle']['left'], face['faceRectangle']['top'])
    p = patches.Rectangle(origin, face['faceRectangle']['width'], face['faceRectangle']['height'], fill=False, linewidth=3, color='b')
    ax.axes.add_patch(p)

plt.savefig('azure05.png', dpi=300) 	# 存圖

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




