import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)

cv2.imshow("Original",o)
cv2.imshow("Canny 1",r1)
cv2.imshow("Canny 2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

