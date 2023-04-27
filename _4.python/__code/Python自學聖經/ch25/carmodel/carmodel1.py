import Algorithmia

input = "data://tsjeng/mlbook/car3.jpg"
try:
    client = Algorithmia.client('你的 API Key')
    algo = client.algo('LgoBE/CarMakeandModelRecognition/0.3.15')
    result = algo.pipe(input).result
    print('此車為 '+result[0]['model_year']+' 年份的 '+result[0]['make']+'，型號為 '+result[0]['model'])
    print('所有可能性：')
    print('%-10s %-10s %-18s %-10s %-4s' % ('style','confidence','make','model','year'))
    print('========== ========== ================== ========== ====')
    for i in range(len(result)):
        print('%-10s %-10s %-18s %-10s %-4s' % (result[i]['body_style'],result[i]['confidence'],result[i]['make'],result[i]['model'],result[i]['model_year']))
except:
    print('資料圖片檔案讀取錯誤！')
