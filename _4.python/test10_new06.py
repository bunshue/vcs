import os

testfiles = os.listdir('C:/______test_files/__RW/_dicom')

#簡檔名
testfiles = [x for x in testfiles if x.endswith('dcm')]

#全檔名
testfiles = [os.path.join('C:/______test_files/__RW/_dicom', x) for x in testfiles]

for dcmfile in testfiles:
    print(dcmfile)

