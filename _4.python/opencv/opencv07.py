import cv2

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2a = 'C:/_git/vcs/_1.data/______test_files2/picture1a.jpg'
filename2b = 'C:/_git/vcs/_1.data/______test_files2/picture1b.jpg'

cv2.namedWindow("ShowImage1")
cv2.namedWindow("ShowImage2")

image1 = cv2.imread(filename1)
#image1 = cv2.imread(filename1, 1)
image2 = cv2.imread(filename1, 0)  #0:黑白 1:彩色

cv2.imshow("ShowImage1", image1) 
cv2.imshow("ShowImage2", image2)

cv2.imwrite(filename2a, image1)
cv2.imwrite(filename2b, image2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])


cv2.waitKey(0)
#cv2.waitKey(10000)
cv2.destroyAllWindows()


