filename = 'C:/_git/vcs/_1.data/______test_files1/__RW\_txt/python_password2.txt'

import ast

data = dict()
with open(filename,'r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   data = ast.literal_eval(filedata)
print(type(data),data)


print('------------------------------------------------------------')	#60個






import os
import sys

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

def fixtype(n):
    return int(n.strip().replace(",",""))

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

