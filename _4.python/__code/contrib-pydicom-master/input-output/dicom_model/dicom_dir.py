import argparse
import fnmatch
import os
import sys
from pprint import pformat

import pydicom
from pydicom.misc import is_dicom

from patient import Patient


def find_dicom_files(directory, pattern="*", directory_exclude_pattern='', recursive=True):

    for root, dirs, files in os.walk(directory):
        if not recursive:
            dirs = []
        for x in dirs:
            if fnmatch.fnmatch(x, directory_exclude_pattern):
                try:
                    dirs.remove(x)
                except Exception:
                    pass
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                if is_dicom(filename):
                    yield filename

foldername = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom'
patients = list()
for x in find_dicom_files(directory=foldername, pattern="*.dcm", directory_exclude_pattern=".*"):
    print('檔案 : ', x)
    f = pydicom.dcmread(x)
    for p in patients:
        print('已有資料')
        try:
            p.add_dataset(f)
        except Exception as e:
            print('無法添入資料')
            pass
        else:
            print('其他錯誤')
            break
    else:
        print("新增資料")
        patients.append(Patient(dicom_dataset = f))
            
print("Found", len(patients), "patients")
for x in patients:
    print(repr(x))
    print("\n")

