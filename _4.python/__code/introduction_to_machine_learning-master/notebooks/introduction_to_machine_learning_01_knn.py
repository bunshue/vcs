"""
introduction_to_machine_learning_01_knn

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.model_selection import cross_val_score



def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#k-Nearest Neighbors

# numpy and matplotlib will be used a lot during the lecture
# if you are familiar with these libraries you may skip this part
# if not - extended comments were added to make it easier to understand

# used later to apply different colors in for loops
mpl_colors = ('r', 'b', 'g', 'c', 'm', 'y', 'k', 'w')

# just to overwrite default colab style
plt.style.use('default')
plt.style.use('seaborn-talk')


def generate_random_points(size=10, low=0, high=1):
  """Generate a set of random 2D points
  
  size -- number of points to generate
  low  -- min value
  high -- max value
  """
  # random_sample([size]) returns random numbers with shape defined by size
  # e.g.
  # >>> np.random.random_sample((2, 3))
  #
  # array([[ 0.44013807,  0.77358569,  0.64338619],
  #        [ 0.54363868,  0.31855232,  0.16791031]])
  #
  return (high - low) * np.random.random_sample((size, 2)) + low


def init_plot(x_range=None, y_range=None, x_label="$x_1$", y_label="$x_2$"):
  """Set axes limits and labels
  
  x_range -- [min x, max x]
  y_range -- [min y, max y]
  x_label -- string
  y_label -- string
  """
 
  # subplots returns figure and axes
  # (in general you may want many axes on one figure)
  # we do not need fig here
  # but we will apply changes (including adding points) to axes
  _, ax = plt.subplots(dpi=70)
  
  # set grid style and color
  ax.grid(c='0.70', linestyle=':')
  
  # set axes limits (x_range and y_range is a list with two elements)
  ax.set_xlim(x_range) 
  ax.set_ylim(y_range)
    
  # set axes labels
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  
  # return axes so we can continue modyfing them later
  return ax


def plot_random_points(style=None, color=None):
  """Generate and plot two (separated) sets of random points
  style -- latter group points style (default as first)
  color -- latter group color (default as first)
  """
  
  # create a plot with x and y ranges from 0 to 2.5
  ax = init_plot([0, 2.5], [0, 2.5])

  # add two different sets of random points
  # first set = 5 points from [0.5, 1.0]x[0.5, 1.0]
  # second set = 5 points from [1.5, 2.0]x[1.5, 2.0]
  # generate_random_points return a numpy array in the format like
  # [[x1, y1], [x2, y2], ..., [xn, yn]]
  # pyplot.plt take separately arrays with X and Y, like
  # plot([x1, x2, x3], [y1, y2, y3])
  # thus, we transpose numpy array to the format
  # [[x1, x2, ..., xn], [y1, y2, ..., yn]]
  # and unpack it with *
  ax.plot(*generate_random_points(5, 0.5, 1.0).T, 'ro')
  ax.plot(*generate_random_points(5, 1.5, 2.0).T, style or 'ro')
  
  return ax


def plot_an_example(style=None, color=None, label="Class"):
  """Plot an example of supervised or unsupervised learning"""
  ax = plot_random_points(style, color)

  # circle areas related to each set of points
  # pyplot.Circle((x, y), r); (x, y) - the center of a circle; r - radius
  # lw - line width
  ax.add_artist(plt.Circle((0.75, 0.75), 0.5, fill=0, color='r', lw=2))
  ax.add_artist(plt.Circle((1.75, 1.75), 0.5, fill=0, color=color or 'r', lw=2))

  # put group labels
  # pyplot.text just put arbitrary text in given coordinates
  ax.text(0.65, 1.4, label + " I", fontdict={'color': 'r'})
  ax.text(1.65, 1.1, label + " II", fontdict={'color': color or 'r'})

"""
Our first ML problem
    Two classes: red circles and blue squares (training samples)
    Where does the green triangle (test sample) belong?
