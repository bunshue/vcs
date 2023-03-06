import Algorithmia
import cv2

input = {
  "image": "data://tsjeng/mlbook/facedetect2.jpg",
  "numResults": 7  #傳回的情緒種類數目
}
try:
    client = Algorithmia.client('你的 API Key')
    algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/1.0.1')
    emotion = algo.pipe(input).result['results'][0]['emotions']
    print('此人的表情為 '+emotion[0]['label'])
    print('所有可能性：')
    print('%-10s %-10s' % ('confidence','emotion'))
    print('========== ==========')
    for i in range(len(emotion)):
        print('%-10s %-10s' % (emotion[i]['label'],emotion[i]['confidence']))
    
    img = cv2.imread('../media/facedetect2.jpg')  #讀取本機圖片
    rect = algo.pipe(input).result['results'][0]['bbox']  #取得臉部坐標
    cv2.rectangle(img, (rect['left'],rect['top']), (rect['right'],rect['bottom']), (0,0,255), 2)  #畫出框線
    cv2.namedWindow("win")
    cv2.imshow("win", img)  #顯示圖片
    cv2.waitKey(0)  
    cv2.destroyWindow("win")
except:
    print('沒有偵測到人臉資訊！')
