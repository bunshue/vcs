import sys



print('------------------------------------------------------------')	#60個

print('應用：車牌辨識')

import keras_ocr
import re

def checkcharnum(str1):
    if re.match("^[a-z0-9]*$", str1): 
        return True
    else:
        return False

pipeline = keras_ocr.pipeline.Pipeline()
images = []
imgfiles = [
    'ABP0023.jpg',
    # '0655VN.jpg',
]
for imgfile in imgfiles:
    print('加入辨識圖片 :', imgfile)
    images.append(keras_ocr.tools.read(imgfile))

prediction_groups = pipeline.recognize(images)
#print(len(prediction_groups))
#print(prediction_groups)

for n in range(len(prediction_groups)):
    print('n =', n)
    result = ''
    if len(prediction_groups[n]) == 1:
        result = prediction_groups[n][0][0]
    else:
        txt = []
        xpos = []
        for i in range(len(prediction_groups[n])):
          temstr = prediction_groups[n][i][0]
          if checkcharnum(temstr) and len(temstr)<=7:
              txt.append(temstr) 
              xpos.append(prediction_groups[n][i][1][0][0])
        xtem = xpos.copy()
        xtem.sort()
        for i in range(len(xpos)):
            result += txt[xpos.index(xtem[i])]
    result = result.upper()
    print('第 {} 個車牌號碼：{}'.format(n+1, result)) 

print('------------------------------------------------------------')	#60個



