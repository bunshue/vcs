"""

# 使用 deepface 模組

"""

from opencv_common import *

from deepface import DeepFace

filename = "data/FourPeople.jpg"


# 定義加入文字函式
def putText(x, y, text, size=30, color=WHITE):
    global image
    fontpath = "C:/_git/vcs/_1.data/______test_files1/_font/NotoSansTC-Bold.otf"  # 字型
    font = ImageFont.truetype(fontpath, size)  # 定義字型與文字大小
    imagePil = Image.fromarray(image)  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imagePil)  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 加入文字
    image = np.array(imagePil)  # 轉換成 np.array


# 定義該情緒的中文字
text_obj = {
    "angry": "生氣",
    "disgust": "噁心",
    "fear": "害怕",
    "happy": "開心",
    "sad": "難過",
    "surprise": "驚訝",
    "neutral": "正常",
}

print("------------------------------------------------------------")  # 60個

print("DeepFace.analyze 1")

image = cv2.imread(filename)
try:
    analyze = DeepFace.analyze(image)  # 辨識圖片人臉資訊
    print("共找到 :", len(analyze), "筆資料")
    for cc in analyze:
        # print(cc)
        print(
            "判斷結果 :",
            cc["dominant_gender"],
            cc["age"],
            cc["dominant_race"],
            cc["dominant_emotion"],
            "位置",
            cc["region"],
        )
        x = cc["region"]["x"]
        y = cc["region"]["y"]
        w = cc["region"]["w"]
        h = cc["region"]["h"]
        cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 5)  # 把臉框出來
except:
    print("找不到資料")
    pass

print("取出情緒資訊")
image = cv2.imread(filename)
try:
    analyze = DeepFace.analyze(image, actions=["emotion"])  # 辨識圖片人臉資訊，取出情緒資訊
    print("共找到 :", len(analyze), "筆資料 emotion")
    for cc in analyze:
        # print(cc)
        print(cc["region"])
        x = cc["region"]["x"]
        y = cc["region"]["y"]
        w = cc["region"]["w"]
        h = cc["region"]["h"]
        cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 5)  # 把臉框出來
except:
    print("找不到資料")
    pass

