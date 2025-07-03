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

MIN_NUM_KEYPOINT_MATCHES = 50

def find_best_matches(img1, img2): 
    """傳回關鍵點 list，以及最吻合點的 list""" 
    orb = cv2.ORB_create(nfeatures=100) # 建立 ORB 物件 
    kp1, desc1 = orb.detectAndCompute(img1, mask=None) 
    kp2, desc2 = orb.detectAndCompute(img2, mask=None) 
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance) 
    best_matches = matches[:MIN_NUM_KEYPOINT_MATCHES] 
    return kp1, kp2, best_matches

def QC_best_matches(img_match): 
    """顯示已用線條連接的最吻合關鍵點的影像""" 
    cv2.imshow('Best {} Matches'.format(MIN_NUM_KEYPOINT_MATCHES), img_match) 
    cv2.waitKey(2500) # 讓視窗顯示 2.5 秒
    cv2.destroyAllWindows()
    
def register_image(img1, img2, kp1, kp2, best_matches):
    """傳回將第 1 個影像對準另一個影像後的結果"""
    if len(best_matches) >= MIN_NUM_KEYPOINT_MATCHES:
        src_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
        dst_pts = np.zeros((len(best_matches), 2), dtype=np.float32)
        for i, match in enumerate(best_matches):
            src_pts[i, :] = kp1[match.queryIdx].pt
            dst_pts[i, :] = kp2[match.trainIdx].pt
        h_array, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
        height, width = img2.shape
        img1_warped = cv2.warpPerspective(img1, h_array, (width, height))

        return img1_warped

    else:
        print("WARNING: Number of keypoint matches < {}\n".format
              (MIN_NUM_KEYPOINT_MATCHES))
        return img1

def blink(image_1, image_2, window_name, num_loops):
    """用 2 個影像模擬閃爍比較儀的動作"""
    for _ in range(num_loops):
        cv2.imshow(window_name, image_1)
        cv2.waitKey(200)
        cv2.imshow(window_name, image_2)
        cv2.waitKey(200)
        
filename1 ="data/file1.png"
filename2 ="data/file2.png"

"""做影像對齊和閃爍顯示""" 
img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE) 
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE) 
print("Comparing {} to {}.\n".format(filename1, filename2)) 
kp1, kp2, best_matches = find_best_matches(img1, img2)
img_match = cv2.drawMatches(img1, kp1, img2, kp2, best_matches, outImg=None) 

height, width = img1.shape 
cv2.line(img_match, (width, 0), (width, height), (255, 255, 255), 1) 
QC_best_matches(img_match) # 確認過執行結果滿意，即可標示為註解，不予執行 
img1_registered = register_image(img1, img2, kp1, kp2, best_matches) 

blink(img1, img1_registered, 'Check Registration', num_loops=5) 

cv2.destroyAllWindows()

blink(img1_registered, img2, 'Blink Comparator', num_loops=15)

cv2.destroyAllWindows() 
