import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print('------------------------------------------------------------')	#60個

#怎麼選最好參數、model？
#製造像真的一様的數據

#from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples = 500,
                  centers = 3,
                  n_features = 2,
                  random_state = 0)
plt.scatter(x[:, 0], x[:, 1], c = y)
plt.show()

print('------------------------------------------------------------')	#60個

#Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

clf = SVC()
#clf = SVC(gamma = 'scale')

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

#試用 Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

#試用 Random Forest

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 100)

#看一下五次的成績
scores = cross_val_score(clf, x, y, cv = 5)
print(scores)

#很快的算一下平均
print(scores.mean())

print('------------------------------------------------------------')	#60個

