"""

全景圖

"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

"""
filename1 = 'C:/_git/vcs/_4.python/_data/penguin3.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/penguin4.jpg'
output_filename = 'tmp_penguin_all.jpg'
filenames = [filename1, filename2]
"""

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF2.jpg"
filename3 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF3.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF4.jpg"
filename5 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF5.jpg"
filename6 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF6.jpg"
filename7 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF7.jpg"
filename8 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF8.jpg"
output_filename = "tmp_SF_all.jpg"
filenames = [
    filename1,
    filename2,
    filename3,
    filename4,
    filename5,
    filename6,
    filename7,
    filename8,
]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)

stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", pano)
    cv2.imwrite(output_filename, pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")
else:
    print("error: {}".format(status))
