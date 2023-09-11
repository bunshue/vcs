import sys
import os

import jieba

print('------------------------------------------------------------')	#60個

import jieba

filename = "chinnews.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
print(data, "\n")
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
for word in words:
    print(word, "/ ", end="")
    
print('------------------------------------------------------------')	#60個

import jieba

filename = "chinnews.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
word_freq = dict()
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

from collections import Counter
import jieba

filename = "chinnews.txt"
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”（）「」，。、：；！|\n/ ")})
words = jieba.cut(data)
for w, c in Counter(words).most_common():
    if c > 1:
        print(w, c)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個











print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


