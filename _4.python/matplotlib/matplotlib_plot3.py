import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=500, centers=3,
                 n_features=2,
                 random_state=0)

plt.scatter(x[:,0], x[:,1], c=y)
plt.show()

from sklearn.model_selection import cross_val_score

from sklearn.svm import SVC

clf = SVC(gamma='scale')
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
print(scores.mean())

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
print(scores.mean())


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(clf, x, y, cv=5)
print(scores)
print(scores.mean())









