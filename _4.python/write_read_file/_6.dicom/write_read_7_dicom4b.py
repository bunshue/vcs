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

    return np.piecewise(
        data,
        [
            data <= (level - 0.5 - (window - 1) / 2),
            data > (level - 0.5 + (window - 1) / 2),
        ],
        [
            0,
            255,
            lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0),
        ],
    )


def get_PIL_image(ds):
    """Get Image object from Python Imaging Library(PIL)"""

    if "PixelData" not in ds:
        print("XXXXXXXXXXX")
        raise TypeError(
            "Cannot show image -- DICOM dataset does not have " "pixel data"
        )
    # can only apply LUT if these window info exists
    if ("WindowWidth" not in ds) or ("WindowCenter" not in ds):
        print('1111')
        bits = ds.BitsAllocated
        samples = ds.SamplesPerPixel
        if bits == 8 and samples == 1:
            print('L')
            mode = "L"
        elif bits == 8 and samples == 3:
            print('RGB')
            mode = "RGB"
        elif bits == 16:
            print('16')
            # not sure about this -- PIL source says is 'experimental'
            # and no documentation. Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            print('XXXX')
            raise TypeError(
                "Don't know PIL mode for %d BitsAllocated "
                "and %d SamplesPerPixel" % (bits, samples)
            )

        # PIL size = (width, height)
        size = (ds.Columns, ds.Rows)
        print(size)

        im = PIL.Image.frombuffer(mode, size, ds.PixelData, "raw", mode, 0, 1)

    else:
        print('2222')
        ew = ds["WindowWidth"]
        ec = ds["WindowCenter"]
        print(ew)
        print(ec)
        ww = int(ew.value[0] if ew.VM > 1 else ew.value)
        wc = int(ec.value[0] if ec.VM > 1 else ec.value)
        image = get_LUT_value(ds.pixel_array, ww, wc)

        im = PIL.Image.fromarray(image).convert("L")  # 轉換成灰階圖像

    return im

print("讀取dicom檔案內的圖片")

filename1 = "data/CT_small.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/test.dcm"

ds = pydicom.dcmread(filename3)
dImage = get_PIL_image(ds)

print("有 影像資料")
#dImage.show() #  直接顯示
plt.imshow(dImage, cmap="gray")  # 顯示黑白圖片
plt.title("原始圖像")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



