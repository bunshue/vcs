import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

PAD = 5  # 設定要忽略鄰近影像邊緣多少距離的像素數

def find_transient(image, diff_image, pad):
    transient = False
    height, width = diff_image.shape
    cv2.rectangle(image, (PAD, PAD), (width - PAD, height - PAD), 255, 1)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(diff_image)
    if pad < maxLoc[0] < width - pad and pad < maxLoc[1] < height - pad:
        cv2.circle(image, maxLoc, 10, 255, 0)
        transient = True
    return transient, maxLoc

filename1 ="file1.png"
filename2 ="file2.png"

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

# 比較並顯示差異影像
diff_imgs1_2 = cv2.absdiff(img1, img2)
cv2.imshow('Difference', diff_imgs1_2)
cv2.waitKey(2000)

# 複製一份影像副本，偵測及標示瞬變
temp = diff_imgs1_2.copy()
transient1, transient_loc1 = find_transient(img1, temp, PAD)

# 畫圓蓋掉最亮點
cv2.circle(temp, transient_loc1, 10, 0, -1)

# 偵測及標示瞬變      
transient2, transient_loc2 = find_transient(img1, temp, PAD)

if transient1 or transient2:
    print('\nTRANSIENT DETECTED between {} and {}\n'.format(filename1, filename2))
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img1, filename1, (10, 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img1, filename2, (10, 55), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    if transient1 and transient2:
        cv2.line(img1, transient_loc1, transient_loc2, (255, 255, 255), 1, lineType=cv2.LINE_AA) # 畫一條連接 2 個瞬變的線
                
    blended = cv2.addWeighted(img1, 1, diff_imgs1_2, 1, 0)
    cv2.imshow('Surveyed', blended)
    cv2.waitKey(2500)

    out_filename = '{}_DECTECTEDtttt.png'.format(filename1)
    cv2.imwrite(out_filename, blended)  # 會覆寫既有檔案！

else:
    print('\nNo transient detected between {} and {}\n'.format(filename1, filename2))
cv2.destroyAllWindows()

