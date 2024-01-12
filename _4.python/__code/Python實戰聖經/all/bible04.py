import os
import sys
import time
import random

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



from pydub import AudioSegment
from pydub.playback import play

record1 = AudioSegment.from_wav("record1.wav")
play(record1)


print('------------------------------------------------------------')	#60個

import moviepy.editor

filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

vsr = moviepy.editor.VideoFileClip(filename)
vsr.preview()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個






