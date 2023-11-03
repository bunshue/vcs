import numpy as np 

a = np.arange(10)
outputfile = "Example.npy"
with open(outputfile, 'wb') as fp:
    np.save(fp, a)
