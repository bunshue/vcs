import requests, json
import matplotlib.pyplot as plt
from matplotlib import patches
from PIL import Image
from io import BytesIO

# 指定電腦視覺分析的金鑰
subscriptionKey = '電腦視覺分析的金鑰'
# 指定電腦視覺分析服務網址(Web API)
# 分析服務網址是電腦視覺分析服務端點加上vision/v3.1/analyze
endpoint = '電腦視覺分析服務網址'
analyzeUrl = endpoint + "vision/v3.1/analyze"

# 指定imagePath為分析圖像的本地路徑。
imagePath = "images/日本旅遊.jpg"

# 將圖像讀入位元組陣列
imageData = open(imagePath, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
           'Content-Type': 'application/octet-stream'}

# 指定影像視覺特徵
params = {'visualFeatures': 'Description,Categories,Adult,Tags,Faces,Color,ImageType,Objects,Brands'}
response = requests.post(
    analyzeUrl, headers=headers, params=params, data=imageData)

dictAnalysis = response.json()   # 傳回分析結果，其結果為字典物件
#print(dictAnalysis)              # 印出分析結果
#strJson = json.dumps(dictAnalysis ,indent=4);  # 將分析結果轉成JSON字串資料
#print(strJson);  # 以JSON字串資料印出分析結果


tags=dictAnalysis['description']['tags']
imgCaption=dictAnalysis['description']['captions'][0]['text']
confidence=dictAnalysis['description']['captions'][0]['confidence']
print('影像標籤：%s' %(tags))
print('影像描述：%s' %(imgCaption))
print('描述信度：%f' %(confidence))
print()


image = Image.open(BytesIO(imageData))
plt.figure(figsize=(7,7))
plt.title(imgCaption, size="x-large", y=-0.1)
ax = plt.imshow(image)
plt.axis("off") 
print('影像人物資訊：')
for face in dictAnalysis['faces']:
    print('\t年齡：{}歲\t性別：{}'.format(face['age'], face['gender']))
    origin=(face['faceRectangle']['left'], face['faceRectangle']['top'])
    p = patches.Rectangle(origin, face['faceRectangle']['width'],
                          face['faceRectangle']['height'], fill=False, linewidth=3, color='b')
    ax.axes.add_patch(p)
    plt.text(origin[0], origin[1], '%s, %d'%(face['gender'], face['age']),
             fontsize=18, va='bottom', color='r')
plt.savefig('cv05.png', dpi=300) 	# 將圖檔與分析後的影像描述合併，檔名為cv05.png 
os.system('cv05.png')  	            # 開啟cv05.png