"""
X1 = generate_random_points(20, 0, 1)
X2 = generate_random_points(20, 1, 2)

new_point = generate_random_points(1, 0, 2)

plot = init_plot([0, 2], [0, 2])  # [0, 2] x [0, 2]

plot.plot(*X1.T, 'ro', *X2.T, 'bs', *new_point.T, 'g^')
plt.show()

#Nearest Neighbor

class NearestNeighbor():
  """Nearest Neighbor Classifier"""
  
  def __init__(self, distance=0):
    """Set distance definition: 0 - L1, 1 - L2"""
    if distance == 0:
      self.distance = np.abs     # absolute value
    elif distance == 1:
      self.distance = np.square  # square root
    else:
      raise Exception("Distance not defined.")
    
  
  def train(self, x, y):
    """Train the classifier (here simply save training data)
    
    x -- feature vectors (N x D)
    y -- labels (N x 1)
    """
    self.x_train = x
    self.y_train = y
    

  def predict(self, x):
    """Predict and return labels for each feature vector from x
    
    x -- feature vectors (N x D)
    """
    predictions = []  # placeholder for N labels
    
    # loop over all test samples
    for x_test in x:
      # array of distances between current test and all training samples
      distances = np.sum(self.distance(self.x_train - x_test), axis=1)
      
      # get the closest one
      min_index = np.argmin(distances)
      
      # add corresponding label
      predictions.append(self.y_train[min_index])

    return predictions

# let's create an array with 5x2 shape
a = np.random.random_sample((5, 2))

# and another array with 1x2 shape
b = np.array([[1., 1.]])

print(a, b, sep="\n\n")

# subtract arguments (element-wise)
# note, that at least one dimension must be the same 
print(a - b)

# numpy.abs calculates absolute value (element-wise)
print(np.abs(a - b))

# sum all elements
np.sum(np.abs(a - b))

# sum elements over a given axis
np.sum(np.abs(a - b), axis=0)

np.sum(np.abs(a - b), axis=1)

#Analysis

class Analysis():
  """Apply NearestNeighbor to generated (uniformly) test samples."""
  
  def __init__(self, *x, distance):
    """Generate labels and initilize classifier
    
    x -- feature vectors arrays
    distance -- 0 for L1, 1 for L2    
    """
    # get number of classes
    self.nof_classes = len(x)
    
    # create lables array
    # np.ones creates an array of given shape filled with 1 of given type
    # we apply consecutive integer numbers as class labels
    # ravel return flatten array
    y = [i * np.ones(_x.shape[0], dtype=np.int) for i, _x in enumerate(x)]
    y = np.array(y).ravel()

    # save training samples to plot them later
    self.x_train = x
    
    # merge feature vector arrays for NearestNeighbor
    x = np.concatenate(x, axis=0)
    
    # train classifier
    self.nn = NearestNeighbor(distance)
    self.nn.train(x, y)
        
    
  def prepare_test_samples(self, low=0, high=2, step=0.01):
    """Generate a grid with test points (from low to high with step)"""
    # remember range
    self.range = [low, high]
    
    # start with grid of points from [low, high] x [low, high]
    grid = np.mgrid[low:high+step:step, low:high+step:step]
    
    # convert to an array of 2D points
    self.x_test = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
    
  
  def analyse(self):
    """Run classifier on test samples and split them according to labels."""
    
    # find labels for test samples 
    self.y_test = self.nn.predict(self.x_test)
    
    self.classified = []  # [class I test points, class II test ...]
    
    # loop over available labels
    for label in range(self.nof_classes):
      # if i-th label == current label -> add test[i]
      class_i = np.array([self.x_test[i] \
                          for i, l in enumerate(self.y_test) \
                          if l == label])
      self.classified.append(class_i)
  
  
  def plot(self, t=''):
    """Visualize the result of classification"""
    plot = init_plot(self.range, self.range)
    plot.set_title(t)
    plot.grid(False)
    
    # plot training samples
    for i, x in enumerate(self.x_train):
      plot.plot(*x.T, mpl_colors[i] + 'o')
      
    # plot test samples
    for i, x in enumerate(self.classified):
      plot.plot(*x.T, mpl_colors[i] + ',')

#L1 test

l1 = Analysis(X1, X2, distance=0)
l1.prepare_test_samples()
l1.analyse()
l1.plot()

#L2 Test

l2 = Analysis(X1, X2, distance=1)
l2.prepare_test_samples()
l2.analyse()
l2.plot()


#Multiclass classification

def generate4(n=50):
  """Generate 4 sets of random points."""
  
  # points from [0, 1] x [0, 1]
  X1 = generate_random_points(n, 0, 1)
  # points from [1, 2] x [1, 2]
  X2 = generate_random_points(n, 1, 2)
  # points from [0, 1] x [1, 2]
  X3 = np.array([[x, y+1] for x,y in generate_random_points(n, 0, 1)])
  # points from [1, 2] x [0, 1]
  X4 = np.array([[x, y-1] for x,y in generate_random_points(n, 1, 2)])

  return X1, X2, X3, X4

# loop over no. of training samples
for n in (5, 10, 50, 100):
  # generate 4 sets of random points (each one with n samples)
  # unpack them when passing to Analysis
  c4 = Analysis(*generate4(n), distance=1)
  c4.prepare_test_samples()
  c4.analyse()
  c4.plot("No. of samples = {}".format(n))
  plt.show()

#Message 01: size matters!

#Noise

# generate 4 classes of 2D points
X1, X2, X3, X4 = generate4()

# add some noise by applying gaussian to every point coordinates
noise = lambda x, y: [np.random.normal(x, 0.1), np.random.normal(y, 0.1)]

X1 = np.array([noise(x, y) for x, y in X1])
X2 = np.array([noise(x, y) for x, y in X2])
X3 = np.array([noise(x, y) for x, y in X3])
X4 = np.array([noise(x, y) for x, y in X4])

# perform analysis
c4 = Analysis(X1, X2, X3, X4, distance=1)
c4.prepare_test_samples()
c4.analyse()
c4.plot()
plt.show()

#Overfitting

# Message 02: avoid overfitting!
#Accuracy

accuracy = 0

# loop over (sample, reconstructed label)
for sample, label in zip(c4.x_test, c4.y_test):
  # determine true label
  if sample[0] < 1 and sample[1] < 1:
    true_label = 0
  elif sample[0] > 1 and sample[1] > 1:
    true_label = 1
  elif sample[0] < 1 and sample[1] > 1:
    true_label = 2
  else:
    true_label = 3
    
  if true_label == label: accuracy += 1
    
accuracy /= len(c4.x_test)

print(accuracy)

print("------------------------------------------------------------")  # 60個

# Message 03: keep some data for testing!
print("k-Nearest Neighbors")


class kNearestNeighbors(NearestNeighbor):
  """k-Nearest Neighbor Classifier"""
  
  
  def __init__(self, k=1, distance=0):
    """Set distance definition: 0 - L1, 1 - L2"""
    super().__init__(distance)
    self.k = k
    
  
  def predict(self, x):
    """Predict and return labels for each feature vector from x
    
    x -- feature vectors (N x D)
    """
    predictions = []  # placeholder for N labels
    
    # no. of classes = max label (labels starts from 0)
    nof_classes = np.amax(self.y_train) + 1
    
    # loop over all test samples
    for x_test in x:
      # array of distances between current test and all training samples
      distances = np.sum(self.distance(self.x_train - x_test), axis=1)
      
      # placeholder for labels votes
      votes = np.zeros(nof_classes, dtype=np.int)
            
      # find k closet neighbors and vote
      # argsort returns the indices that would sort an array
      # so indices of nearest neighbors
      # we take self.k first
      for neighbor_id in np.argsort(distances)[:self.k]:
        # this is a label corresponding to one of the closest neighbor
        neighbor_label = self.y_train[neighbor_id]
        # which updates votes array
        votes[neighbor_label] += 1
                
      # predicted label is the one with most votes
      predictions.append(np.argmax(votes))

    return predictions

print("kAnalysis")


class kAnalysis(Analysis):
  """Apply kNearestNeighbor to generated (uniformly) test samples."""
  
  def __init__(self, *x, k=1, distance=1):
    """Generate labels and initilize classifier
    
    x -- feature vectors arrays
    k -- number of nearest neighbors
    distance -- 0 for L1, 1 for L2    
    """
    # get number of classes
    self.nof_classes = len(x)
    
    # create lables array
    y = [i * np.ones(_x.shape[0], dtype=np.int) for i, _x in enumerate(x)]
    y = np.array(y).ravel()

    # save training samples to plot them later
    self.x_train = x
    
    # merge feature vector arrays for NearestNeighbor
    x = np.concatenate(x, axis=0)
    
    # train classifier (knn this time)
    self.nn = kNearestNeighbors(k, distance)
    self.nn.train(x, y)

print("Sanity check")

# apply kNN with k=1 on the same set of training samples
knn = kAnalysis(X1, X2, X3, X4, k=1, distance=1)
knn.prepare_test_samples()
knn.analyse()
knn.plot()
plt.show()

print("k-Test")

# training size = 50
# let's check a few values between 1 and 50
for k in (1, 5, 10, 50):
  knn = kAnalysis(X1, X2, X3, X4, k=k, distance=1)
  knn.prepare_test_samples()
  knn.analyse()
  knn.plot("k = {}".format(k))
  plt.show()

print("------------------------------------------------------------")  # 60個

#Hyperparameters

#Over-, under-fitting example

# generate random data from x^2 function (with some noise)
data = np.array([[x, np.random.normal(x**2, 0.1)] \
                 for x in 2*np.random.random(10) - 1])

plot = init_plot([-1, 1], [-1, 1])
plot.plot(*data.T, 'o')
plt.show()

# loop over degrees of polynomial
# data is x^2, so let's try degrees 1, 2, 10
for n in (1, 2, 10):
  # polyfit returns an array with polynomial coefficients
  # poly1d is a polynomial class
  f = np.poly1d(np.polyfit(*data.T, n))
  
  # returns an array with 100 uniformly distributed numbers from -1 to 1
  x = np.linspace(-1, 1, 100)

  plot = init_plot([-1, 1], [-1, 1])
  plot.set_title("n = {}".format(n))
  plot.plot(*data.T, 'o', x, f(x))
  plt.show()

"""
For n = 1 we clearly underfit the data as we do not have enough parameters to describe the complexity of the problem

