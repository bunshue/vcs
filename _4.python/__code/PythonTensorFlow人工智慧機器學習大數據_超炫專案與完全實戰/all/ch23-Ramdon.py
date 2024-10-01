from sklearn.ensemble import RandomForestClassifier

import numpy as np

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

RForest = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=2)
RForest.fit(X, Y)
print(RForest.predict([[180, 85]]))


from sklearn.ensemble import RandomForestClassifier

import numpy as np
from sklearn.datasets import make_classification

X, Y = make_classification(
    n_samples=10,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    random_state=0,
    shuffle=True,
)

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=2)
model.fit(X, Y)
print(model.feature_importances_)
print(model.predict([[0, 0, 0]]))
estimator = model.estimators_[5]

from sklearn.tree import export_graphviz

export_graphviz(
    estimator,
    out_file="tmp_tree.dot",
    feature_names=["A", "B", "C"],
    class_names=["0", "1"],
    rounded=True,
    proportion=False,
    precision=2,
    filled=True,
)
