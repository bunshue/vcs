import sys

import pandas as pd


print('------------------------------------------------------------')	#60個

#製作訓練數據

from PIL import Image
img = Image.open('label.png')
print(img.mode)

#01   Img_8 = img.convert("P")
#02   Img_8.save('xxx.png')


print('------------------------------------------------------------')	#60個

#訓練模型和預測

# pip install mrcnn

""" 一些 fail

import os
import sys
#sys.path.append('../../Mask_RCNN/') # 加入Mask_RCNN源碼所在目錄
import cv2
from mrcnn.config import Config
from mrcnn import model as modellib,utils
import numpy as np
from PIL import Image
import yaml
import warnings
warnings.filterwarnings('ignore')


ROOT_DIR = os.getcwd() #當前目錄
MODEL_DIR = os.path.join(ROOT_DIR, "models")
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# 從網上下載訓練好的基礎模型
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# 配置項
class ShapesConfig(Config):
    NAME = "shapes" # 命名
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 1  # 背景一類，香蕉一類，共兩類
    IMAGE_MIN_DIM = 320
    IMAGE_MAX_DIM = 384
    RPN_ANCHOR_SCALES = (8 * 6, 16 * 6, 32 * 6, 64 * 6, 128 * 6)
    TRAIN_ROIS_PER_IMAGE = 100
    STEPS_PER_EPOCH = 100
    VALIDATION_STEPS = 50

config = ShapesConfig()
config.display() # 顯示配置項


print('------------------------------------------------------------')	#60個

#構建數據集


class FruitDataset(utils.Dataset):
    def get_obj_index(self, image):
        n = np.max(image)
        return n

    # 獲取標籤
    def from_yaml_get_class(self, image_id):
        info = self.image_info[image_id]
        with open(info['yaml_path']) as f:
            temp = yaml.load(f.read())
            labels = temp['label_names']
            del labels[0]
        return labels

    # 填充mask
    def draw_mask(self, num_obj, mask, image,image_id):
        info = self.image_info[image_id]
        for index in range(num_obj):
            for i in range(info['width']):
                for j in range(info['height']):
                    at_pixel = image.getpixel((i, j))
                    if at_pixel == index + 1:
                        mask[j, i, index] = 1
        return mask

    # 讀入訓練圖片及其配置文件
    def load_shapes(self, count, img_folder, mask_folder, imglist, dataset_root_path):
        self.add_class("shapes", 1, "banana") # 自定義標籤 
        print(count, len(imglist))
        for i in range(count):
            filestr = imglist[i].split(".")[0]
            mask_path = mask_folder + "/" + filestr + "_json.png"
            yaml_path = dataset_root_path + "labelme_json/" + filestr + "_json/info.yaml"
            cv_img = cv2.imread(dataset_root_path + "labelme_json/" +
                    filestr + "_json/img.png")
            self.add_image("shapes", image_id=i, path=img_folder + "/" + imglist[i],
                    width=cv_img.shape[1], height=cv_img.shape[0], 
                    mask_path=mask_path, yaml_path=yaml_path)

    # 讀取標籤和配置 
    def load_mask(self, image_id):
        info = self.image_info[image_id]
        count = 1  # number of object
        img = Image.open(info['mask_path'])
        num_obj = self.get_obj_index(img)
        mask = np.zeros([info['height'], info['width'], num_obj], dtype=np.uint8)
        mask = self.draw_mask(num_obj, mask, img,image_id)
        occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)
        for i in range(count - 2, -1, -1):
            mask[:, :, i] = mask[:, :, i] * occlusion
            occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))
        labels = []
        labels = self.from_yaml_get_class(image_id)
        labels_form = []
        for i in range(len(labels)):
            if labels[i].find("banana") != -1: # 自定義標籤
                labels_form.append("banana")
        class_ids = np.array([self.class_names.index(s) for s in labels_form])
        return mask, class_ids.astype(np.int32)

print('------------------------------------------------------------')	#60個

#模型訓練

#基礎設置
dataset_root_path="data/" # 數據目錄下只有一個圖片權作爲demo使用，訓練時需要加入更多文件
img_folder = dataset_root_path + "pic" # 基本圖片目錄
mask_folder = dataset_root_path + "cv2_mask" # mask圖片目錄
imglist = os.listdir(img_folder)

# 構造訓練集
dataset_train = FruitDataset()
dataset_train.load_shapes(len(imglist), img_folder, mask_folder, imglist, dataset_root_path)
dataset_train.prepare()

# 構造驗證集
dataset_val = FruitDataset()
dataset_val.load_shapes(7, img_folder, mask_folder, imglist, dataset_root_path)
dataset_val.prepare()

# 建立模型
model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=MODEL_DIR)

# 定義模式
model.load_weights(COCO_MODEL_PATH, by_name=True,
                       exclude=["mrcnn_class_logits", "mrcnn_bbox_fc",
                                "mrcnn_bbox", "mrcnn_mask"])

# 模型訓練
model.train(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE / 10,
            epochs=30,
            layers="all")

print('------------------------------------------------------------')	#60個

#用模型分割圖片

import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
import skimage.io
from mrcnn.config import Config
import mrcnn.model as modellib
from mrcnn import visualize

ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)
MODEL_DIR = os.path.join(ROOT_DIR, "models")

# 配置，同train
class ShapesConfig(Config):
    NAME = "shapes"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 1
    IMAGE_MIN_DIM = 320
    IMAGE_MAX_DIM = 384
    RPN_ANCHOR_SCALES = (8 * 6, 16 * 6, 32 * 6, 64 * 6, 128 * 6)
    TRAIN_ROIS_PER_IMAGE =100
    STEPS_PER_EPOCH = 100
    VALIDATION_STEPS = 50

config = ShapesConfig()
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
model.load_weights('models/shapes20190620T1915/mask_rcnn_shapes_0029.h5', 
             by_name=True) # 注意換成讀者生成模型的路徑

class_names = ['BG', 'banana']
image = skimage.io.imread('banana.jpg') # 注意配換成需要識別的圖片路徑

results = model.detect([image], verbose=1)
r = results[0]
# 畫圖
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            class_names, r['scores'])

"""

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


