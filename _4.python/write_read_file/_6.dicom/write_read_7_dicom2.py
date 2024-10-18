# 各種檔案寫讀範例 dicom

import sys
import pydicom
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
        #print(data_element)
        dic = collections.OrderedDict()
        if data_element.VR == "SQ":
            print('Get SQ')
            items = collections.OrderedDict()
            dic[data_element.name] = items
            i = 0
            for dataset_item in data_element:
                items["item " + str(i)] = self.dataset_to_dic(dataset_item)
                i += 1
        elif data_element.name != "Pixel Data":
            dic[data_element.name] = data_element.value
        else:
            print('Get Pixel Data')
        #print(dic)
        return dic

    def dataset_to_dic(self, dataset):
        dic = collections.OrderedDict()
        for data_element in dataset:
            dic.update(self.data_element_to_dic(data_element))
        #print(dic)
        return dic

    def display(self):
        print('display 現在的檔案是 :', self.filename)


filename1 = "data/test.dcm"
filename2 = "data/ims000525.dcm"

dicomTree = DicomTree(filename1)
dicomTree.show_tree()

