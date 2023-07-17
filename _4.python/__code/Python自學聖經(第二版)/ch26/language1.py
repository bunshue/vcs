import  requests

subscription_key = "你的翻譯資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + 'detect?api-version=3.0'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
while True:
    textinput = input('輸入文句 (直接按 Enter 鍵就結束程式)：')
    if textinput != '':
        data    = [{'text' : textinput}]
        response = requests.post(trans_url, headers=headers, json=data)
        result = response.json()
        print('輸入文句語言：' + result[0]['language'])
        #print(result)
    else:
        break
