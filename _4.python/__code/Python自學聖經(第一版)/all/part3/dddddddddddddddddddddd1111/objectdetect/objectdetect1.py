import Algorithmia
from PIL import Image

input = {
  "image": "data://tsjeng/mlbook/object2.jpg",
  "output": "data://.algo/deeplearning/ObjectDetectionCOCO/temp/output.png",
  "min_score": 0.5,  #最低信心指數
  "model": "ssd_mobilenet_v1"
}
try:
    client = Algorithmia.client('你的 API Key')
    algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.1')
    result = algo.pipe(input).result['boxes']
    cropobj = 'horse'  #要擷取的物件
    objfile = '../media/object2.jpg'  #本機檔名
    objlist = []  #儲存合乎條件的索引值
    for i in range(len(result)):
        if result[i]['label'] == cropobj:  #合乎條件就加入串列
            objlist.append(i)
    if len(objlist) > 0:  #如果要擷取的物件存在
        img1 = Image.open(objfile)  #讀入本機圖片檔
        for i in range(len(objlist)):
            n = objlist[i]  #取得索引值
            coord = result[n]['coordinates']  #取得坐標字典
            img2 = img1.crop((coord['x0'], coord['y0'], coord['x1'], coord['y1']))  #擷圖
            img2.save('../media/crop/' + cropobj + '{}.jpg'.format(i+1))  #存檔
    else:  #要擷取的物件不存在
        print('此圖沒有要擷取的物件！')
except:
    print('資料圖片檔案讀取錯誤！')
        