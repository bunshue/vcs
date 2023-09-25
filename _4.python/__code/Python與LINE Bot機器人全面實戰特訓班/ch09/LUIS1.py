import requests

text = '台東天氣如何？'
r = requests.get('https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/你的App ID/slots/production/predict?subscription-key=你的Key&verbose=true&show-all-intents=true&log=true&query=' + text)
result = r.json()
#print(result)
city = ''
try:
    if result["prediction"]['topIntent'] == '縣市天氣':
        city = result["prediction"]['entities']['地點'][0]
        if not city == '': 
            print('縣市名稱：' + city)
        else:
            print('找不到地點！')
    else:
        print('無法判斷文句！')
except:
    print('LUIS 產生錯誤！')
