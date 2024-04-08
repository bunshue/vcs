from numpy import *
import numpy as np
from Nbayes_lib import *

dataSet,listClasses = loadDataSet()
nb = NBayes()
nb.train_set(dataSet,listClasses)
nb.map2vocab(dataSet[3])

print(nb.predict(nb.testset))

