import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import glob, cv2


def show_images_labels_predictions(images, labels, predictions, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        if len(predictions) > 0:  # 有傳入預測資料
            title = "ai = " + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
            title += "\nlabel = " + str(labels[start_id])
        else:  # 沒有傳入預測資料
            title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    plt.show()


files = glob.glob("imagedata\*.jpg")  # 建立測試資料
test_feature = []
test_label = []
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    test_feature.append(img)
    label = file[10:11]  # "imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))

test_feature = np.array(test_feature)  # 串列轉為矩陣
test_label = np.array(test_label)  # 串列轉為矩陣
test_feature_vector = test_feature.reshape(len(test_feature), 28, 28, 1).astype(
    "float32"
)
test_feature_normalize = test_feature_vector / 255
model = load_model("Mnist_cnn_model.h5")

# y_pred = model.predict_classes(test_feature_normalize) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(test_feature_normalize)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

show_images_labels_predictions(
    test_feature, test_label, y_pred, 0, len(test_feature)
)
