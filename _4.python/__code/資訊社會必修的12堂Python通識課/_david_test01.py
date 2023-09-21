import os

import sys

print('------------------------------------------------------------')	#60個

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())
    print("-->Next")

filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())
    print("-->Next")

filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(repr(data))

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(data.split())

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.split()
for d in data:
    d.strip()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.replace("(", "")
data = data.replace(")", "")
data = data.replace(",", "")
data = data.replace(".", "")
data = data.replace("“", "")
data = data.replace("”", "")
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
special_chars = list("(),.“”")
for char in special_chars:
    data = data.replace(char, "")
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord('('):None, ord(')'):None, ord('.'):None, ord('“'):None, ord('”'):None})
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
print(data)

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
print(word_freq)

print('------------------------------------------------------------')	#60個

import operator

filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
print(ksvote)

print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)


print('------------------------------------------------------------')	#60個

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

def fixtype(n):
    return int(n.strip().replace(",",""))

filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個
filename = 'ksvote.txt'
with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

