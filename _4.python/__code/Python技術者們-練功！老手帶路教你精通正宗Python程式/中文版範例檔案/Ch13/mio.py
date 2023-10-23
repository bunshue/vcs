"""mio 模組: 包含函式 capture_output, restore_output,
   print_file, and clear_file """

import sys
_file_object = None

def capture_output(file="capture_file.txt"):
    """capture_output(file='capture_file.txt'): 
       將標準輸出重導至檔案."""
    global _file_object
    print("output will be sent to file: {0}".format(file))
    print("restore to normal by calling 'mio.restore_output()'")
    _file_object = open(file, 'w')
    sys.stdout = _file_object

def restore_output():
    """restore_output():
       將標準輸出回復為原始值，並且將之前重導時寫入的檔案關閉)"""
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()
    print("standard output has been restored back to normal")

def print_file(file="capture_file.txt"):
    """print_file(file="capture_file.txt"): 
       將之前重導時寫入的檔案內容列印到標準輸出"""
    f = open(file, 'r')
    print(f.read())
    f.close()

def clear_file(file="capture_file.txt"):
    """clear_file(file="capture_file.txt"): 
       將之前重導時寫入的檔案清空"""
    f = open(file, 'w')
    f.close()
