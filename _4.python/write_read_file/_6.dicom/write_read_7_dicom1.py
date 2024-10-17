# 各種檔案寫讀範例 dicom

print("------------------------------------------------------------")  # 60個

import pydicom
from pydicom.data import get_testdata_files
from pydicom.data import get_testdata_file

filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/CT_small.dcm"

ds = pydicom.dcmread(filename1)
# ds = pydicom.dcmread(filename2, force=True)

print(ds)
print(ds.PatientID)
print(ds.PatientName)
print(ds[0x10, 0x10].value)
print(ds.PatientSex)
print(ds.PatientBirthDate)
print(ds.PatientAge)

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

import matplotlib.pyplot as plt
import pydicom

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

# 另存 DICOM 檔案，指定存檔位置
filename = "change_info.dcm"
ds.save_as(filename)

print(f"File {filename1} processed and saved as {filename}")

print("------------------------------------------------------------")  # 60個

import logging
import pydicom


def show_patient_IDs(file_list=None):
    logger = logging.getLogger("show_patient_IDs")
    if file_list is None:
        file_list = []
    for file_name in file_list:
        try:
            logger.info(f"reading: {file_name}")
            f = pydicom.dcmread(file_name)
            logger.info("finished reading")
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

#另存新檔
dataset.save_as('kkkk.dcm')
"""

"""
# 取得 Pydicom 附帶的 DICOM 測試影像路徑
ds = dcmread(filename)

print(ds.SeriesNumber)


"""

print("------------------------------------------------------------")  # 60個


print("讀 改寫 dicom 檔案")
from pydicom.filereader import dcmread

dataset = dcmread(filename1)
dataset.PatientName = "anonymous"
dataset.save_as("file2.dcm")

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
