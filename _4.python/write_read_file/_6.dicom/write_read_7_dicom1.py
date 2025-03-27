"""
# 各種檔案寫讀範例 dicom

MR-SIEMENS-DICOM-WithOverlays.dcm
US1_J2KR.dcm
須將檔案下載在
C:\\Users\\david\\.pydicom\\data\\ 2 dcm files
C:\\Users\\070601\\.pydicom\\data
檔案在
C:\_git\vcs\_4.python\__code\pydicom-data-master\data_store\data

"""

import pydicom
from pydicom.data import get_testdata_file
from pydicom.data import get_testdata_files

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


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個

filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"

print("------------------------------------------------------------")  # 60個

print("讀取dicom資料")

ds = pydicom.dcmread(filename1)
# ds = pydicom.dcmread(filename2, force=True)

"""
#ds全部資訊
print(type(ds))
print(len(ds))
print(ds)
for _ in ds:
    print(_)
"""

print(ds.PatientID)
print(ds.PatientName)
print(ds[0x10, 0x10].value)
print(ds.PatientSex)
print(ds.PatientBirthDate)
print(ds.PatientAge)
print(ds.ImageType)
print(ds.InstanceCreationDate)
print(ds.InstanceCreationTime)
print(ds.StudyDate)
print(ds.ContentDate)
print(ds.StudyTime)
print(ds.ContentTime)
print(ds.AccessionNumber)
print(ds.Modality)
print(ds.StudyDescription)
print(ds.DerivationDescription)
print(ds.SoftwareVersions)
print(ds.NumberOfFrames)
print(ds.Rows)
print(ds.Columns)

ds = pydicom.dcmread(filename1)

data_elements = [
    "PatientID",
    "PatientName",
    "PatientSex",
    "PatientBirthDate",
    "PatientAge",
]

for de in data_elements:
    print(ds.data_element(de))


print("------------------------------------------------------------")  # 60個

filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"


ds = pydicom.dcmread(filename3, force=True)
print(ds.file_meta.MediaStorageSOPClassUID)
print(ds.file_meta.TransferSyntaxUID)

ds = pydicom.dcmread(filename3)
cc = len(ds)
print(cc)

info = {}
# 读取dicom文件
ds = pydicom.read_file(filename3)
# 通过字典关键字来获取图像的数据元信息（当然也可以根据TAG号）
# 这里获取几种常用信息
info["PatientID"] = ds.PatientID  # 患者ID
info["PatientName"] = ds.PatientName  # 患者姓名
info["PatientAge"] = ds.PatientAge  # 患者年龄
info["PatientSex"] = ds.PatientSex  # 患者性别
info["StudyID"] = ds.StudyID  # 检查ID
info["StudyDate"] = ds.StudyDate  # 检查日期
info["StudyTime"] = ds.StudyTime  # 检查时间
info["InstitutionName"] = ds.InstitutionName  # 机构名称
info["Manufacturer"] = ds.Manufacturer  # 设备制造商
info["StudyDescription"] = ds.StudyDescription  # 检查项目描述
print(info)

# 单张影像的读取

# 使用 pydicom.dcmread() 函数进行单张影像的读取,返回一个pydicom.dataset.FileDataset对象.

ds = pydicom.dcmread(filename3)

# 获取图像像素矩阵和大小

img_array = ds.pixel_array  # 获取图像像素矩阵
lens = img_array.shape[0] * img_array.shape[1]  # 获取像素矩阵大小
print(lens)

print(ds.PatientID)
print(ds.StudyDate)
print(ds.Modality)

print("------------------------------------------------------------")  # 60個

ds = pydicom.dcmread(filename3)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
show()

print("------------------------------------------------------------")  # 60個

filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"

print("修改Dicom內的資料")

# Read DICOM file
ds = pydicom.dcmread(filename1)

# 更改 Patient Name 資料
# ds.PhotometricInterpretation = "gary"

