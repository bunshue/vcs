import pydicom
import os

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom/CT_small.dcm'

ds = pydicom.dcmread(filename, force=True)
print(ds.file_meta.MediaStorageSOPClassUID)
print(ds.file_meta.TransferSyntaxUID)

