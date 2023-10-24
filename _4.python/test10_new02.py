import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print("global: ", list(globals().keys()))
print("進入 local:", locals())
print("離開 local:", locals().keys())


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

infile = open('word_count.tst')      #開啟檔案
lines = infile.read().split("\n")    #讀取檔案; 分成不同行

line_count = len(lines)    #以len()取得總行數
word_count = 0     #初始化其他計數器
char_count = 0     #初始化其他計數器

for line in lines:    #一行一行走訪
    words = line.split()    #拆成以字為單元
    word_count += len(words)
    char_count += len(line)    #傳回字元個數

#印出結果
print("File has {0} lines, {1} words, {2} characters".format(     
      line_count, word_count, char_count))                 





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


punct = str.maketrans("",  "", "!.,:;-?")

def clean_line(line):
    """changes case and removes punctuation"""
    # make all one case
    cleaned_line = line.lower()
        
    # remove punctuation
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line

def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    return "\n".join(words) + "\n"
     
    
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
        cleaned_words = get_words(cleaned_line)
        
        # write all words for line
        outfile.write(cleaned_words)

def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}
    for word in moby_words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five 
       entries"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]
    return most_common, least_common

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
        
word_count = count_words(moby_words)
most, least = word_stats(word_count)

print("Most common words:")
for word in most:
    print(word)

print("\nLeast common words:")
for word in least:
    print(word)


print('------------------------------------------------------------')	#60個


