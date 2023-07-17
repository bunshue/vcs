import Algorithmia

input = {
  "image": "data://tsjeng/mlbook/black1.jpg",
}
try:
    client = Algorithmia.client('你的 API Key')
    algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
    print(algo.pipe(input).result)
except:
    print('資料圖片檔案讀取錯誤！')
    