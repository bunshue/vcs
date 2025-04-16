"""
chest_xray

Chest X-Ray Images (Pneumonia)
https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import tensorflow as tf


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler


# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[
        [col for col in df if nunique[col] > 1 and nunique[col] < 50]
    ]  # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(
        num=None,
        figsize=(6 * nGraphPerRow, 8 * nGraphRow),
        dpi=80,
        facecolor="w",
        edgecolor="k",
    )
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if not np.issubdtype(type(columnDf.iloc[0]), np.number):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel("counts")
        plt.xticks(rotation=90)
        plt.title(f"{columnNames[i]} (column {i})")
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    show()


# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna("columns")  # drop columns with NaN
    df = df[
        [col for col in df if df[col].nunique() > 1]
    ]  # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(
            f"No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2"
        )
        return
    corr = df.corr()
    plt.figure(
        num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor="w", edgecolor="k"
    )
    corrMat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f"Correlation Matrix for {filename}")
    show()


# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include=[np.number])  # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna("columns")
    df = df[
        [col for col in df if df[col].nunique() > 1]
    ]  # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if (
        len(columnNames) > 10
    ):  # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(
        df, alpha=0.75, figsize=[plotSize, plotSize], diagonal="kde"
    )
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate(
            "Corr. coef = %.3f" % corrs[i, j],
            (0.8, 0.2),
            xycoords="axes fraction",
            ha="center",
            va="center",
            size=textSize,
        )
    plt.suptitle("Scatter and Density Plot")
    show()


"""
Oh, no! There are no automatic insights available for the file types used in this dataset.
As your Kaggle kerneler bot, I'll keep working to fine-tune my hyper-parameters.
In the meantime, please feel free to try a different dataset.
Conclusion
This concludes your starter analysis!
To go forward from here, click the blue "Edit Notebook" button at the top of the kernel.
This will create a copy of the code and environment for you to edit.
Delete, modify, and add code as you please. Happy Kaggling!
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import cv2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import swish
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils import class_weight


def preprocess_image(image_path, target_size=(128, 128)):
    img = cv2.imread(image_path)  # Read image with OpenCV
    if img is None:
        raise ValueError(f"Image not found: {image_path}")

    # Resize image
    img = cv2.resize(img, target_size)

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    img_eq = cv2.equalizeHist(img_gray)

    # Apply Gaussian blur to reduce noise (kernel size 3x3)
    img_blur = cv2.GaussianBlur(img_eq, (3, 3), 0)

    # Normalize pixel values to the range [0, 1]
    img_norm = img_blur.astype("float32") / 255.0

    # Expand dims to add a channel dimension (H, W, 1)
    img_norm = np.expand_dims(img_norm, axis=-1)
    return img_norm


def load_data(split_paths, target_size=(128, 128)):
    X, y = [], []
    supported_formats = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}

    # Each element in split_paths is a dictionary mapping a category to its folder path.
    for cat_dict in split_paths:
        for category, path in cat_dict.items():
            # Map categories to labels: 'normal' -> 0, 'pneumonia' -> 1
            label = 0 if category.lower() == "normal" else 1
            # List all files in the directory
            for filename in os.listdir(path):
                ext = os.path.splitext(filename)[1].lower()
                if ext in supported_formats:
                    image_path = os.path.join(path, filename)
                    try:
                        img = preprocess_image(image_path, target_size)
                        X.append(img)
                        y.append(label)
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")
    return np.array(X), np.array(y)


folder_path = {
    "train": [
        {"normal": "D:/_git/vcs/_big_files/chest_xray/train/NORMAL/"},
        {"pneumonia": "D:/_git/vcs/_big_files/chest_xray/train/PNEUMONIA/"},
    ],
    "val": [
        {"normal": "D:/_git/vcs/_big_files/chest_xray/val/NORMAL/"},
        {"pneumonia": "D:/_git/vcs/_big_files/chest_xray/val/PNEUMONIA/"},
    ],
    "test": [
        {"normal": "D:/_git/vcs/_big_files/chest_xray/test/NORMAL/"},
        {"pneumonia": "D:/_git/vcs/_big_files/chest_xray/test/PNEUMONIA/"},
    ],
}

print("Loading training data...")
X_train, y_train = load_data(folder_path["train"], target_size=(128, 128))
print("Loading validation data...")
X_val, y_val = load_data(folder_path["val"], target_size=(128, 128))
print("Loading test data...")
X_test, y_test = load_data(folder_path["test"], target_size=(128, 128))

