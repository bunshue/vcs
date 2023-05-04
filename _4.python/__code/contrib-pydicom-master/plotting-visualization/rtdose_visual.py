import pydicom
import matplotlib.pyplot as plt
import os
import numpy as np
import gzip
import sys

#path = 'C:/______test_files1/__RW/_dicom'
path = 'C:/______test_files1/__RW/_dicom/ims000525.dcm'
global cMin, cMax, cMap
cMap = "inferno"
cMin = None
cMax = None

# This would print all the files and directories
if __name__ == "__main__":

    if os.path.isdir(path):
        print('11111')
        dirs = os.listdir(path)
        for file in dirs:
            if not os.path.isdir(path + "/" + file):
                ds = pydicom.dcmread(path + "/" + file, force=True)
                if (
                    ds.file_meta.MediaStorageSOPClassUID
                    == "1.2.840.10008.5.1.4.1.1.481.2"
                ):
                    print("The RTDose file is named:", file)
                    print(".")
                    print(".")
                    print(".")
                    break

    else:
        print('22222')
        cwd = os.getcwd()

        if not os.path.isfile(cwd + "/" + path):
            print("Input file not found")
            sys.exit()

        if path.endswith(".gz"):
            with gzip.open(path, "rb") as f_in:
                ds = pydicom.dcmread(f_in, force=True)
        else:
            ds = pydicom.dcmread(cwd + "/" + path, force=True)

        if ds.file_meta.MediaStorageSOPClassUID == "1.2.840.10008.5.1.4.1.1.481.2":
            print("The RTDose file is named:", path)
            print(".")
            print(".")
            print(".")
        else:
            print("The file is not in RTDose format ")
            sys.exit()
        if not hasattr(ds.file_meta, "TransferSyntaxUID"):
            ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian

