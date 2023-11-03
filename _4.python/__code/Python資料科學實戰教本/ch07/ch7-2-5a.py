import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
outputfile = "Example.out"
np.savetxt(outputfile, a, delimiter=',')
