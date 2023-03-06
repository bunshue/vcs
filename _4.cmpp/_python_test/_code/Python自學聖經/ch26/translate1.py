import requests

subscription_key = "你的翻譯文字資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + 'translate?api-version=3.0'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = '&to=en'  #翻譯為英文
while True:
    textinput = input('輸入文句 (直接按 Enter 鍵就結束程式)：')
    if textinput != '':
        data    = [{'text' : textinput}]
        response = requests.post(trans_url, headers=headers, params=params, json=data)
        result = response.json()
        print('翻譯結果：' + result[0]['translations'][0]['text'])
        #print(result)
    else:
        break