import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('chardet：檔案編碼格式')

import chardet

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/2.utf_to_ascii.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/3.ascii_to_unicode.txt'
filename4 = '__code/PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰/ch03/mycode.py'
filename5 = '__code/PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰/ch07/05-Dictionaries1.py'
filename6 = '__code/PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰/ch17_numpy/06-Datatype.py'

files = [filename4, filename5, filename6]
for f in files:
    text = open(f, 'rb').read()
    codetype = chardet.detect(text)
    print('{}\n編碼格式：{}'.format(f, codetype))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


