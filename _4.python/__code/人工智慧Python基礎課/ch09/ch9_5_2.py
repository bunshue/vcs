# coding: utf-8
import pickle
fp = open("note.dat", "rb")
num = pickle.load(fp)
print(num)
str1 = pickle.load(fp)
print(str1)
lst1 = pickle.load(fp)
print(lst1)
fp.close()
