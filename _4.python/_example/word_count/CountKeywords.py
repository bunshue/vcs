import os.path
import sys

print('統計一個python檔案內關鍵字出現的次數')    

keyWords = {"and", "as", "assert", "break", "class", 
            "continue", "def", "del", "elif", "else",
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"}

filename = '../../data/python_word_count1.txt'

infile = open(filename, "r") # Open files for input 
text = infile.read().split() # Read and split words from the file 
count = 0
for word in text:
    if word in keyWords:
        count += 1

print("The number of keywords in", filename, "is", count)