For n = 2 we have appropriate capacity (as we actually generated data form

    function)

    For n = 10 we overfit the data - training samples are described perfectly, but we clearly lost the generalization ability

Message 04: right choice of hyperparameters is crucial!
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Validation dataset

#Iris dataset

# columns names - can be used to access columns later
columns = ["Sepal Length", "Sepal Width",
           "Petal Length", "Petal Width",
           "Class"]

# iris.data is a csv file
src = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# load the file with pandas.read_csv 
# it will name columns as defined in columns list
# so one can access a column through index or name
iris_data = pd.read_csv(src, header=None, names=columns)

iris_data.head()  # print a few first entries


#Visualize dataset

# to extract rows with class column == class_name
extract = lambda class_name: iris_data.loc[iris_data['Class'] == class_name]

# axes settings - part = Sepal or Petal; x = Length, y = Width
set_ax = lambda part: {"x": part + " Length",
                       "y": part + " Width",
                       "kind": "scatter"}

# add iris type / sepal or petal / color to existing axis
plot = lambda class_name, part, color, axis: \
  extract(class_name).plot(**set_ax(part),
                           color=color,
                           label=class_name,
                           ax=axis)
  
# plot all Iris types (sepal or petal) on existing axis
plot_all = lambda part, axis: \
  [plot(iris, part, mpl_colors[i], axis) \
   for i, iris in enumerate(set(iris_data['Class']))] 

