import cv2

filename1 = 'box.png'
filename2 = 'box_in_scene.png'

img1 = cv2.imread(filename1, -1)
img2 = cv2.imread(filename2, -1)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x:x.distance)
img3 = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:10],
    outImg = None,
    flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
)

width, height, channel = img3.shape
ratio = float(width) / float(height)
img3 = cv2.resize(img3, (1024, int(1024 * ratio)))

cv2.imshow('image', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
