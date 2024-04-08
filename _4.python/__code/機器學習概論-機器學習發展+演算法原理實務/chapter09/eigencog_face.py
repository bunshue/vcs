from numpy import *
import sys,os
from pca import *

ef = Eigenfaces() 
ef.dist_metric=ef.distEclud
ef.loadimgs("orl_faces/")
ef.compute()
E = []
X = mat(zeros((10,10304)))
for i in range(16):
	X = ef.Mat[i*10:(i+1)*10,:].copy()
	# X = ef.normalize(X.mean(axis =0),0,255)
	X = X.mean(axis =0)
	imgs = X.reshape(112,92)
	E.append(imgs)
ef.subplot(title="AT&T Eigen Facedatabase", images=E)  
