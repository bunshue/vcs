import cv2

filename1 = 'box.png'
filename2 = 'box_in_scene.png'

'''
img1 = cv2.imread(filename1, -1)
img2 = cv2.imread(filename2, -1)
'''

img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

#feature = cv2.xfeatures2d.SIFT_create()
feature = cv2.xfeatures2d.SURF_create()
kp1, des1 = feature.detectAndCompute(img1, None)
kp2, des2 = feature.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.55 * n.distance:
        good.append(m)
print('Matching points :{}'.format(len(good)))
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], outImg=None, 
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

width, height, channel = img3.shape
ratio = float(width) / float(height)
img3 = cv2.resize(img3, (1024, int(1024 * ratio)))

cv2.imshow('video', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
