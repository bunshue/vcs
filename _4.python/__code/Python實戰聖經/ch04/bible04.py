import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

# 多媒體圖片聲音影片處理

#Pillow：圖片處理

from PIL import Image

import matplotlib.pyplot as plt

img = Image.open("lion1.jpg")

plt.imshow(img)

plt.show()

w,h = img.size

img1 = img.resize((w*2,h), Image.ANTIALIAS)

plt.imshow(img1)

plt.show()

img2 = img.convert('1')

plt.imshow(img2)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：基本繪圖

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt

#繪直線

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.line([40,50,360,280], fill="blue", width=3)

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個


#繪矩形

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.rectangle((100,80,300,240), fill="yellow", outline="black")

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪點

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.point([(100,100), (100,101), (100,102)], fill='red')

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪圓或橢圓

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.ellipse((50,50,350,250), fill="purple", outline="green")

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪多邊形

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.polygon([(200,40),(60,250),(320,250)], fill="brown", outline="red")

plt.imshow(img)

plt.show()


print('------------------------------------------------------------')	#60個

#繪文字

from PIL import ImageFont



img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.text((150,80), "font demo", fill="red")  #繪英文文字

myfont = ImageFont.truetype("msyh.ttc",24)

drawimg.text((120,150),"雅黑字體示範", fill="blue", font=myfont)  #繪中文 

plt.imshow(img)

plt.show()

#繪文字

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.text((120,80), "English Demo", fill="red")  #繪製英文文字

myfont = ImageFont.truetype("taipei_sans_tc_beta.ttf", 24)

drawimg.text((120,150), "中文字型示範", fill="blue", font=myfont) #繪製中文文字

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：繪圖範例

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

img = Image.new("RGB", (300,400), "lightgray")

drawimg = ImageDraw.Draw(img)

#繪圓
drawimg.ellipse((50,50,250,250), width=3, outline="gold")# 臉

#繪多邊形
drawimg.polygon([(100,90), (120,130), (80,130)], fill="brown", outline="red") #左眼精
drawimg.polygon([(200,90), (220,130), (180,130)],   fill="brown", outline="red")#右眼精

#繪矩形
drawimg.rectangle((140,140,160,180),    fill="blue", outline="black") #鼻子

#繪橢圓
drawimg.ellipse((100,200,200,220), fill="red") #嘴巴   

#繪文字
drawimg.text((130,280), "e-happy", fill="orange")  #英文字

myfont = ImageFont.truetype("taipei_sans_tc_beta.ttf", 16)

drawimg.text((110,320), "文淵閣工作室", fill="red", font=myfont) #中文字 

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#pydub：聲音處理

import IPython.display as display

display.Audio("record1.wav", autoplay=True)

#!pip install pydub
#!pip install pydub==0.24.1

from pydub import AudioSegment

record1 = AudioSegment.from_wav("record1.wav")

print(record1.duration_seconds)

display.Audio("record1.wav", autoplay=True)

#record2 = record1[3000:9000]

#record2 = record1[:6000]

record2 = record1[-5000:]

print(record2.duration_seconds)

record2.export("record2.wav", format="wav")

display.Audio("record2.wav", autoplay=True)

#record3 = record1 + 8

record3 = record1 - 5

record3.export("record3.wav", format="wav")

display.Audio("record3.wav", autoplay=True)

birth = AudioSegment.from_wav("birth.wav")

print("birth 長度：" + str(birth.duration_seconds))

record4 = birth + record1

print("合併長度：" + str(record4.duration_seconds))

record4.export("record4.wav", format="wav")

display.Audio("record4.wav", autoplay=True)

#record5 = record1.fade_in(5000)  #5秒淡入

#record5 = record1.fade_out(3000)  #3秒淡出

record5 = record1.fade_in(5000).fade_out(3000)  #5秒淡入,3秒淡出

record5.export("record5.wav", format="wav")

display.Audio("record5.wav", autoplay=True)

record6 = record1.reverse()

record6.export("record6.wav", format="wav")

display.Audio("record6.wav", autoplay=True)

print('------------------------------------------------------------')	#60個

#moviepy：影片處理

from IPython.display import HTML

from base64 import b64encode

mp4 = open('holo1.mp4','rb').read()

data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML("""

<video width=400 controls>

      <source src="%s" type="video/mp4">

</video>

""" % data_url)

from moviepy.editor import *

vsr = VideoFileClip('holo1.mp4')

print('長度：' + str(vsr.duration))

print('幀數：' + str(vsr.fps))

print('解析度：' + str(vsr.size))

clip1 = vsr.subclip(10, 20)

print('clip1 長度：' + str(clip1.duration))

clip1.write_videofile('clip1.mp4')

clip2 = vsr.subclip(30, 50)

print('clip2 長度：' + str(clip2.duration))

clip2.write_videofile('clip2.mp4')

clip1 = VideoFileClip('clip1.mp4')

clip2 = VideoFileClip('clip2.mp4')

clip3 = concatenate_videoclips([clip1, clip2])

print('clip3 長度：' + str(clip3.duration))

clip3.write_videofile('clip3.mp4')

audio1 = AudioFileClip('holo1.mp4')

audio1.write_audiofile('holo1.mp3')

clip1_margin = clip1.margin(20)  #加黑邊

clip1_margin.write_videofile('clip1_margin.mp4')

clip1_mirrorx = clip1.fx(vfx.mirror_x)  #水平翻轉

clip1_mirrorx.write_videofile('clip1_mirrorx.mp4')

clip1_mirrory = clip1.fx(vfx.mirror_y)  #垂直翻轉

clip1_mirrory.write_videofile('clip1_mirrory.mp4')

clip1_resize = clip1.resize(0.50)  #改變尺寸

clip1_resize.write_videofile('clip1_resize.mp4')

clip1_mir_size = clip1.fx(vfx.mirror_x).resize(0.50)  #水平翻轉並改變尺寸

clip1_resize.write_videofile('clip1_resize.mp4')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



