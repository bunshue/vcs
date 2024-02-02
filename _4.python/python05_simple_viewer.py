'''
簡易播放一個檔案 簡易即可
1. 純文字檔 單純 cat
2. 播放圖片
3. 播放聲音檔案
4. 播放影片檔案


簡易顯示圖片的各種方法

'''

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import cv2
from matplotlib import pyplot as plt
'''
img_bgr = cv2.imread(filename)	#讀取本機圖片
img_rgb = img_bgr[:,:,::-1]     # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(img_rgb)
plt.show()
'''

'''
im = Image.open(filename)
print("%s:" % filename, im.format, "%dx%d" % im.size, im.mode)
print(im.info, im.tile)
'''

print('------------------------------------------------------------')	#60個
filename = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'
#filename = 'C:/_git/vcs/_1.data/______test_files1/quotes.txt'

fp = open(filename, 'r', encoding = 'UTF-8')
try:
    while 1:
        line = fp.readline()
        if not line:
            break
        print(line, end = '')
finally:
    fp.close()

print('------------------------------------------------------------')	#60個
with open(filename, 'r', encoding = 'UTF-8') as file:
    line = file.readlines()
#print(line)
    
for l in line:
    #print(l, end ="")
    print(l[:3])    #每行的前三字
    print(l[3:])    #每行的第三字開始到最後
    
print('------------------------------------------------------------')	#60個
'''
fp = open(filename, 'r', encoding = 'UTF-8')
line = fp.readlines()
fp.close()

print(line)
'''

print('------------------------------------------------------------')	#60個
#簡易播放一檔

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from matplotlib import pyplot as plt
img = cv2.imread(filename)
plt.imshow(img)
plt.show()


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'


from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load(filename)
#mixer.music.play()





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




