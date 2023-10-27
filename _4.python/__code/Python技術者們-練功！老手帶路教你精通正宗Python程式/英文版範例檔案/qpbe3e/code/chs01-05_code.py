import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


# Python version.
def pairwise_sum(list1, list2): 
    result = [] 
    for i in range(len(list1)): 
        result.append(list1[i] + list2[i]) 
    return result

print('------------------------------------------------------------')	#60個


import http.server
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler)



print('------------------------------------------------------------')	#60個

"""wo module. Contains function: words_occur()"""   #1

# interface functions                #2
def words_occur():
    """words_occur() - count the occurrences of words in a file."""
    # Prompt user for the name of the file to use.
    file_name = 'exception.py'
    # Open the file, read it and store its words in a list.
    f = open(file_name, 'r')
    word_list = f.read().split()  #3
    f.close()
    # Count the number of occurrences of each word in the file.
    occurs_dict = {}
    for word in word_list:
        # increment the occurrences count for this word
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Print out the results.
    print("File %s has %d words (%d are unique)" % (file_name, len(word_list), len(occurs_dict)))
    print(occurs_dict)


words_occur()



print('------------------------------------------------------------')	#60個


class EmptyFileError(Exception):
    pass
filenames = ["myfile1","nonExistent", "emptyFile", "myfile2"]
for file in filenames:
    try:
        f = open(file,'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % (file))
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline())) 
    finally:
        print("Done processing", file)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



