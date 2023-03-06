def getFaceId(image_url):  #取得臉部Id
    face_url = face_base_url + 'detect'
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age',
    }
    data    = {'url': image_url}
    response = requests.post(face_url, headers=headers, params=params, json=data)
    faces = response.json()
    return faces[0]['faceId']

def verifyFace(faceid1, faceid2):  #比對臉部是否相同
    face_url = face_base_url + 'verify'
    data    = {
        'faceId1': faceid1,
        'faceId2': faceid2,
    }
    response = requests.post(face_url, headers=headers, json=data)
    result = response.json()
    #print(result)
    if result['isIdentical']== True:  #臉部相同
        return '兩張相片為同一人！'
    else:  #臉部不同
        return '兩張相片為不同人！'  

import requests

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

jengid1 = getFaceId("https://i.imgur.com/JKKvMiP.jpg")  #jeng照片一
jengid2 = getFaceId("https://i.imgur.com/dtusSZ1.jpg")  #jeng照片二
davidid1 = getFaceId("https://i.imgur.com/o4boWWG.jpg")  #david照片
print('傳入相同人員的不同照片：' + verifyFace(jengid1, jengid2))
print('\n傳入不同人員的照片：' + verifyFace(jengid1, davidid1))
