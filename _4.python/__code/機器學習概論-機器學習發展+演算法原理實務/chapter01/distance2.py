import numpy as np
import scipy.spatial.distance as dist

Vector1 = np.array([1,1,0,1,0,1,0,0,1])
Vector2 = np.array([0,1,1,0,0,0,1,1,1])
matV = np.mat([Vector1 ,Vector2])
print(matV)
print("dist.jaccard:",dist.pdist(matV,'jaccard'))

