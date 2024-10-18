import pydicom
import PIL.Image

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

def get_LUT_value(data, window, level):
    """Apply the RGB Look-Up Table for the given
    data and window/level value."""

    win = window
    lvl = level

    e = [0, 255, lambda data: ((data - (lvl - 0.5)) / (win - 1) + 0.5) * (255 - 0)]
    return np.piecewise(
        data,
        [data <= (lvl - 0.5 - (win - 1) / 2), data > (lvl - 0.5 + (win - 1) / 2)],
        e,
    )


# -----------------------------------------------------------
# ImFrame.loadPIL_LUT(dataset)
# Display an image using the Python Imaging Library (PIL)
# -----------------------------------------------------------
def loadPIL_LUT(dataset):
    if "PixelData" not in dataset:
        print("XXXXXXXXXXX")
        raise TypeError("Cannot show image -- DICOM dataset does not have pixel data")

    # can only apply LUT if these values exist
    if ("WindowWidth" not in dataset) or ("WindowCenter" not in dataset):
        print('1111')
        bits = dataset.BitsAllocated
        samples = dataset.SamplesPerPixel
        if bits == 8 and samples == 1:
            print('L')
            mode = "L"
        elif bits == 8 and samples == 3:
            print('RGB')
            mode = "RGB"
        # not sure about this -- PIL source says is
        # 'experimental' and no documentation.
        elif bits == 16:
            print('16')
            # Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            print('XXXX')
            msg = "Don't know PIL mode for %d BitsAllocated" % (bits)
            msg += " and %d SamplesPerPixel" % (samples)
            raise TypeError(msg)
        size = (dataset.Columns, dataset.Rows)
        print(size)

        im = PIL.Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)
    else:
        print('2222')
        ew = dataset["WindowWidth"]
        ec = dataset["WindowCenter"]
        print(ew)
        print(ec)
        ww = int(ew.value[0] if ew.VM > 1 else ew.value)
        wc = int(ec.value[0] if ec.VM > 1 else ec.value)
        image = get_LUT_value(dataset.pixel_array, ww, wc)

        im = PIL.Image.fromarray(image).convert("L")  # 轉換成灰階圖像
    return im


print("讀取dicom檔案內的圖片")

filename1 = "data/CT_small.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/test.dcm"

ds = pydicom.dcmread(filename3)
ds.decode()

if "PixelData" in ds:
    print('有 影像資料')
    dImage = loadPIL_LUT(ds)
    if dImage is not None:
        print("有 影像資料")
        #dImage.show() #  直接顯示
        plt.imshow(dImage, cmap="gray")  # 顯示黑白圖片
        plt.title("原始圖像")
        plt.show()
else:
    print('無 影像資料')

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
