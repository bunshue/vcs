import re
import sys

with open('dictionary.txt', 'r') as txt_file_stream:
    file_iter = iter(lambda: txt_file_stream.readline(), '')
    print(type(file_iter))
    cnt = 0
    for word in file_iter:
        word = re.sub(r'\s', '', word)
        print(word)
        cnt += 1
        if cnt > 10:
            break;
        

print('------------------------------------------------------------')	#60個

import re

import PyPDF2

with open('Python_Tricks_encrypted.pdf', 'rb') as pdf_file_stream:
    reader = PyPDF2.PdfReader(pdf_file_stream)
    with open('dictionary.txt', 'r') as txt_file_stream:
        file_iter = iter(lambda: txt_file_stream.readline(), '')
        for word in file_iter:
            word = re.sub(r'\s', '', word)
            if reader.decrypt(word):
                print('取得密碼')
                print(word)
                break


print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


