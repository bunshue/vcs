import logging
import pydicom

def show_patient_IDs(file_list=None):
    logger = logging.getLogger("show_patient_IDs")
    if file_list is None:
        file_list = []
    for file_name in file_list:
        try:
            logger.info(f'reading: {file_name}')
            f = pydicom.dcmread(file_name)
            logger.info("finished reading")
            patient_id = f.get("PatientID", "No ID")
            print(file_name, "has patient id of", patient_id)
        except Exception:
            print(file_name, "had no patient id for some reason")

print('讀取dicom檔案內的資料')

filename1 = 'C:/______test_files1/__RW/_dicom/CT_small.dcm'
filename2 = 'C:/______test_files1/__RW/_dicom/ims000525.dcm'
filename3 = 'C:/______test_files1/__RW/_dicom/test.dcm'

file_list = []
file_list.append(filename1)
file_list.append(filename2)
file_list.append(filename3)

show_patient_IDs(file_list)








