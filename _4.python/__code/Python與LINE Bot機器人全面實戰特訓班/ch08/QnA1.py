import http.client, json

host = '你的主機'  #主機
endpoint_key = "你的授權碼"  #授權碼
kb = "你的GUID碼"  #GUID碼
method = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

while True:
    strin = input('輸入諮詢問題 (直接按 Enter 鍵就結束)：')
    if strin == '':
        break
    else:
        question = {  #問題
            'question': strin,
        }
        content = json.dumps(question)
        headers = {
            'Authorization': 'EndpointKey ' + endpoint_key,
            'Content-Type': 'application/json',
            'Content-Length': len(content)
        }
        conn = http.client.HTTPSConnection(host)  #連線
        conn.request("POST", method, content, headers)
        response = conn.getresponse()
        result = response.read()  #取得結果
        result1 = json.loads(result)  #轉為JSON格式
        print(result1['answers'][0]['answer'])  #顯示結果