# with pyplot.subplots we can create many plots on one figure
# here we create 2 plots - 1 row and 2 columns
# thus, subplots returns figure, axes of 1st plot, axes for 2nd plot
_, (ax1, ax2) = plt.subplots(1, 2, figsize=(9,4))

# using messy lambda we can plot all Iris types at once
# Petal data on 1st plots and Sepal data on 2nd plot
plot_all("Petal", ax1)
plot_all("Sepal", ax2)

# tight_layout adjust subplots params so they fit into figure ares
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

#Prepare feature vectors and labels

# every Iris has 4 features (forming our 4D feature vectors)
# pandaoc.DataFrame.iloc allows us access data through indices
# we create an array with feature vectors by taking all rows for first 4 columns
X = iris_data.iloc[:, :4]

# it is still pandoc.DataFrame object - pretty handy
X.head()

# create numpy array (matrix) for further processing
X = np.array(X)

# print a few first entries
print(X[:5])

# as mentioned before, we can access DataFrame object through column labels
Y = np.array(iris_data["Class"])

# print a few first entries
print(Y[:5])

#Prepare test dataset

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train, X_valid, Y_train, Y_valid = train_test_split(X_train, Y_train, test_size=0.2)

# check how many sample we have
print(X_train.shape[0], X_valid.shape[0], X_test.shape[0])

