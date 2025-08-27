"""
# 各種檔案寫讀範例 dicom

MR-SIEMENS-DICOM-WithOverlays.dcm
US1_J2KR.dcm
須將檔案下載在
C:\\Users\\david\\.pydicom\\data\\ 2 dcm files
C:\\Users\\070601\\.pydicom\\data
檔案在
D:\_git\vcs\_4.python\__code\pydicom-data-master\data_store\data

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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

from pydicom.data import get_testdata_file

path = get_testdata_file("CT_small.dcm")

ds = pydicom.dcmread(path)
type(ds.PixelData)
# <class 'bytes'>

cc = len(ds.PixelData)
print(cc)
# 32768

cc = ds.PixelData[:2]
print(cc)

# b'\xaf\x00'


arr = ds.pixel_array
cc = arr.shape
print(cc)
# (128, 128)

print(arr)

# Change a patient's ID

from pydicom import dcmread

ds = dcmread(filename3)
# Edit the (0010,0020) 'Patient ID' element
ds.PatientID = "12345678"
ds.save_as("tmp_CT_small.dcm")

# Display the Pixel Data

# With NumPy and matplotlib

import matplotlib.pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file

# The path to a pydicom test dataset
path = get_testdata_file("CT_small.dcm")
ds = dcmread(path)
# `arr` is a numpy.ndarray
arr = ds.pixel_array

plt.imshow(arr, cmap="gray")
plt.show()

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
filename4 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

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

import gc
from pydicom.sequence import Sequence


def _listFiles(files, path):
    # List all files in the directory, recursively.

    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            _listFiles(files, item)
        else:
            files.append(item)


def _splitSerieIfRequired(serie, series):
    # Sort the original list and get local name
    serie._sort()
    L = serie._datasets

    # Init previous slice
    ds1 = L[0]

    # Check whether we can do this
    if "ImagePositionPatient" not in ds1:
        return

    # Initialize a list of new lists
    L2 = [[ds1]]

    # Init slice distance estimate
    distance = 0

    for index in range(1, len(L)):
        # Get current slice
        ds2 = L[index]

        # Get positions
        pos1 = float(ds1.ImagePositionPatient[2])
        pos2 = float(ds2.ImagePositionPatient[2])

        # Get distances
        newDist = abs(pos1 - pos2)
        # deltaDist = abs(firstPos-pos2)

        # If the distance deviates more than 2x from what we've seen,
        # we can agree it's a new dataset.
        if distance and newDist > 2.1 * distance:
            L2.append([])
            distance = 0
        else:
            # Test missing file
            if distance and newDist > 1.5 * distance:
                print(f'Warning: missing file after "{ds1.filename}"')
            distance = newDist

        # Add to last list
        L2[-1].append(ds2)

        # Store previous
        ds1 = ds2

    # Split if we should
    if len(L2) > 1:
        # At what position are we now?
        i = series.index(serie)

        # Create new series
        series2insert = []
        for L in L2:
            newSerie = DicomSeries(serie.suid)
            newSerie._datasets = Sequence(L)
            series2insert.append(newSerie)

        # Insert series and remove self
        for newSerie in reversed(series2insert):
            series.insert(i, newSerie)
        series.remove(serie)


def _getPixelDataFromDataset(ds):
    """Get the pixel data from the given dataset. If the data
    was deferred, make it deferred again, so that memory is
    preserved. Also applies RescaleSlope and RescaleIntercept
    if available."""

    # Get original element
    el = ds["PixelData"]

    # Get data
    data = ds.pixel_array

    # Remove data (mark as deferred)
    ds["PixelData"] = el
    del ds._pixel_array

    # Obtain slope and offset
    slope = 1
    offset = 0
    needFloats = False
    needApplySlopeOffset = False
    if "RescaleSlope" in ds:
        needApplySlopeOffset = True
        slope = ds.RescaleSlope
    if "RescaleIntercept" in ds:
        needApplySlopeOffset = True
        offset = ds.RescaleIntercept
    if int(slope) != slope or int(offset) != offset:
        needFloats = True
    if not needFloats:
        slope, offset = int(slope), int(offset)

    # Apply slope and offset
    if needApplySlopeOffset:
        # Maybe we need to change the datatype?
        if data.dtype in [np.float32, np.float64]:
            pass
        elif needFloats:
            data = data.astype(np.float32)
        else:
            # Determine required range
            minReq, maxReq = data.min(), data.max()
            minReq = min([minReq, minReq * slope + offset, maxReq * slope + offset])
            maxReq = max([maxReq, minReq * slope + offset, maxReq * slope + offset])

            # Determine required datatype from that
            dtype = None
            if minReq < 0:
                # Signed integer type
                maxReq = max([-minReq, maxReq])
                if maxReq < 2**7:
                    dtype = np.int8
                elif maxReq < 2**15:
                    dtype = np.int16
                elif maxReq < 2**31:
                    dtype = np.int32
                else:
                    dtype = np.float32
            else:
                # Unsigned integer type
                if maxReq < 2**8:
                    dtype = np.uint8
                elif maxReq < 2**16:
                    dtype = np.uint16
                elif maxReq < 2**32:
                    dtype = np.uint32
                else:
                    dtype = np.float32

            # Change datatype
            if dtype != data.dtype:
                data = data.astype(dtype)

        # Apply slope and offset
        data *= slope
        data += offset

    # Done
    return data


# The public functions and classes


def find_shape(dataset):
    """Find the expected shape of `dataset.pixel_array` without reading the pixel data.
    The returned shape is a tuple"""
    shape = dataset.Rows, dataset.Columns
    frames = dataset.get("NumberOfFrames", 1) or 1
    if frames > 1:
        shape = (frames,) + shape
    samples = dataset.SamplesPerPixel
    if samples > 1:
        conf = dataset.PlanarConfiguration
        if conf == 0:
            shape += (samples,)
        elif conf == 1:
            shape = (samples,) + shape
        else:
            raise ValueError(f"Invalid Planar Configuration: '{conf}'")
    return shape


def read_files(path, readPixelData=False, force=False):
    print(path)

    # Init list of files
    files = []

    # Obtain data from the given path
    if isinstance(path, str):
        # Make dir nice
        basedir = os.path.abspath(path)
        # Check whether it exists
        if not os.path.isdir(basedir):
            raise ValueError("The given path is not a valid directory.")
        # Find files recursively
        _listFiles(files, basedir)
        print("files a")

    elif isinstance(path, (tuple, list)):
        # Iterate over all elements, which can be files or directories
        for p in path:
            print(p)
            if os.path.isdir(p):
                _listFiles(files, os.path.abspath(p))
                print("files b")
            elif os.path.isfile(p):
                files.append(p)
                print("files c")
            else:
                print(f"Warning, the path '{p}' is not valid.")
    else:
        raise ValueError("The path argument must be a string or list.")

    # Set defer size
    deferSize = 16383  # 128**2-1
    if readPixelData:
        deferSize = None

    # Gather file data and put in DicomSeries
    series = {}
    count = 0
    print("111")
    for filename in files:
        print(filename)

        # Skip DICOMDIR files
        if filename.count("DICOMDIR"):
            print("skip 1")
            continue

        # Try loading dicom ...
        try:
            dcm = pydicom.dcmread(filename, deferSize, force=force)
        except pydicom.filereader.InvalidDicomError:
            print("skip 2")
            continue  # skip non-dicom file
        except Exception as why:
            print("skip 3")
            continue

        # Get SUID and register the file with an existing or new series object
        try:
            suid = dcm.SeriesInstanceUID
            print("suid = ", suid)
        except AttributeError:
            print("skip 4")
            continue  # some other kind of dicom file
        if suid not in series:
            series[suid] = DicomSeries(suid)
        series[suid]._append(dcm)

        count += 1

    print("222")

    # Make a list and sort, so that the order is deterministic
    series = list(series.values())
    series.sort(key=lambda x: x.suid)

    # Split series if necessary
    for serie in reversed([serie for serie in series]):
        _splitSerieIfRequired(serie, series)

    print("333")
    # Finish all series
    series_ = []
    for i in range(len(series)):
        print(i)
        print(series[i])
        try:
            # series[i]._finish()    ????
            series_.append(series[i])
            print("append ", series[i])
        except Exception:
            pass  # Skip serie (probably report-like file without pixels)

    return series_


class DicomSeries(object):
    def __init__(self, suid):
        # Init dataset list and the callback
        self._datasets = Sequence()

        # Init props
        self._suid = suid
        self._info = None
        self._shape = None
        self._spacing = None

    @property
    def suid(self):
        """The Series Instance UID."""
        return self._suid

    @property
    def shape(self):
        """The shape of the data (nz, ny, nx).
        If None, the series contains a single dicom file."""
        return self._shape

    @property
    def spacing(self):
        """The spacing (voxel distances) of the data (dz, dy, dx).
        If None, the series contains a single dicom file."""
        return self._spacing

    @property
    def info(self):
        """A DataSet instance containing the information as present in the
        first dicomfile of this series."""
        return self._info

    @property
    def description(self):
        """A description of the dicom series. Used fields are
        PatientName, shape of the data, SeriesDescription,
        and ImageComments.
        """

        info = self.info

        # If no info available, return simple description
        if info is None:
            return "DicomSeries containing %i images" % len(self._datasets)

        fields = []

        # Give patient name
        if "PatientName" in info:
            fields.append(f"{info.PatientName}")

        # Also add dimensions
        if self.shape:
            tmp = [str(d) for d in self.shape]
            fields.append("x".join(tmp))

        # Try adding more fields
        if "SeriesDescription" in info:
            fields.append("'" + info.SeriesDescription + "'")
        if "ImageComments" in info:
            fields.append("'" + info.ImageComments + "'")

        # Combine
        return " ".join(fields)

    def __repr__(self):
        adr = hex(id(self)).upper()
        data_len = len(self._datasets)
        return "<DicomSeries with %i images at %s>" % (data_len, adr)

    def get_pixel_array(self):
        """get_pixel_array()

        Get (load) the data that this DicomSeries represents, and return
        it as a numpy array. If this serie contains multiple images, the
        resulting array is 3D, otherwise it's 2D.

        If RescaleSlope and RescaleIntercept are present in the dicom info,
        the data is rescaled using these parameters. The data type is chosen
        depending on the range of the (rescaled) data.

        """

        # It's easy if no file or if just a single file
        if len(self._datasets) == 0:
            raise ValueError("Serie does not contain any files.")
        elif len(self._datasets) == 1:
            ds = self._datasets[0]
            slice = _getPixelDataFromDataset(ds)
            return slice

        # Check info
        if self.info is None:
            raise RuntimeError("Cannot return volume if series not finished.")

        # Init data (using what the dicom packaged produces as a reference)
        ds = self._datasets[0]
        slice = _getPixelDataFromDataset(ds)
        vol = np.zeros(self.shape, dtype=slice.dtype)
        vol[0] = slice

        # Fill volume
        ll = self.shape[0]
        for z in range(1, ll):
            ds = self._datasets[z]
            vol[z] = _getPixelDataFromDataset(ds)

        # Finish

        # Done
        gc.collect()
        return vol

    def _append(self, dcm):
        """_append(dcm)
        Append a dicomfile (as a pydicom.dataset.FileDataset) to the series.
        """
        self._datasets.append(dcm)

    def _sort(self):
        """sort()
        Sort the datasets by instance number.
        """
        self._datasets.sort(key=lambda k: k.InstanceNumber)

    def _finish(self):
        """_finish()

        Evaluate the series of dicom files. Together they should make up
        a volumetric dataset. This means the files should meet certain
        conditions. Also some additional information has to be calculated,
        such as the distance between the slices. This method sets the
        attributes for "shape", "spacing" and "info".

        This method checks:
          * that there are no missing files
          * that the dimensions of all images match
          * that the pixel spacing of all images match

        """

        # The datasets list should be sorted by instance number
        L = self._datasets
        if len(L) == 0:
            return
        elif len(L) < 2:
            # Set attributes
            ds = self._datasets[0]
            self._info = self._datasets[0]
            self._shape = find_shape(ds)
            self._spacing = ds.PixelSpacing
            return

        # Get previous
        ds1 = L[0]

        # Init measures to calculate average of
        distance_sum = 0.0

        # Init measures to check (these are in 2D)
        dimensions = find_shape(ds1)

        # row, column
        spacing = ds1.PixelSpacing

        for index in range(len(L)):
            # The first round ds1 and ds2 will be the same, for the
            # distance calculation this does not matter

            # Get current
            ds2 = L[index]

            # Get positions
            pos1 = float(ds1.ImagePositionPatient[2])
            pos2 = float(ds2.ImagePositionPatient[2])

            # Update distance_sum to calculate distance later
            # TODO: use ImageOrientationPatient's normal to calculate this distance
            distance_sum += abs(pos1 - pos2)

            # Test measures
            dimensions2 = find_shape(ds2)
            spacing2 = ds2.PixelSpacing
            if dimensions != dimensions2:
                # We cannot produce a volume if the dimensions match
                raise ValueError("Dimensions of slices does not match.")
            if spacing != spacing2:
                # We can still produce a volume, but we should notify the user
                msg = "Warning: spacing does not match."
                print(msg)
            # Store previous
            ds1 = ds2

        # Create new dataset by making a deep copy of the first
        info = pydicom.dataset.Dataset()
        firstDs = self._datasets[0]
        for key in firstDs.keys():
            if key != "PixelData":
                el = firstDs[key]
                info.add_new(el.tag, el.VR, el.value)

        # Finish calculating average distance
        # (Note that there are len(L)-1 distances)
        distance_mean = distance_sum / (len(L) - 1)

        # Store information that is specific for the series
        self._shape = (len(L),) + dimensions
        spacing.insert(0, distance_mean)
        self._spacing = spacing

        # Store
        self._info = info


foldername = "D:/_git/vcs/_1.data/______test_files1/__RW/_dicom"

adir = foldername
all_series = read_files(adir, False, False)

print("Summary of each series:")
for series in all_series:
    print(series.description)
    arr = series.get_pixel_array()

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
