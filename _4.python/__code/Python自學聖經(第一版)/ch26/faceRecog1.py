from io import BytesIO
from PIL import Image
from matplotlib import patches
import requests
import matplotlib.pyplot as plt

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
face_url = face_base_url + 'detect'
image_url = "https://i.imgur.com/G4cZrJ0.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}
data    = {'url': image_url}
response = requests.post(face_url, headers=headers, params=params, json=data)
result = response.json()
#print(result)

#框選臉部及顯示部分資訊
image_file = BytesIO(requests.get(image_url).content)
image = Image.open(image_file)
plt.figure(figsize=(8,8))
ax = plt.imshow(image)
for face in result:
     fr = face["faceRectangle"]  #取得臉部坐標
     fa = face["faceAttributes"]  #取得臉部屬性
     origin = (fr["left"], fr["top"])
     p = patches.Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')  #畫出矩形
     ax.axes.add_patch(p)
     plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"], fa["age"]), fontsize=20, weight="bold", va="bottom", color='r')  #顯示資訊
plt.axis("off")
