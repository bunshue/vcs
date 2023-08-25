#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組

print('------------------------------------------------------------')	#60個

print("框出照片中的人臉")

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/ming_emperor3.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/dface3.jpg'

# OpenCV 人臉識別分類器
#xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default333.xml'
#face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

#读取待检测的图像
image = cv2.imread(filename)
# 获取xml文件,加载人脸检测器
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
# 色彩转换，转换为灰度图像
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 调用函数detectMultiScale
faces = face_cascade_classifier.detectMultiScale(
    gray,
    scaleFactor = 1.15,
    minNeighbors = 5,
    minSize = (5,5)
)
print(faces)
#打印输出测试结果
print("发现{0}个人脸!".format(len(faces)))
#逐个标记人脸
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2) #矩形标注
    #cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)

#显示结果
cv2.imshow("dect",image)

#保存检测结果
cv2.imwrite("re.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

