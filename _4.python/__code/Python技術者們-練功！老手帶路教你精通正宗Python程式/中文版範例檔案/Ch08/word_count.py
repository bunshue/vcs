#!/usr/bin/env python3
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
