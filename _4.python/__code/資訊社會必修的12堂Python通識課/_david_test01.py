import os
import sys

print('------------------------------------------------------------')	#60個

print('3333')
filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)

print('------------------------------------------------------------')	#60個

print('4444')
filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

print('5555')
def fixtype(n):
    return int(n.strip().replace(",",""))

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

print('6666')
filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

