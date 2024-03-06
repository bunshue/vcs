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

MIN_NUM_KEYPOINT_MATCHES = 150

# 讀取影像
img1 = cv2.imread('montage_left.JPG', cv2.IMREAD_COLOR)
img2 = cv2.imread('montage_right.JPG', cv2.IMREAD_COLOR)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=700) 

# 找出關鍵點和其描述器
kp1, desc1 = orb.detectAndCompute(img1, None)
kp2, desc2 = orb.detectAndCompute(img2, None)

# 用漢明距離進行比對，並匹配影像
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1, desc2, None)

# 進行升序排序
matches = sorted(matches, key=lambda x: x.distance)
          
# 標示吻合的關鍵點
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:MIN_NUM_KEYPOINT_MATCHES],
                       None)

cv2.namedWindow('Matches', cv2.WINDOW_NORMAL) # 命名視窗
img3_resize = cv2.resize(img3, (699, 700)) # 設定視窗大小
cv2.imshow('Matches', img3_resize) # 顯示視窗
cv2.waitKey(7000)  # 視窗停滯 7 秒
cv2.destroyWindow('Matches') # 關閉視窗

# 只留下最吻合的關鍵點
best_matches = matches[:MIN_NUM_KEYPOINT_MATCHES]

if len(best_matches) >= MIN_NUM_KEYPOINT_MATCHES:
    src_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
    dst_pts = np.zeros((len(best_matches), 2), dtype=np.float32)

    for i, match in enumerate(best_matches):
        src_pts[i, :] = kp1[match.queryIdx].pt
        dst_pts[i, :] = kp2[match.trainIdx].pt
        
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

    # 取得 img2 的大小
    height, width = img2.shape
    img1_warped = cv2.warpPerspective(img1, M, (width, height))

    # 覆寫，存檔
    cv2.imwrite('tmp_montage_left_registered.JPG', img1_warped)
    cv2.imwrite('tmp_montage_right_gray.JPG', img2)

else:
    print("\n{}\n".format('WARNING: Number of keypoint matches < 10!'))