cv2.imshow("ImageShow", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("DeepFace.analyze 3")

image = cv2.imread(filename)
try:
    print("情緒資訊 emotion")
    emotion = DeepFace.analyze(image, actions=["emotion"])  # 情緒
    print(emotion)

    print("年齡資訊 age")
    age = DeepFace.analyze(image, actions=["age"])  # 年齡
    print(age)

    print("人種資訊 race")
    race = DeepFace.analyze(image, actions=["race"])  # 人種
    print(race)

    print("性別資訊 gender")
    gender = DeepFace.analyze(image, actions=["gender"])  # 性別
    print(gender)

    print("其他資訊")
    """ fail
    print(emotion['dominant_emotion'])
    print(age['age'])
    print(race['dominant_race'])
    print(gender['gender'])
    """
except:
    print("錯誤")
    pass

cv2.imshow("ImageShow", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("DeepFace.analyze 4")

filename = "data/FourPeople.jpg"
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 將圖片轉成灰階

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(xml_filename)  # 載入人臉模型

faces = face_cascade.detectMultiScale(image)  # 偵測人臉
print("共找到 :", len(faces), "張臉")

"""
#先把臉框出來
for x, y, w, h in faces:
    print(x, y, w, h)
    cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 5)  # 把臉框出來
"""
"""
cv2.imshow('ImageShow', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

for x, y, w, h in faces:
    # print(x, y, w, h)
    # 擴大偵測範圍，避免無法辨識情緒
    dd = 10
    x1 = x - dd
    x2 = x + w + dd
    y1 = y - dd
    y2 = y + h + dd
    # print(x1, x2, y1, y2)
    face = image[y1:y2, x1:x2]  # 取出人臉範圍

    try:
        # emotion = DeepFace.analyze(face, actions=["emotion"])  # 辨識情緒
        analyze = DeepFace.analyze(face)  # 辨識圖片人臉資訊
        print("共找到 :", len(analyze), "筆資料")
        cc = analyze[0]["dominant_emotion"]
        print(cc)

        """
        print(analyze[0]["dominant_emotion"])
        for cc in analyze:
            #print(cc)
            print('判斷結果 :', cc["dominant_gender"], cc["age"], cc["dominant_race"], cc["dominant_emotion"], '位置', cc["region"])
        """

        putText(x, y, text_obj[cc])  # 放入文字
    except:
        print("XXXXXXX")
        pass
    cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 2)  # 把臉框出來

cv2.imshow("ImageShow", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("DeepFace.analyze 5")

image = cv2.imread(filename)

try:
    analyze = DeepFace.analyze(image, actions=["emotion"])
    # print(type(analyze))
    # print(len(analyze))
    # print(analyze)
    for cc in analyze:
        emotion = cc["dominant_emotion"]  # 取得情緒文字
        x = cc["region"]["x"]
        y = cc["region"]["y"]
        # print("emotion = ", emotion, x, y)
        putText(x, y, text_obj[emotion])  # 放入文字
except:
    print("fail")
    pass

cv2.imshow("ImageShow", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用webcam TBD")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    image = frame
    try:
        analyze = DeepFace.analyze(image, actions=["emotion"])
        # fail TBD
        """
        for cc in analyze:
            emotion = cc["dominant_emotion"]  # 取得情緒文字
            x = cc["region"]["x"]
            y = cc["region"]["y"]
            #print("emotion = ", emotion, x, y)
            putText(x, y, text_obj[emotion])  # 放入文字
        """
    except:
        print("a", end="")
        pass

    cv2.imshow("ImageShow", image)
    if cv2.waitKey(5) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" 使用webcam
print("DeepFace.analyze 6")

cap = cv2.VideoCapture(0)        # 讀取攝影鏡頭

# 定義在畫面中放入文字的函式
def putText(source, x, y, text, scale=2.5, color=(255,255,255)):
    org = (x,y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)


a = 0        # 白色圖片透明度
n = 0        # 檔名編號
happy = 0    # 是否有 happy 的變數

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, image = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)   # 轉換成 BGRA，目的為了和白色圖片組合
    w = int(image.shape[1]*0.5)           # 取得圖片寬度的 1/2
    h = int(image.shape[0]*0.5)           # 取得圖片高度的 1/2
    image = cv2.resize(image,(w,h))         # 縮小圖片尺寸 ( 加快處理速度 )
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    key = cv2.waitKey(1)                # 每隔一毫秒取得鍵盤輸入資訊

    try:
        emotion = DeepFace.analyze(image, actions=['emotion'])               # 情緒偵測
        print(emotion['emotion']['happy'], emotion['emotion']['neutral'])  # 印出數值
        if emotion['emotion']['happy'] >0.5:
            happy = happy + 1       # 如果具有一點點 happy 的數值，就認定正在微笑，將 happy 增加 1
        else:
            happy = 0               # 如果沒有 happy，將 happy 歸零
    except:
        pass

    if happy == 1:
        a = 1                # 如果 happy 等於 1，將 a 變成 1 ，觸發拍照程式
        sec = 4              # 倒數秒數從 4 開始

    if key == 32:            # 按下空白將 a 等於 1 ( 按下空白也可以拍照 )
        a = 1
        sec = 4
    elif key == ord('q'):    # 按下 q 結束
        break

    if a == 0:
        output = image.copy()  # 如果 a 為 0，設定 output 和 photo 變數
    else:
        if happy >= 1:
            output = image.copy()
            photo = image.copy()
            sec = sec - 0.5       # 根據個人電腦效能，設定到接近倒數三秒
            putText(output, 10, 70, str(int(sec)))
            if sec < 1:
                output = cv2.addWeighted(white, a, photo, 1-a, 0)  # 計算權重，產生白色慢慢消失效果
                a = a - 0.5
                print('a', a)
                if a<=0:
                    a = 0
                    n = n + 1
                    cv2.imwrite(f'photo-{n}.jpg', photo)   # 存檔
                    print('save ok')
        else:
            a = 0
            pass
    cv2.imshow('ImageShow', output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗
"""
print("------------------------------------------------------------")  # 60個

print("Deepface：人臉特徵分析工具")

"""
#!pip install deepface
#人臉偵測
下載(488MB)
https://github.com/swghosh/DeepFace/releases/download/weights-vggface2-2d-aligned/VGGFace2_DeepFace_weights_val-0.9034.h5.zip
放到 C:/Users/070601/.deepface/weights 之下
要解壓縮
"""

imgpath = "data/deepface/person1.jpg"
img_sr = cv2.imread(imgpath)

plt.imshow(cv2.cvtColor(img_sr, cv2.COLOR_BGR2RGB))

image = DeepFace.detectFace(img_path=imgpath, enforce_detection=False)
plt.imshow(image)

image.shape
image *= 255.0
cv2.imwrite("tmp_detectFace.jpg", image[:, :, ::-1])
image = DeepFace.detectFace(
    img_path=imgpath, detector_backend="retinaface", enforce_detection=False
)
# image = DeepFace.detectFace(img_path=imgpath, detector_backend='mtcnn'', enforce_detection=False)
# image = DeepFace.detectFace(img_path=imgpath, detector_backend='dlib'', enforce_detection=False)
# image = DeepFace.detectFace(img_path=imgpath, detector_backend='ssd'', enforce_detection=False)  #有錯誤
# plt.imshow(image)
# plt.show()

print("------------------------------------------------------------")  # 60個

print("人臉驗證")

filename1 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk02.jpg"
filename2 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg"

# result = DeepFace.verify(filename1, filename2, model_name='DeepFace', model=DeepFace.build_model('DeepFace'), enforce_detection=False)
result = DeepFace.verify(
    filename1, filename2, model_name="DeepFace", enforce_detection=False
)

print(result)
if result["verified"]:
    print("兩張圖片是同一人！")
else:
    print("兩張圖片不是同一人！")

print("------------------------------------------------------------")  # 60個

"""
下載 566MB
https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
放在
C:/Users/070601/.deepface/weights/vgg_face_weights.h5

下載 90MB
https://github.com/serengil/deepface_models/releases/download/v1.0/facenet_weights.h5
放在
C:/Users/070601/.deepface/weights/facenet_weights.h5

下載 15MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/openface_weights.h5
放在
C:/Users/070601/.deepface/weights/openface_weights.h5


From: http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
To: C:/Users/070601/.deepface/weights/dlib_face_recognition_resnet_model_v1.dat.bz2

下載 131 MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5
To: C:/Users/070601/.deepface/weights/arcface_weights.h5

"""

filename1 = "data/deepface/bear1.jpg"
filename2 = "data/deepface/jeng1.jpg"

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
result = []
for model in models:
    ret = DeepFace.verify(
        filename1, filename2, model_name=model, enforce_detection=False
    )
    result.append(ret)
print(result)

print("搜尋人臉")

# 尋找單一相同人臉
filename1 = "data/deepface/bear2.jpg"
df = DeepFace.find(
    img_path=filename1, db_path="data/deepface/member", enforce_detection=False
)

print(type(df))
print(len(df))
print()
print()
print(df[0])
print()


""" 這一種特殊串列還不會分析出來
print("aaa")
cc = str(df)
cc = cc.split()
print("bbb")
print(cc)
print("ccc")
print(len(cc))
print("ddd")
for _ in cc:
    print(_)

"""


""" TBD
print(df['VGG-Face_cosine'])
print(type(df['VGG-Face_cosine']))

count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量

if count > 0:
  split1 = df['identity'][0].split('/')
  print(split1[-1])
else:
  print('沒有符合的人臉！')

#尋找所有相同人臉
filename1 = 'data/deepface/find_person.jpg'
df = DeepFace.find(img_path = filename1, db_path = 'member', enforce_detection=False)
#print(df)
count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量
if count > 0:
  for i in range(count):
    split1 = df['identity'][i].split('/')
    print(split1[-1])
else:
  print('沒有符合的人臉！')
"""

print("------------------------------------------------------------")  # 60個

''' TBD
print('範例：攝影機拍攝登入系統')

from IPython.display import display  # 用IPython
from IPython.display import Javascript  # 用IPython
#from IPython.display import Image  # 用IPython顯示圖片
#from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='person.jpg', quality=0.8):
  js = Javascript("""
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = '拍攝';
      div.appendChild(capture);
      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});
      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => capture.onclick = resolve);
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    """)
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

try:
  filename = take_photo()
  display(Image(filename))  # 用IPython顯示圖片
except Exception as err:
  print('攝影錯誤：{}'.format(str(err)))

df = DeepFace.find(img_path = 'person.jpg', db_path = 'member', enforce_detection=False)
#print(df)
count = np.sum((df['VGG-Face_cosine']<=0.25)!=0) #計算符合的人臉數量
if count > 0:
  print('歡迎登入系統！')
else:
  print('抱歉！你不是會員！')
  
print('人臉屬性分析')
'''

print("------------------------------------------------------------")  # 60個
"""
514MB
From: https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
To: C:/Users/070601/.deepface/weights/age_model_weights.h5
"""

filename = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg"

img = cv2.imread(filename)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

obj = DeepFace.analyze(
    img_path=filename,
    actions=["age", "gender", "race", "emotion"],
    enforce_detection=False,
)

print(obj)
print(type(obj))
print(len(obj))

""" 這一種特殊串列還不會分析出來
print('年齡：{}'.format(obj['age']))
print('性別：{}'.format(obj['gender']))
print('種族：{}'.format(obj['dominant_race']))
print('情緒：{}'.format(obj['dominant_emotion']))
"""

print("------------------------------------------------------------")  # 60個

'''TBD
print('範例：攝影機拍攝人臉屬性分析')

from IPython.display import display  # 用IPython
from IPython.display import Javascript  # 用IPython
from IPython.display import Image  # 用IPython顯示圖片
#from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='person.jpg', quality=0.8):
  js = Javascript("""
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = '拍攝';
      div.appendChild(capture);
      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});
      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => capture.onclick = resolve);
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    """)
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

try:
  filename = take_photo()
  display(Image(filename))  # 用IPython顯示圖片
except Exception as err:
  print('攝影錯誤：{}'.format(str(err)))

obj = DeepFace.analyze(img_path = 'person.jpg', actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)
label = {'angry':'生氣', 'disgust':'厭惡', 'fear':'恐懼', 'happy':'開心', 'neutral':'中性', 'sad':'悲傷', 'surprise':'吃驚',
          'Man':'男', 'Woman':'女',
          'asian':'亞洲', 'black':'黑', 'indian':'印第安', 'latino hispanic':'拉丁美洲', 'middle eastern':'中東', 'white':'白'}
print('\n你是{}歲的{}性{}人，目前情緒似乎是{}'.format(obj['age'], label[obj['gender']], label[obj['dominant_race']], label[obj['dominant_emotion']]))
'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
