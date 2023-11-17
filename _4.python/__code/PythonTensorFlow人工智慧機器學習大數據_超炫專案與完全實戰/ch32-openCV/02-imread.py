import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

img = cv2.imread(filename)

img[0,0]=[0,0,255]
img[70:120, 200:250]=[0,255,0]

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

