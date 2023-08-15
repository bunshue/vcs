import pickle

def main():
    # Open file for writing binary
    outfile = open("pickle.dat", "wb")
    pickle.dump(45, outfile)
    pickle.dump(56.6, outfile)
    pickle.dump("Programming is fun", outfile)
    pickle.dump([1, 2, 3, 4], outfile)
    outfile.close() # Close the output file

    # Open file for reading binary
    infile = open("pickle.dat", "rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close() # Close the input file

main() # Call the main function

print('------------------------------')  #30個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pickle/pickle_test1.dat'

import pickle
fp = open(filename, "rb")
num = pickle.load(fp)
print(num)
str1 = pickle.load(fp)
print(str1)
lst1 = pickle.load(fp)
print(lst1)
fp.close()

print('------------------------------')  #30個

import pickle
fp = open("pickle_test2.dat", "wb")
pickle.dump(11, fp)
pickle.dump("陳會安", fp)
pickle.dump([1, 2, 3, 4], fp)
fp.close()


print('------------------------------')  #30個




