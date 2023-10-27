import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

"""mymath - our example math module"""
pi = 3.14159
def area(r):
    """area(r): return the area of a circle with radius r."""
    global pi
    return(pi * r * r) 



print('------------------------------------------------------------')	#60個


# open the file
infile = open('word_count.txt')
# read the file and split into lines
lines = infile.read().split("\n")

# get number of lines with len() function
line_count = len(lines)
# initialize other counts
word_count = 0
char_count = 0

# iterate through the lines
for line in lines:
    # split into words
    words = line.split()
    word_count += len(words)
    # len() function returns characters when used on a string
    char_count += len(line)

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count,
                                                             word_count, char_count))
    



print('------------------------------------------------------------')	#60個


"""wo module. Contains function: words_occur()""" 
# interface functions
def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Prompt user for the name of the file to use.
    file_name = input("Enter the name of the file: ")
    # Open the file, read it and store its words in a list.
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()
    # Count the number of occurrences of each word in the file.
    occurs_dict = {}
    for word in word_list:
        # increment the occurrences count for this word
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Print out the results.
    print("File %s has %d words (%d are unique)" \
      % ( file_name, len(word_list), len(occurs_dict) ))
    print(occurs_dict)

words_occur()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



