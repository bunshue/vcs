import cv2

cv2.namedWindow("ShowImage")
image = cv2.imread("media\\img01.jpg", 0)
cv2.imshow("ShowImage", image)
cv2.imwrite("media\\img01copy1.jpg", image)
cv2.imwrite("media\\img01copy2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

cv2.waitKey(0)
cv2.destroyWindow("ShowImage")

