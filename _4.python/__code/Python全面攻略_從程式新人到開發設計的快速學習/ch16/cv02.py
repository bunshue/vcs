import requests, json

# 指定電腦視覺分析的金鑰
subscriptionKey = '電腦視覺分析的金鑰'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = '電腦視覺分析服務網址'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定imagePath為分析圖像的本地路徑。
imagePath = "images/劉德華.jpg"

# 將圖像讀入位元組陣列
imageData = open(imagePath, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定分析影像描述(Description)
params = {'visualFeatures': 'Description'}
response = requests.post(
    analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)
#print()              # 印出分析結果
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