print(f"Train set: {X_train.shape[0]} images")
print(f"Validation set: {X_val.shape[0]} images")
print(f"Test set: {X_test.shape[0]} images")

input_shape = X_train.shape[1:]

model = Sequential(
    [
        Conv2D(32, (3, 3), activation="relu", padding="same", input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="tanh", padding="same"),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation="relu", padding="same"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation=swish),  # Using swish activation
        Dropout(0.5),
        Dense(1, activation="sigmoid"),  # Sigmoid for binary classification
    ]
)

# Use mini-batch gradient descent via SGD optimizer
optimizer = SGD(learning_rate=0.01, momentum=0.9)

model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"])

print("檢視模型架構")
model.summary()  # 檢視模型架構

class_weights_arr = class_weight.compute_class_weight(
    class_weight="balanced", classes=np.unique(y_train), y=y_train
)
class_weights = dict(enumerate(class_weights_arr))
print("Class weights:", class_weights)
# Class weights: {0: 1.9448173005219984, 1: 0.6730322580645162}

""" 以下很久
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=32,
    class_weight=class_weights
)

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test loss: {test_loss:.4f}, Test accuracy: {test_acc:.4f}")

y_pred = model.predict(X_test)
# Convert probabilities to binary class labels (threshold = 0.5)
y_pred_class = (y_pred > 0.5).astype("int32")

print("Classification Report:")
print(classification_report(y_test, y_pred_class, target_names=["normal", "pneumonia"]))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_class))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import PIL

image = PIL.Image.open(
    "D:/_git/vcs/_big_files/chest_xray/train/PNEUMONIA/person1000_bacteria_2931.jpeg"
)
plt.imshow(image, cmap="gray")
show()

image_normal = PIL.Image.open(
    "D:/_git/vcs/_big_files/chest_xray/train/NORMAL/IM-0115-0001.jpeg"
)
plt.imshow(image_normal, cmap="gray")
show()

from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增

training_dir = "D:/_git/vcs/_big_files/chest_xray/train"
training_generator = ImageDataGenerator(
    rescale=1 / 255,
    rotation_range=30,  # 旋轉角度 +-30度
    width_shift_range=0.2,  # 平移範圍 W 20%
    height_shift_range=0.2,  # 平移範圍 H 20%
    shear_range=0.2,  # Shear effect
    zoom_range=0.2,  # Zoom in/out
    horizontal_flip=True,  # 左右翻轉
    fill_mode="nearest",  # Fill in missing pixels
)
data_train = training_generator.flow_from_directory(
    training_dir, target_size=(120, 120), batch_size=32, class_mode="binary"
)

# Found 5216 images belonging to 2 classes.

valid_dir = "D:/_git/vcs/_big_files/chest_xray/val"
validation_generator = ImageDataGenerator(
    rescale=1 / 255,
    rotation_range=30,  # Rotate images up to 30 degrees
    width_shift_range=0.2,  # Shift width by 20%
    height_shift_range=0.2,  # Shift height by 20%
    shear_range=0.2,  # Shear effect
    zoom_range=0.2,  # Zoom in/out
    horizontal_flip=True,  # Flip images horizontally
    fill_mode="nearest",  # Fill in missing pixels
)
data_valid = validation_generator.flow_from_directory(
    valid_dir, target_size=(120, 120), batch_size=8, class_mode="binary"
)

# Found 16 images belonging to 2 classes.

test_dir = "D:/_git/vcs/_big_files/chest_xray/test"
test_generator = ImageDataGenerator(rescale=1 / 255)
data_test = test_generator.flow_from_directory(
    test_dir, target_size=(120, 120), batch_size=32, class_mode="binary"
)

# Found 624 images belonging to 2 classes.

# CNN

model_cnn = tf.keras.Sequential(
    [
        tf.keras.layers.Conv2D(
            32, (3, 3), input_shape=(120, 120, 3), activation="relu"
        ),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(256, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)

print("檢視模型架構")
model_cnn.summary()  # 檢視模型架構

model_cnn.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

""" 以下很久
history = model_cnn.fit(data_train, epochs=10, validation_data=data_valid)

model_cnn.evaluate(data_test)

prediction = model_cnn.predict(data_test)
print(prediction)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
#Train and validation accuracy
plt.plot(epochs, acc, 'b', label='Training accurarcy')
plt.plot(epochs, val_acc, 'r', label='Validation accurarcy')
plt.title('Training and Validation accurarcy')
plt.legend()
show()

#Train and validation loss
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and Validation loss')
plt.legend()
show()

#I tried to minimize the gap between training and testing accuracy
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
