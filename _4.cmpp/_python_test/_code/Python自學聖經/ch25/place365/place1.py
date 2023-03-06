import Algorithmia

input = {
  "image": "data://tsjeng/mlbook/place1.jpg"
}
try:
    client = Algorithmia.client('你的 API Key')
    algo = client.algo('deeplearning/Places365Classifier/0.1.9')
    place = algo.pipe(input).result['predictions']
    print('此處最可能為 '+place[0]['class'])
    print('所有可能性：')
    print('%-25s %-15s' % ('class','probability'))
    print('========================= ===============')
    for i in range(len(place)):
        print('%-25s %-15s' % (place[i]['class'], place[i]['prob']))
except:
    print('資料圖片檔案讀取錯誤！')
