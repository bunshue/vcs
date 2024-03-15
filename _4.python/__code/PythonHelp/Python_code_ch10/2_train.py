import os
import numpy as np
import cv2 as cv

# 設定 Haar 分類器檔案路徑
cascade_path = "C:/Users/Admin/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/"
face_detector = cv.CascadeClassifier(cascade_path +
                                    'haarcascade_frontalface_default.xml')

#train_path = './trainer' # 若使用的是你的臉，請取消註解
train_path = './demming_trainer' # 使用提供的 Demming 臉部影像
image_paths = [os.path.join(train_path, f) for f in os.listdir(train_path)]
images, labels = [], []

# 讀取灰階影像，並顯示使用者 ID、影像的名稱、影像的畫面號碼
for image in image_paths:
    print(image)
    train_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    label = int(os.path.split(image)[-1].split('.')[1])
    name = os.path.split(image)[-1].split('.')[0]
    frame_num = os.path.split(image)[-1].split('.')[2]
    faces = face_detector.detectMultiScale(train_image)
    for (x, y, w, h) in faces:
        images.append(train_image[y:y + h, x:x + w])
        labels.append(label)
        print(f"Preparing training images for {name}.{label}.{frame_num}")
        cv.imshow("Training Image", train_image[y:y + h, x:x + w])
        cv.waitKey(50)

cv.destroyAllWindows()

# 訓練影像
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
recognizer.write('lbph_trainer.yml')
print("Training complete. Exiting...")
