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

print("------------------------------------------------------------")  # 60個

filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"

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

dataset = pydicom.dcmread(filename1)

data_elements = [
    "PatientID",
    "PatientName",
    "PatientSex",
    "PatientBirthDate",
    "PatientAge",
]

for de in data_elements:
    print(dataset.data_element(de))

print("------------------------------------------------------------")  # 60個

ds = pydicom.dcmread(filename3)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()

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

from pydicom.filereader import dcmread

dataset = dcmread(filename1)
dataset.PatientName = "anonymous"

# 存檔
filename = "tmp_modify_info2.dcm"
dataset.save_as(filename)
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
dataset.data_element('PatientBirthDate').value = '19000101'

# 存檔
dataset.save_as('kkkk.dcm')
"""

"""
# 取得 Pydicom 附帶的 DICOM 測試影像路徑
ds = dcmread(filename)

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

#取得pydicom內建的dicom檔案

filename = get_testdata_file("CT_small.dcm")
print(filename)

ds = pydicom.dcmread(filename)
pixel_bytes = ds.PixelData

#使用 array
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

from pydicom.tag import Tag

t1 = Tag(0x00100010) # all of these are equivalent
t2 = Tag(0x10,0x10)
t3 = Tag((0x10, 0x10))
t4 = Tag("PatientName")
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
#['PatientSetupSequence']
cc = ds.PatientSetupSequence[0]
print(cc)

#(0018, 5100) Patient Position                    CS: 'HFS'
#(300a, 0182) Patient Setup Number                IS: '1'
#(300a, 01b2) Setup Technique Description         ST: ''

cc = ds.PatientSetupSequence[0].PatientPosition = "HFP"
print(cc)

ds.save_as("tmp_rtplan2.dcm")

print("------------------------------------------------------------")  # 60個

from typing import List, Tuple

from pydicom import dcmread
from pydicom.encaps import encapsulate, encapsulate_extended
from pydicom.uid import JPEG2000Lossless

path = get_testdata_file("CT_small.dcm")
ds = dcmread(path)

ds.file_meta.TransferSyntaxUID = JPEG2000Lossless

ds.is_little_endian = True
ds.is_implicit_VR = False

print("------------------------------------------------------------")  # 60個

#壓縮
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
ds.PhotometricInterpretation = 'RGB'
ds.compress(RLELossless, arr)
ds.save_as("tmp_US1_RLE.dcm")

print("------------------------------------------------------------")  # 60個

from pydicom import dcmread

ct_filename = get_testdata_file("CT_small.dcm")
ds = dcmread(ct_filename)
print(ds)

print("看 (0009, 1001) 的資料")
cc = ds[0x00091001].value
print(cc)


block = ds.private_block(0x0009, 'GEMS_IDEN_01')
cc = block[0x01]
print(cc)
#(0009, 1001) [Full fidelity]                     LO: 'GE_GENESIS_FF'
cc = block[0x01].value
print(cc)
#'GE_GENESIS_FF'

print('設定新值')

block = ds.private_block(0x000b, "Insight Medical Solutions", create=True)
block.add_new(0x01, "SH", "Aries 1.0.5")
print(ds)

#移除設定
#ds.remove_private_tags()

print("------------------------------------------------------------")  # 60個

filename = get_testdata_files("CT_small.dcm")[0]
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) # doctest: +ELLIPSIS
plt.show()

print("------------------------------------------------------------")  # 60個

fpath = get_testdata_files("MR-SIEMENS-DICOM-WithOverlays.dcm")[0]
ds = pydicom.dcmread(fpath)
elem = ds[0x6000, 0x3000]  # returns a DataElement
print(elem)
#(6000, 3000) Overlay Data

print("------------------------------------------------------------")  # 60個

from pydicom import dcmread

fpath = get_testdata_file("waveform_ecg.dcm")
ds = dcmread(fpath)
cc = ds.WaveformSequence
print(cc)

#<Sequence, length 2>
multiplex = ds.WaveformSequence[0]
cc = multiplex.NumberOfWaveformChannels
print(cc)
#12
cc = multiplex.SamplingFrequency
print(cc)
#"1000.0"
cc = multiplex['WaveformData']
print(cc)
#(5400, 1010) Waveform Data

print("------------------------------------------------------------")  # 60個


