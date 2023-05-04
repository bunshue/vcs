#各種檔案寫讀範例 dicom

import pydicom
from pydicom.data import get_testdata_files
from pydicom.data import get_testdata_file

filename1 = 'C:/______test_files1/__RW/_dicom/test.dcm'
filename2 = 'C:/______test_files1/__RW/_dicom/ims000525.dcm'
filename3 = 'C:/______test_files1/__RW/_dicom/CT_small.dcm'

ds = pydicom.dcmread(filename1)
#ds = pydicom.dcmread(filename2, force=True)

print(ds)
print(ds.PatientID)
print(ds.PatientName)
print(ds[0x10,0x10].value)
print(ds.PatientSex)
print(ds.PatientBirthDate)
print(ds.PatientAge)

dataset = pydicom.dcmread(filename1)

data_elements = ['PatientID',
                 'PatientName',
                 'PatientSex',
                 'PatientBirthDate',
                 'PatientAge']

for de in data_elements:
    print(dataset.data_element(de))

'''
#修改資料內容
dataset.data_element('PatientBirthDate').value = '19000101'

#另存新檔
dataset.save_as('kkkk.dcm')
'''

'''
# 取得 Pydicom 附帶的 DICOM 測試影像路徑
ds = dcmread(filename)

print(ds.SeriesNumber)
# 更改 Patient Name 資料
ds.PhotometricInterpretation = "gary"

# 另存 DICOM 檔案，指定存檔位置
ds.save_as("de-identification.dcm")



'''



import matplotlib.pyplot as plt
import pydicom

ds = pydicom.dcmread(filename3)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()


