import numpy as np 

outputfile = "Example.npy"
with open(outputfile, 'rb') as fp:
    a = np.load(fp)
print(a)
