import sys

print('------------------------------------------------------------')	#60個

print('pyocr：簡單易用OCR')

"""
!apt install tesseract-ocr libtesseract-dev tesseract-ocr
!pip install pyocr
"""

import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
# print(tools)
if len(tools) == 0:
    print("沒有可用的OCR！")
else:
  tool = tools[0]
  txt = tool.image_to_string(
      Image.open('text1.jpg'),
      builder=pyocr.builders.TextBuilder()
  )
  print("辨識文字：{}".format(txt))

print('------------------------------------------------------------')	#60個

print('keras-ocr模組：效果強大OCR')

import keras_ocr
import matplotlib.pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()
images = []
imgfiles = [
    'ad1.jpg',
    # 'ad02.jpg',
]
for imgfile in imgfiles:
    print('加入辨識圖片 :', imgfile)
    images.append(keras_ocr.tools.read(imgfile))

prediction_groups = pipeline.recognize(images)
#print(len(prediction_groups))
#print(prediction_groups)

_, axs = plt.subplots(ncols=len(images), figsize=(12, 8))
for i in range(len(prediction_groups)):
    if len(prediction_groups) == 1:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs)
    else:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs[i])

plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