# 存檔
filename = "tmp_modify_info1.dcm"
ds.save_as(filename)
print("存檔完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個

print("讀 改寫 dicom 檔案")

ds = pydicom.dcmread(filename1)
ds.PatientName = "anonymous"

# 存檔
filename = "tmp_modify_info2.dcm"
ds.save_as(filename)
print("存檔完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個


def show_patient_IDs(file_list=None):
    if file_list is None:
        file_list = []
    for file_name in file_list:
        try:
            f = pydicom.dcmread(file_name)

            patient_id = f.get("PatientID", "No ID")
            print(file_name, "has patient id of", patient_id)
        except Exception:
            print(file_name, "had no patient id for some reason")


print("讀取dicom檔案內的資料")

filename1 = "data/CT_small.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/test.dcm"

file_list = []
file_list.append(filename1)
file_list.append(filename2)
file_list.append(filename3)

show_patient_IDs(file_list)

print("------------------------------------------------------------")  # 60個

"""
#修改資料內容
ds.data_element('PatientBirthDate').value = '19000101'

# 存檔
ds.save_as('kkkk.dcm')
"""

"""
# 取得 Pydicom 附帶的 DICOM 測試影像路徑
ds = pydicom.dcmread(filename)

print(ds.SeriesNumber)

"""

print("------------------------------------------------------------")  # 60個

print("判斷 dicom 檔案")


def is_dicom(filename):
    with open(filename, "rb") as fp:
        fp.read(128)  # preamble
        return fp.read(4) == b"DICM"


filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"
filename4 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

print(is_dicom(filename1))
print(is_dicom(filename2))
print(is_dicom(filename3))
print(is_dicom(filename4))
print(is_dicom(filename1))

print("------------------------------------------------------------")  # 60個

# 取得pydicom內建的dicom檔案

filename = get_testdata_file("CT_small.dcm")
print(filename)

ds = pydicom.dcmread(filename)
pixel_bytes = ds.PixelData

# 使用 array
arr = ds.pixel_array
print(arr.shape)
print(len(arr))
print(arr)

"""
elem = ds['PatientName']
print(elem)
cc = elem.VR, elem.value
print(cc)

# same
elem = ds[0x0010,0x0010]
print(elem)
cc = elem.VR, elem.value
print(cc)

#cc = ds.SoftwareVersions
print(ds.SoftwareVersions)

del ds.SoftwareVersions  #刪除資料
#print(ds.SoftwareVersions)
"""

t1 = pydicom.tag.Tag(0x00100010)  # all of these are equivalent
t2 = pydicom.tag.Tag(0x10, 0x10)
t3 = pydicom.tag.Tag((0x10, 0x10))
t4 = pydicom.tag.Tag("PatientName")
print(t1)
print(t2)
print(t3)
print(t4)

print("------------------------------------------------------------")  # 60個

filename = get_testdata_file("rtplan.dcm")
ds = pydicom.dcmread(filename)  # plan dataset
ds.PatientName

#'Last^First^mid^pre'
cc = ds.dir("setup")  # get a list of tags with "setup" somewhere in the name
print(cc)
# ['PatientSetupSequence']
cc = ds.PatientSetupSequence[0]
print(cc)

# (0018, 5100) Patient Position                    CS: 'HFS'
# (300a, 0182) Patient Setup Number                IS: '1'
# (300a, 01b2) Setup Technique Description         ST: ''

cc = ds.PatientSetupSequence[0].PatientPosition = "HFP"
print(cc)

ds.save_as("tmp_rtplan2.dcm")

print("------------------------------------------------------------")  # 60個

from typing import List
from typing import Tuple

from pydicom.encaps import encapsulate
from pydicom.encaps import encapsulate_extended
from pydicom.uid import JPEG2000Lossless

path = get_testdata_file("CT_small.dcm")
ds = pydicom.dcmread(path)

ds.file_meta.TransferSyntaxUID = JPEG2000Lossless

ds.is_little_endian = True
ds.is_implicit_VR = False

print("------------------------------------------------------------")  # 60個

# 壓縮
from pydicom.uid import RLELossless

ds = get_testdata_file("CT_small.dcm", read=True)
ds.compress(RLELossless)
ds.save_as("tmp_CT_small_rle.dcm")

"""
# Will set `ds.is_little_endian` and `ds.is_implicit_VR` automatically
ds.compress(RLELossless, encoding_plugin='pylibjpeg')
ds.save_as("tmp_CT_small_rle2.dcm")
"""

# Requires a JPEG 2000 compatible image data handler
ds = get_testdata_file("US1_J2KR.dcm", read=True)
arr = ds.pixel_array
ds.PhotometricInterpretation = "RGB"
ds.compress(RLELossless, arr)
ds.save_as("tmp_US1_RLE.dcm")

print("------------------------------------------------------------")  # 60個

ct_filename = get_testdata_file("CT_small.dcm")
ds = pydicom.dcmread(ct_filename)
print(ds)

print("看 (0009, 1001) 的資料")
cc = ds[0x00091001].value
print(cc)

block = ds.private_block(0x0009, "GEMS_IDEN_01")
cc = block[0x01]
print(cc)
# (0009, 1001) [Full fidelity]                     LO: 'GE_GENESIS_FF'
cc = block[0x01].value
print(cc)
#'GE_GENESIS_FF'

print("設定新值")

block = ds.private_block(0x000B, "Insight Medical Solutions", create=True)
block.add_new(0x01, "SH", "Aries 1.0.5")
print(ds)

# 移除設定
# ds.remove_private_tags()

print("------------------------------------------------------------")  # 60個

filename = get_testdata_files("CT_small.dcm")[0]
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)  # doctest: +ELLIPSIS
show()

print("------------------------------------------------------------")  # 60個

fpath = get_testdata_files("MR-SIEMENS-DICOM-WithOverlays.dcm")[0]
ds = pydicom.dcmread(fpath)
elem = ds[0x6000, 0x3000]  # returns a DataElement
print(elem)
# (6000, 3000) Overlay Data

print("------------------------------------------------------------")  # 60個

fpath = get_testdata_file("waveform_ecg.dcm")
ds = pydicom.dcmread(fpath)
cc = ds.WaveformSequence
print(cc)

# <Sequence, length 2>
multiplex = ds.WaveformSequence[0]
cc = multiplex.NumberOfWaveformChannels
print(cc)
# 12
cc = multiplex.SamplingFrequency
print(cc)
# "1000.0"
cc = multiplex["WaveformData"]
print(cc)
# (5400, 1010) Waveform Data

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import collections


class DicomTree(object):
    def __init__(self, filename):
        self.filename = filename

    def show_tree(self):
        ds = self.dicom_to_dataset(self.filename)
        print(ds)
        array = []
        for data_element in ds:
            array.append(self.data_element_to_dic(data_element))

        dic = self.dataset_to_dic(ds)
        self.display()

    def dicom_to_dataset(self, filename):
        dataset = pydicom.dcmread(filename, force=True)
        return dataset

    def data_element_to_dic(self, data_element):
        # print(data_element)
        dic = collections.OrderedDict()
        if data_element.VR == "SQ":
            print("Get SQ")
            items = collections.OrderedDict()
            dic[data_element.name] = items
            i = 0
            for dataset_item in data_element:
                items["item " + str(i)] = self.dataset_to_dic(dataset_item)
                i += 1
        elif data_element.name != "Pixel Data":
            dic[data_element.name] = data_element.value
        else:
            print("Get Pixel Data")
        # print(dic)
        return dic

    def dataset_to_dic(self, dataset):
        dic = collections.OrderedDict()
        for data_element in dataset:
            dic.update(self.data_element_to_dic(data_element))
        # print(dic)
        return dic

    def display(self):
        print("display 現在的檔案是 :", self.filename)


filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"

dicomTree = DicomTree(filename1)
dicomTree.show_tree()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import PIL.Image


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
        print("1111")
        bits = dataset.BitsAllocated
        samples = dataset.SamplesPerPixel
        if bits == 8 and samples == 1:
            print("L")
            mode = "L"
        elif bits == 8 and samples == 3:
            print("RGB")
            mode = "RGB"
        # not sure about this -- PIL source says is
        # 'experimental' and no documentation.
        elif bits == 16:
            print("16")
            # Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            print("XXXX")
            msg = "Don't know PIL mode for %d BitsAllocated" % (bits)
            msg += " and %d SamplesPerPixel" % (samples)
            raise TypeError(msg)
        size = (dataset.Columns, dataset.Rows)
        print(size)

        im = PIL.Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)
    else:
        print("2222")
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
    print("有 影像資料")
    dImage = loadPIL_LUT(ds)
    if dImage is not None:
        print("有 影像資料")
        # dImage.show() #  直接顯示
        plt.imshow(dImage, cmap="gray")  # 顯示黑白圖片
        plt.title("原始圖像")
        show()
else:
    print("無 影像資料")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import PIL.Image


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
        print("1111")
        bits = ds.BitsAllocated
        samples = ds.SamplesPerPixel
        if bits == 8 and samples == 1:
            print("L")
            mode = "L"
        elif bits == 8 and samples == 3:
            print("RGB")
            mode = "RGB"
        elif bits == 16:
            print("16")
            # not sure about this -- PIL source says is 'experimental'
            # and no documentation. Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            print("XXXX")
            raise TypeError(
                "Don't know PIL mode for %d BitsAllocated "
                "and %d SamplesPerPixel" % (bits, samples)
            )

        # PIL size = (width, height)
        size = (ds.Columns, ds.Rows)
        print(size)

        im = PIL.Image.frombuffer(mode, size, ds.PixelData, "raw", mode, 0, 1)

    else:
        print("2222")
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
# dImage.show() #  直接顯示
plt.imshow(dImage, cmap="gray")  # 顯示黑白圖片
plt.title("原始圖像")
show()

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
