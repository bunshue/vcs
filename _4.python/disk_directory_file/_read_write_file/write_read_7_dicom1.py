#各種檔案寫讀範例 dicom

import pydicom
from pydicom.data import get_testdata_files
from pydicom.data import get_testdata_file

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/test.dcm'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/ims000525.dcm'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/CT_small.dcm'

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


print('----------------------------------------------------------------------')	#70個

import matplotlib.pyplot as plt
import pydicom

ds = pydicom.dcmread(filename3)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.show()

print('----------------------------------------------------------------------')	#70個



print('----------------------------------------------------------------------')	#70個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/test.dcm'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/ims000525.dcm'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/CT_small.dcm'

print('修改Dicom內的資料')

# Read DICOM file
ds = pydicom.dcmread(filename1)

# 更改 Patient Name 資料
#ds.PhotometricInterpretation = "gary"

# 另存 DICOM 檔案，指定存檔位置
filename = 'change_info.dcm'
ds.save_as(filename)

print(f"File {filename1} processed and saved as {filename}")
       



print('----------------------------------------------------------------------')	#70個








print('----------------------------------------------------------------------')	#70個



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


'''

print('----------------------------------------------------------------------')	#70個




print('讀 改寫 dicom 檔案')
from pydicom.filereader import dcmread
dataset = dcmread(filename1)
dataset.PatientName = 'anonymous'
dataset.save_as("file2.dcm")

print('----------------------------------------------------------------------')	#70個



print('判斷 dicom 檔案')
def is_dicom(filename):
    with open(filename, 'rb') as fp:
        fp.read(128)  # preamble
        return fp.read(4) == b"DICM"


filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/test.dcm'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/ims000525.dcm'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/CT_small.dcm'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(is_dicom(filename1))
print(is_dicom(filename2))
print(is_dicom(filename3))
print(is_dicom(filename4))
print(is_dicom(filename1))




print('----------------------------------------------------------------------')	#70個



