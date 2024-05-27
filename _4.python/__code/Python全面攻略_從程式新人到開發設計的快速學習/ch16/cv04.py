import requests, json, os
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# 指定電腦視覺分析的金鑰
subscriptionKey = '電腦視覺分析的金鑰'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = '電腦視覺分析服務網址'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定imagePath為分析圖像的本地路徑。
imagePath = "images/絲瓜水.jpg"
#imagePath = "images/劉德華.jpg"
#imagePath = "images/台北101.jpg"

# 將圖像讀入位元組陣列
imageData = open(imagePath, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定影像視覺特徵
params = {'visualFeatures': 
    'Description,Categories,Adult,Tags,Faces,Color,ImageType,Objects,Brands'}
response = requests.post(
    analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果
#print()
#strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
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