#kNN from scikit-learn

# create knn classifier with k = 48
knn = KNeighborsClassifier(n_neighbors=48)

# train the model
knn.fit(X_train, Y_train)

# predict labels for test samples
Y_pred = knn.predict(X_valid)

#Accuracy

# use bold if true != predicted
for true, pred in zip(Y_valid, Y_pred):
  if pred == true:
    print("{}\t -> {}".format(true, pred))
  else:
    print("\033[1m{}\t -> {}\033[0m".format(true, pred))

# Y_valid == Y_pred -> array of True/False (if two elements are equal or not)
# (Y_valid == Y_pred).sum() -> number of Trues
# Y_valid.shape[0] -> number of validation samples
accuracy = (Y_valid == Y_pred).sum() / Y_valid.shape[0]
print(accuracy)

from sklearn.metrics import accuracy_score

print(accuracy_score(Y_valid, Y_pred))

#k-dependence of the accuracy

scores = []  # placeholder for accuracy

max_k = 85  # maximum number of voters

# loop over different values of k
for k in range(1, max_k):
  # create knn classifier with k = k
  knn = KNeighborsClassifier(n_neighbors=k)

  # train the model
  knn.fit(X_train, Y_train)

  # predict labels for test samples
  Y_pred = knn.predict(X_valid)
  
  # add accuracy to score table
  scores.append(accuracy_score(Y_valid, Y_pred))

#Now, we can plot accuracy as a function of k

def k_accuracy_plot(max_k=85):
  """Just plot settings"""
  plt.grid(True)
  plt.xlabel("k")
  plt.ylabel("Accuracy")
  plt.xlim([0, max_k + 5])
  plt.ylim([0, 1])
  plt.xticks(range(0, max_k + 5, 5))
  
  return plt

k_accuracy_plot().plot(range(1, max_k), scores)
plt.show()

#And check the accuracy measured on the test samples

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
  
print(accuracy_score(Y_test, Y_pred))

#0.9666666666666667

print("------------------------------------------------------------")  # 60個

#Cross-validation

# this time we do not create dedicated validation set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

avg_scores = []  # average score for different k

nof_folds = 10

# loop over different values of k
for k in range(1, max_k):
  # create knn classifier with k = k
  knn = KNeighborsClassifier(n_neighbors=k)

  # cross-validate knn on our training sample with nof_folds
  scores = cross_val_score(knn, X_train, Y_train,
                           cv=nof_folds, scoring='accuracy')
  
  # add avg accuracy to score table
  avg_scores.append(scores.mean())

k_accuracy_plot().plot(range(1, max_k), avg_scores)
plt.show()

print("------------------------------------------------------------")  # 60個

#Data normalization

# original data - both in cm
print(X[:5])

# make a copy of X
Xmm = X.copy()

# and multiply last two columns by 0.1
Xmm[:,2:] *= 0.1

# and we have our fake Iris data with petal length/width in mm
print(Xmm[:5])


def get_accuracy(X, Y, k=10):
  """Make training and test datasets and process through kNN"""
  
  # prepare training / test samples
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

  # create a kNN with k = k
  knn = KNeighborsClassifier(n_neighbors=k)

  # get prediction for original dataset
  knn.fit(X_train, Y_train)
  Y_pred = knn.predict(X_test)
  
  return accuracy_score(Y_test, Y_pred)

cm = get_accuracy(X, Y)
mm = get_accuracy(Xmm, Y)

print("Accuracy:\n\tboth in cm: {}\n\tpetal in mm: {}".format(cm, mm))

# Message 05: be aware of data normalization!

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#MNIST
"""
    THE MNIST DATABASE of handwritten digits
    The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
    It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.
    To make it simpler (and faster) let's use digits toy dataset which comes with scikit-learn src
    Each datapoint is a 8x8 image of a digit.
    About 180 samples per class (digit)
    Total number of samples 1797
"""

from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)

"""
(1797, 64)
    digits.images is a numpy array with 1797 numpy arrays 8x8 (feature vectors) representing digits
    digits.target is a numpy array with 1797 integer numbers (class labels)
    the code below allow us to visualize a random digits from the dataset
"""
# set grayscale
plt.gray()

# get some random index from 0 to dataset size
random_index = np.random.randint(1796)


# draw random digit
plt.matshow(digits.images[random_index])

# and print the matrix
plt.text(8, 5, digits.images[random_index],
         fontdict={'family': 'monospace', 'size': 16})

# and the label
plt.text(10, 1, "This is: {}".format(digits.target[random_index]),
         fontdict={'family': 'monospace', 'size': 16})
plt.show()

#Distance between images
"""
  TEST      TRAIN    PIXEL-WISE
| 4 2 0     2 5 8 |   |2 3 8|
| 5 3 9  -  2 8 1 | = |3 5 8|  ->  38
| 0 2 3     1 4 9 |   |1 2 6|
"""
#Prepare data

# the original shape of an image
print(digits.images.shape)

#(1797, 8, 8)

# numpy.reshape is handy here
print(digits.images.reshape((1797, -1)).shape)

#(1797, 64)

print(digits.images.reshape((1797, 64)).shape)

#(1797, 64)

print(digits.images.reshape((-1, 64)).shape)

#(1797, 64)

data_train, data_test, label_train, label_test = \
  train_test_split(digits.images.reshape((1797, -1)), digits.target, test_size=0.2)

#Cross-validation

avg_scores = []  # average score for different k

max_k = 50
nof_folds = 10

# loop over different values of k
for k in range(1, max_k):
  # create knn classifier with k = k
  knn = KNeighborsClassifier(n_neighbors=k)

  # cross-validate knn on our training sample with nof_folds
  scores = cross_val_score(knn, data_train, label_train,
                           cv=nof_folds, scoring='accuracy')
  
  # add avg accuracy to score table
  avg_scores.append(scores.mean())

plt.grid(True)
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.xlim([0, max_k])
plt.ylim([0, 1])
plt.xticks(range(0, max_k, 5))
  
plt.plot(range(1, max_k), avg_scores)
plt.show()

#Final test

from sklearn.metrics import accuracy_score

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data_train, label_train)
prediction = knn.predict(data_test)

print(accuracy_score(label_test, prediction))

#0.9888888888888889

for i, (true, predict) in enumerate(zip(label_test, prediction)):
  if true != predict:
    digit = data_test[i].reshape((8, 8))  # reshape again to 8x8
    plt.matshow(digit)                    # for matshow
    plt.title("{} predicted as {}".format(true, predict))
plt.show()

print("------------------------------------------------------------")  # 60個

#Regression with kNN

#Genearate some fake data

data_size = 50

# generate and sort *data_size* numbers from 0 to 4pi 
x_train = 4 * np.pi * np.sort(np.random.rand(data_size, 1), axis=0)

# let's fit to sine  
y_train = np.sin(x_train).ravel()

# add some noise to the data
y_train = np.array([np.random.normal(y, 0.05) for y in y_train])

plt.plot(x_train, y_train, 'ro')
plt.show()

#Make a fit

#Comment on numpy.newaxis

# let's create a 1D numpy array
D1 = np.array([1, 2, 3, 4])

print(D1)

#[1 2 3 4]

# we can easily add another dimension using numpy.newaxis
D2 = D1[:, np.newaxis]

print(D2)

#And back to the task

from sklearn.neighbors import KNeighborsRegressor

# first we need test sample
x_test = np.linspace(0, 4*np.pi, 100)[:, np.newaxis]

for i, k in enumerate((1, 5, 10, 20)):
  # weights=distance - weight using distances
  knn = KNeighborsRegressor(k, weights='distance')
  
  # calculate y_test for all points in x_test
  y_test = knn.fit(x_train, y_train).predict(x_test)
  
  plt.subplot(2, 2, i + 1)

  plt.title("k = {}".format(k))
  
  plt.plot(x_train, y_train, 'ro', x_test, y_test, 'g')
  
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
