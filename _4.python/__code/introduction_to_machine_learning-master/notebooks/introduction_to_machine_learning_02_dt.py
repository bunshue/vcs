"""
決策樹
introduction_to_machine_learning_02_dt

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

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from graphviz import Digraph
'''
styles = {
    'top': {'shape': 'ellipse', 'style': 'filled', 'color': 'lightblue'},
    'no':  {'shape': 'circle', 'style': 'filled', 'color': 'red'},
    'yes': {'shape': 'circle', 'style': 'filled', 'color': 'lightgreen'},
    'qst': {'shape': 'rect'}
}

example_tree = Digraph()

example_tree.node('top', 'Should I attend the ML lecture?', styles['top'])
example_tree.node('q1', 'Do I fulfill requirements?', styles['qst'])

example_tree.node('q2', 'Do I like CS?', styles['qst'])
example_tree.node('no1', 'No ', styles['no'])

example_tree.node('q3', 'Is the lecture early in the morning?', styles['qst'])
example_tree.node('no2', 'No ', styles['no'])

example_tree.node('no3', 'No ', styles['no'])
example_tree.node('yes', 'Yes', styles['yes'])

example_tree.edge('top', 'q1')

example_tree.edge('q1', 'q2', 'Yes')
example_tree.edge('q1', 'no1', 'No')

example_tree.edge('q2', 'q3', 'Yes')
example_tree.edge('q2', 'no2', 'No')

example_tree.edge('q3', 'no3', 'Yes')
example_tree.edge('q3', 'yes', 'No')

example_tree

# just to overwrite default colab style
plt.style.use('default')
plt.style.use('seaborn-talk')

# first define some points representing two classes
grid = np.mgrid[0:10:2, 0:10:2]
set01 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set01 = np.delete(set01, [17, 18, 19, 22, 24], axis=0)

grid = np.mgrid[6:16:2, 0:10:2]
set02 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set02 = np.delete(set02, [0, 1, 5, 6, 8], axis=0)

plt.scatter(*set01.T)
plt.scatter(*set02.T)

plt.text(15, 4, "There are two attributes: x and y\n\n"
                "    * each decision node splits dataset based on one of the attributes\n\n"
                "    * each leaf node defines a class label")
plt.show()



plt.scatter(*set01.T)
plt.scatter(*set02.T)

plt.plot([5, 5], [0, 8], 'r')
plt.plot([0, 14], [3, 3], 'g')

plt.text(15, 3, "We start with [20, 20] (blue, orange)\n\n"
                "Red line splits dataset in [15, 0] (left) and [5, 20] (right)\n\n"
                "Green line split dataset in [10, 6] (bottom) and [10, 14] (top)\n\n"
                "Red line is a winner and should be the root of our tree")
plt.show()





tree = Digraph()

tree.edge("x > 5?\n[20, 20]", "blue\n[15, 0]", "No")
tree.edge("x > 5?\n[20, 20]", "y > 3?\n[5, 20]", "Yes")

tree.edge("y > 3?\n[5, 20]", "x > 9?\n[4, 6]", "No")
tree.edge("y > 3?\n[5, 20]", "almost orange\n[1, 14]", "Yes")

tree.edge("x > 9?\n[4, 6]", "blue\n[4, 0]", "No")
tree.edge("x > 9?\n[4, 6]", "orange\n[0, 6]", "Yes")

tree.edge("almost orange\n[1, 14]", "Should we continue?\nOr would it be overfitting?")

tree

tree = Digraph()

tree.edge("y > 3?\n[20, 20]", "x > 9?\n[10, 6]", "No")
tree.edge("y > 3?\n[20, 20]", "x > 5?\n[10, 14]", "Yes")

tree.edge("x > 9?\n[10, 6]", "blue\n[10, 0]", "No")
tree.edge("x > 9?\n[10, 6]", "orange\n[0, 6]", "Yes")

tree.edge("x > 5?\n[10, 14]", "blue\n[9, 0]", "No")
tree.edge("x > 5?\n[10, 14]", "almost orange\n[1, 14]", "Yes")

tree

#ID3 and C4.5 algorithms

x = np.arange(0.01, 1.01, 0.01)

plt.xlabel("p")
plt.ylabel("I(p)")

plt.plot(x, -np.log2(x), label="bit")
plt.plot(x, -np.log(x), label="nat")
plt.plot(x, -np.log10(x), label="dit")

plt.legend()
plt.show()



p = np.arange(0.01, 1.0, 0.01)

plt.xlabel("p")
plt.ylabel("H")

plt.annotate('we are surprised', xy=(0.5, 1), xytext=(0.5, 0.75),
             arrowprops=dict(facecolor='black', shrink=0.1))

plt.annotate('we are not that surprised', xy=(1, 0.1), xytext=(0.5, 0.25),
             arrowprops=dict(facecolor='black', shrink=0.1))

plt.plot(p, -p * np.log2(p) - (1 - p) * np.log2(1 - p))

plt.show()



from mpl_toolkits import mplot3d

# grid of p, q probabilities
p, q = np.meshgrid(np.arange(0.01, 1.0, 0.01), np.arange(0.01, 1.0, 0.01))

# remove (set to 0) points which do not fulfill P <= 1
idx = p + q > 1
p[idx] = 0
q[idx] = 0

# calculate entropy (disable warnings - we are aware of log(0))
np.warnings.filterwarnings('ignore')
h = -p * np.log2(p) - q * np.log2(q) - (1 - p - q) * np.log2(1 - p - q)

# make a plot
plt.axes(projection='3d').plot_surface(p, q, h)

plt.show()


from math import log

def entropy(*probs):
  """Calculate information entropy"""
  try:
    total = sum(probs)
    return sum([-p / total * log(p / total, 2) for p in probs])
  except:
    return 0

print(entropy(4, 5), entropy(2, 1), entropy(2, 2))

'''
print("------------------------------------------------------------")  # 60個


import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


# first row = headers
src = "http://chem-eng.utoronto.ca/~datamining/dmc/datasets/weather_nominal.csv"
src = "weather-nominal-weka.csv"

golf_data = pd.read_csv(src)

print(golf_data)

# Play golf entropy

cc = entropy(9, 5)
print(cc)

#Play golf vs outlook

cc = entropy(3, 2), 0, entropy(2, 3)
print(cc)

#(0.9709505944546686, 0, 0.9709505944546686)

#Results for all features

tree = Digraph()

tree.edge("outlook", "sunny")
tree.edge("outlook", "overcast")
tree.edge("outlook", "rainy")

tree.edge("overcast", "yes")

print(tree)

#Next branch

cc = golf_data.loc[golf_data['Outlook'] == "Sunny"]
print(cc)

tree.edge("sunny", "windy")

tree.edge("windy", "false")
tree.edge("windy", "true")

tree.edge("false", "yes")
tree.edge("true", "no")

print(tree)

#Last branch

cc = golf_data.loc[golf_data['Outlook'] == "Rainy"]
print(cc)

tree.edge("rainy", "humidity")

tree.edge("humidity", "high")
tree.edge("humidity", "normal")

tree.edge("normal", "yes")
tree.edge("high", "no ")

print(tree)

# Information gain for name

h = entropy(4, 6)  # dataset entropy H(T)

# one John plays and the other one doesn't
# in other cases entropy = 0
g_name = h - 2/10 * entropy(1, 1)

print(g_name)

# 0.7709505944546686

# Information gain for sex

# 5 men - 3 play
# 5 women - 3 play
g_sex = h - 5/10 * entropy(2, 3) - 5/10 * entropy(2, 3)

print(g_sex)

#0.0

# Information gain for age

# 4 old people - 1 plays
# 6 young people - 5 play
g_age = h - 4/10 * entropy(1, 3) - 6/10 * entropy(1, 5)

print(g_age)

#0.256425891682003

# Information gain ratio for name

# 2x John, 2x Alex, 6x unique name 
cc = g_name / entropy(2, 2, *[1]*6)
print(cc)

#0.26384995435159336

# Information gain ratio for sex

# 5 males and 5 females - zero stays zero though
cc = g_sex / entropy(5, 5)
print(cc)

#0.0

#  Information gain ratio for age

# 4x old and 6x young
cc = g_age / entropy(4, 6)
print(cc)

#0.26409777505314147

print("Two possible values:\n")

for i in range(0, 11):
  print("\t({}, {}) split -> entropy = {}".format(i, 10-i, entropy(i, 10-i)))

print("\n10 possible values:", entropy(*[1]*10))

# calculate entropy for all possible thresholds
e18 = 2/10 * entropy(1, 1) + 8/10 * entropy(3, 5)
e24 = 4/10 * entropy(1, 3) + 6/10 * entropy(3, 3)
e31 = 6/10 * entropy(1, 5) + 4/10 * entropy(3, 1)
e50 = 9/10 * entropy(4, 5) + 1/10 * entropy(0, 1)

print("With threshold = {}, entropy = {}".format(18, e18))
print("With threshold = {}, entropy = {}".format(24, e24))
print("With threshold = {}, entropy = {}".format(31, e31))
print("With threshold = {}, entropy = {}".format(50, e50))

# First example - step by step

# first define some points representing two classes
grid = np.mgrid[0:10:2, 0:10:2]
set01 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set01 = np.delete(set01, [17, 18, 19, 22, 24], axis=0)

grid = np.mgrid[6:16:2, 0:10:2]
set02 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set02 = np.delete(set02, [0, 1, 5, 6, 8], axis=0)

plt.scatter(*set01.T)
plt.scatter(*set02.T)
plt.show()

# Validation set

# split dataset to training and validation set
# note, we should splt them randomly
# but here we do this by hand
valid_idx = [3, 7, 10, 14, 18]

blue_valid = set01[valid_idx]
blue_train = np.delete(set01, valid_idx, axis=0)

orange_valid = set02[valid_idx]
orange_train = np.delete(set02, valid_idx, axis=0)

# circles - training set
# x - validation set
plt.scatter(*blue_train.T)
plt.scatter(*blue_valid.T, color='C0', marker='x')
plt.scatter(*orange_train.T)
plt.scatter(*orange_valid.T, color='C1', marker='x')
plt.show()

# Thresholds finder

def info_gain(Nb, No, nb, no):
  """Calculate information gain for given split"""
  h = entropy(Nb, No) # H(S)
  total = Nb + No     # total number of samples
  subtotal = nb + no  # number of samples in subset
  
  return h - subtotal / total * entropy(nb, no) \
           - (total - subtotal) / total * entropy(Nb - nb, No - no)

# Feature X

Nb = 15
No = 15

splits = {"0": (4, 0), "2 ": (8, 0), "4": (11, 0), "6": (13, 3),
          "8": (15, 4), "10": (15, 8), "12": (15, 11)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

# 4 samples with x = 0, 4 samples with x = 2 etc
cc = info_gain(Nb, No, *splits["4"]) / entropy(4, 4, 3, 5, 3, 4, 3, 4)
print(cc)

#Feature Y

Nb = 15
No = 15

splits = {"0": (4, 2), "2": (8, 5), "4": (10, 8), "6": (13, 11)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

cc = info_gain(Nb, No, *splits["2"]) / entropy(6, 7, 5, 6, 6)
print(cc)

#The root

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "[4, 15]", "Yes")

print(tree)

plt.xlim([5.5, 14.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)
plt.show()

# Check x maximum information gain ratio

Nb = 4
No = 15

splits = {"6": (2, 3), "8": (4, 4), "10": (4, 8), "12": (4, 11)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

print("Information gain ratio with x > 8:",
      info_gain(Nb, No, *splits["8"]) / entropy(5, 3, 4, 3, 4))

#Information gain ratio with x > 8: 0.14010311259651076

# Check y maximum information gain ratio

Nb = 4
No = 15

splits = {"0": (2, 2), "2": (3, 5), "4": (3, 6), "6": (4, 9)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))


print("Information gain ratio with y > 6:",
      info_gain(Nb, No, *splits["6"]) / entropy(4, 4, 3, 4, 4))

#Information gain ratio with y > 6: 0.05757775370755489

# Once again x is a winner
# And we have a new node

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

print(tree)

#Branch x<= 8

#We will continue until the tree is fully grown

plt.xlim([5.5, 8.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)
plt.show()

#Again, the best cut may be pretty obvious, but lets check the math
#We have one possible cut in x

Nb = 4
No = 4
'''
print("Information gain ratio with x > 6:",
      info_gain(Nb, No, 2, 3) / entropy(5, 3))

Information gain ratio with x > 6: 0.05112447853477686

    And usual threshold candidates in 

splits = {"0": (2, 0), "2": (3, 0), "4": (3, 1), "6": (4, 2)}

for threshold, (no, nb) in splits.items():
  print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

Threshold = 0	 -> 0.31127812445913283
Threshold = 2	 -> 0.5487949406953986
Threshold = 4	 -> 0.1887218755408671
Threshold = 6	 -> 0.31127812445913283

print("Information gain ratio with y > 2:",
      info_gain(Nb, No, *splits["2"]) / entropy(2, 1, 1, 2, 2))

Information gain ratio with y > 2: 0.24390886253128827

    And the tree is growing

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "[1, 4]", "Yes")

tree

b'\n\n\n\nx > 4?[15, 15]blue[11, 0]Nox > 8?[4, 15]Yesy > 2?[4, 4]Noorange[0, 11]Yesblue[3, 0]No[1, 4]
Yes
Branch y > 2

plt.xlim([5.5, 8.5])
plt.ylim([3.5, 8.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)
plt.show()

Nb = 1
No = 4

print("Information gain ratio with x > 6:",
      info_gain(Nb, No, 0, 3) / entropy(3, 2))

Information gain ratio with x > 6: 0.33155970728682876

print("Information gain ratio with y > 4:",
      info_gain(Nb, No, 0, 1) / entropy(1, 2, 2))

print("Information gain ratio with y > 6:",
      info_gain(Nb, No, 1, 2) / entropy(1, 2, 2))

Information gain ratio with y > 4: 0.047903442721748145
Information gain ratio with y > 6: 0.11232501392736344

The final tree

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "x > 6?\n[1, 4]", "Yes")

tree.edge("x > 6?\n[1, 4]", "orange\n[0, 3]", "No")
tree.edge("x > 6?\n[1, 4]", "y > 6?\n[1, 1]", "Yes")

tree.edge("y > 6?\n[1, 1]", "blue\n[1, 0]", "No")
tree.edge("y > 6?\n[1, 1]", "orange\n[0, 1]", "Yes")

tree

b'\n\n\n\nx > 4?[15, 15]blue[11, 0]Nox > 8?[4, 15]Yesy > 2?[4, 4]Noorange[0, 11]Yesblue[3, 0]Nox > 6?[1, 4]Yesorange[0, 3]Noy > 6?[1, 1]Yesblue[1, 0]Noorange[0, 1]
Yes

    It is likely that this tree is overfitted

    We will proceed with pruning as it was explained

    But first lets implement decision rules to measure accuracy

def tree_nominal(x, y):
  """Implementation of above tree"""
  if x <= 4:
    return "blue"
  elif x > 8:
    return "orange"
  elif y <= 2:
    return "blue"
  elif x <= 6:
    return "orange"
  else:
    return "orange" if y > 6 else "blue"

Sanity check

    If the tree is built correctly we expect 100% accuracy on training set

for x, y in blue_train:
  print(tree_nominal(x, y), end=' ')

blue blue blue blue blue blue blue blue blue blue blue blue blue blue blue 

for x, y in orange_train:
  print(tree_nominal(x, y), end=' ') 

orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange 

Accuracy before pruning

def accuracy(samples, tree):
  """Just print the result of classification"""
  for x, y in samples:
    print("({}, {}) -> {}".format(x, y, tree(x, y)))

accuracy(blue_valid, tree_nominal)

(0, 6) -> blue
(2, 4) -> blue
(4, 0) -> blue
(4, 8) -> blue
(8, 2) -> blue

accuracy(orange_valid, tree)

(8, 4) -> blue
(10, 4) -> orange
(12, 0) -> orange
(12, 8) -> orange
(14, 6) -> orange

Pruning I

    We want to prune last decision node 

    In general, majority decides about the leaf node class

    As it is a tie here, lets check both

def tree_prune01a(x, y):
  """Implementation of above tree"""
  if x <= 4:
    return "blue"
  elif x > 8:
    return "orange"
  elif y <= 2:
    return "blue"
  elif x <= 6:
    return "orange"
  else:
    return "blue"
  
def tree_prune01b(x, y):
  """Implementation of above tree"""
  if x <= 4:
    return "blue"
  elif x > 8:
    return "orange"
  elif y <= 2:
    return "blue"
  else:
    return "orange"

accuracy(blue_valid, tree_prune01a)

(0, 6) -> blue
(2, 4) -> blue
(4, 0) -> blue
(4, 8) -> blue
(8, 2) -> blue

accuracy(orange_valid, tree_prune01a)

(8, 4) -> blue
(10, 4) -> orange
(12, 0) -> orange
(12, 8) -> orange
(14, 6) -> orange

    Pruning does not change the accuracy

    We always use Occam's razor and prune01a is preferred over nominal tree

    But lets see how prune01b works

accuracy(blue_valid, tree_prune01b)

(0, 6) -> blue
(2, 4) -> blue
(4, 0) -> blue
(4, 8) -> blue
(8, 2) -> blue

accuracy(orange_valid, tree_prune01b)

(8, 4) -> orange
(10, 4) -> orange
(12, 0) -> orange
(12, 8) -> orange
(14, 6) -> orange

    In this case we even get the increase of the accuracy

    We decide to prune a tree by replacing 

decision node with "orange" leaf node

Which automatically removes

    decision node

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "orange\n[1, 4]", "Yes")

tree

b'\n\n\n\nx > 4?[15, 15]blue[11, 0]Nox > 8?[4, 15]Yesy > 2?[4, 4]Noorange[0, 11]Yesblue[3, 0]Noorange[1, 4]
Yes
Pruning II

    Now, lets see the accuracy after removing 

    node

    It is once again a tie, so lets check both scenarios

def tree_prune02a(x, y):
  """Implementation of above tree"""
  if x <= 4:
    return "blue"
  else:
    return "orange"
  
def tree_prune02b(x, y):
  """Implementation of above tree"""
  if x <= 4:
    return "blue"
  elif x > 8:
    return "orange"
  else:
    return "blue"

accuracy(blue_valid, tree_prune02a)

(0, 6) -> blue
(2, 4) -> blue
(4, 0) -> blue
(4, 8) -> blue
(8, 2) -> orange

accuracy(orange_valid, tree_prune02a)

(8, 4) -> orange
(10, 4) -> orange
(12, 0) -> orange
(12, 8) -> orange
(14, 6) -> orange

accuracy(blue_valid, tree_prune02b)

(0, 6) -> blue
(2, 4) -> blue
(4, 0) -> blue
(4, 8) -> blue
(8, 2) -> blue

accuracy(orange_valid, tree_prune02b)

(8, 4) -> blue
(10, 4) -> orange
(12, 0) -> orange
(12, 8) -> orange
(14, 6) -> orange

    In both cases the error increased

    We stop pruning and leave the tree as it is in prune01b version

Summary

    C4.5 algorithm gives the full and clear prescription for building decision trees

    It may look as a long procedure, but it is only because I wanted to show everything step by step and avoid "after a few trivial steps..."

    ID3/C4.5/C5.0 are based on information theory

    There is alternative procedure based on gini impurity, which is used by CART

CART

    CART stands for Classification and Regression Tree

    It was created independently from ID3 (more or less at the same time)

    The main differences:

        it creates binary trees (each decision node has two branches)

        it uses gini impurity instead of information gain

        it supports numerical target variables (regression)

Gini impurity

    Let

be the set of

classes

and

be the probability distribution

where
is the probability that a sample belongs to class

and

is the probability that it belongs to another class

Gini impurity is defines as

As before (for entropy), lets consider two case scenario with
, so gini impurity is given by

p = np.arange(0.01, 1.0, 0.01)

plt.xlabel("p")
plt.ylabel("surprise factor")

plt.plot(p, -p * np.log2(p) - (1 - p) * np.log2(1 - p), label="Entropy")
plt.show()

plt.plot(p, -2*p*(p - 1), label="Gini impurity")

plt.legend()
plt.show()


print("------------------------------------------------------------")  # 60個


Play Golf

    Lets consider once again Play Golf dataset


# first row = headers
src = "http://chem-eng.utoronto.ca/~datamining/dmc/datasets/weather_nominal.csv"

golf_data = pd.read_csv(src)

golf_data

	Outlook 	Temperature 	Humidity 	Windy 	Play golf
0 	Rainy 	Hot 	High 	False 	No
1 	Rainy 	Hot 	High 	True 	No
2 	Overcast 	Hot 	High 	False 	Yes
3 	Sunny 	Mild 	High 	False 	Yes
4 	Sunny 	Cool 	Normal 	False 	Yes
5 	Sunny 	Cool 	Normal 	True 	No
6 	Overcast 	Cool 	Normal 	True 	Yes
7 	Rainy 	Mild 	High 	False 	No
8 	Rainy 	Cool 	Normal 	False 	Yes
9 	Sunny 	Mild 	Normal 	False 	Yes
10 	Rainy 	Mild 	Normal 	True 	Yes
11 	Overcast 	Mild 	High 	True 	Yes
12 	Overcast 	Hot 	Normal 	False 	Yes
13 	Sunny 	Mild 	High 	True 	No
Gini impurity

    We treat all values as they are continues

    And consider all possible split

    Every split leads to two subsets

and

And gini impurity for a set

for given split is given by:

def gini(*distribution):
  """Calculate gini impurity for given ditribution of samples"""
  sum2 = sum(distribution)**2  # normalization factor
  
  return 1 - sum([p**2 for p in distribution])/sum2

def gini_split(s1, s2, g1, g2):
  """Calcualte impurity for given split
  
  s1 -- the size of S1 subset
  s1 -- the size of S2 subset
  g1 -- I(S1)
  g2 -- I(S2)
  """
  s = s1 + s2  # the total set size
  
  return s1/s * g1 + s2/s * g2

            | Play golf |
            =============
            | yes | no  |
      -------------------
      | yes |  2  |  3  | 5
rainy | no  |  7  |  2  | 9
      -------------------
               9     5

gini_split(5, 9, gini(2, 3), gini(7, 2))

0.3936507936507937

            | Play golf |
            =============
            | yes | no  |
      -------------------
      | yes |  3  |  2  | 5
sunny | no  |  6  |  3  | 9
      -------------------
               9     5

gini_split(5, 9, gini(3, 2), gini(6, 3))

0.45714285714285713

               | Play golf |
               =============
               | yes | no  |
         -------------------
         | yes |  4  |  0  | 4
overcast | no  |  5  |  5  | 10
         -------------------
                  9     5

gini_split(4, 10, gini(4, 0), gini(5, 5))

0.35714285714285715

    From Outlook feature the best choice is Overcast as it minimizes impurity

    However, we would have to check other features and choose the best predictor from all possibilities

    We have one step by step example done though

    So lets use some tool

Scikit learn

    One step by step example is behind us, so now lets use some tool

    CART is implemented in scikit-learn

    However, their implementation takes only numerical values

    So we will use LabelDecoder to convert all values to numbers

from sklearn.preprocessing import LabelEncoder

# pandas.DataFrame.apply applies a function to given axis (0 by default)
# LabelEncoder encodes class labels with values between 0 and n-1
golf_data_num = golf_data.apply(LabelEncoder().fit_transform)

golf_data_num

	Outlook 	Temperature 	Humidity 	Windy 	Play golf
0 	1 	1 	0 	0 	0
1 	1 	1 	0 	1 	0
2 	0 	1 	0 	0 	1
3 	2 	2 	0 	0 	1
4 	2 	0 	1 	0 	1
5 	2 	0 	1 	1 	0
6 	0 	0 	1 	1 	1
7 	1 	2 	0 	0 	0
8 	1 	0 	1 	0 	1
9 	2 	2 	1 	0 	1
10 	1 	2 	1 	1 	1
11 	0 	2 	0 	1 	1
12 	0 	1 	1 	0 	1
13 	2 	2 	0 	1 	0

    Now, lets splits our dataset to features and labels

# DataFrame.iloc makes an access thourgh indices
# we want all rows and first 4 columns for features
# and the last column for labels
data = np.array(golf_data_num.iloc[:, :4])
target = np.array(golf_data_num.iloc[:, 4])

    Once data is prepared, creating a tree is as easy as 2 + 2 -1

from sklearn import tree

golf_tree = tree.DecisionTreeClassifier()

golf_tree.fit(data, target)
plt.show()

    sklearn.tree supports drawing a tree using graphviz

import graphviz

# dot is a graph description language
dot = tree.export_graphviz(golf_tree, out_file=None, 
                           feature_names=golf_data.columns.values[:4],  
                           class_names=["no", "yes"],  
                           filled=True, rounded=True,  
                           special_characters=True) 

# we create a graph from dot source using graphviz.Source
graph = graphviz.Source(dot) 
graph

b'\n\n\n\nOutlook \xe2\x89\xa4 0.5gini = 0.459samples = 14value = [5, 9]class = yesgini = 0.0samples = 4value = [0, 4]class = yesTrueHumidity \xe2\x89\xa4 0.5gini = 0.5samples = 10value = [5, 5]class = noFalseOutlook \xe2\x89\xa4 1.5gini = 0.32samples = 5value = [4, 1]class = noWindy \xe2\x89\xa4 0.5gini = 0.32samples = 5value = [1, 4]class = yesgini = 0.0samples = 3value = [3, 0]class = noWindy \xe2\x89\xa4 0.5gini = 0.5samples = 2value = [1, 1]class = nogini = 0.0samples = 1value = [0, 1]class = yesgini = 0.0samples = 1value = [1, 0]class = nogini = 0.0samples = 3value = [0, 3]class = yesOutlook \xe2\x89\xa4 1.5gini = 0.5samples = 2value = [1, 1]class = nogini = 0.0samples = 1value = [0, 1]class = yesgini = 0.0samples = 1value = [1, 0]class = no

    Please note, that in the case of a real problem we would want to have a validation set and perform a pruning (scikit-learn does not support it though)

Regression

    The difference now is that targets are numerical values (instead of categorical), e.g. in golf data - number of hours played instead of "yes / no"

    Features may be either discrete or continuous

    The idea is the same though - we want to create a binary tree and minimize the error on in each leaf

    However, having continuous values as targets we can not simply use entropy or gini

    We need to use different measurement - variance

where
and

is the average value

Note, that here

    are equally likely

Simple example

    Before we learn how to grow a regression tree, lets take a look how it works on a simple example

    Lets consider data distributed according to

(with some noise, obviously)

It means with have continuous features (
) and targets (

)

We will split by hand the domain in
and

X = np.random.sample(50)
Y = np.array([x**2 + np.random.normal(0, 0.05) for x in X])

plt.xlabel("x")
plt.ylabel("y")

plt.scatter(X, Y, color='b')
plt.plot([0.3, 0.3], [-0.2, 1.2], 'g--')
plt.plot([0.6, 0.6], [-0.2, 1.2], 'g--')
plt.show()

    The corresponding tree would look like this

tree = Digraph()

tree.edge("x < 0.3?", "?", "No")
tree.edge("x < 0.3?", "x < 0.6?", "Yes")

tree.edge("x < 0.6?", "? ", "No")
tree.edge("x < 0.6?", "?  ", "Yes")

tree

b'\n\n\n\nx < 0.3??Nox < 0.6?Yes? No?  
Yes

    For each split lets find a value

def avg(X, Y, x_min, x_max):
  """Return the average value in (x_min, x_max) range"""
  n = 0    # number of samples in given split 
  avg = 0  # average value

  for x, y in zip(X, Y):
    if x >= x_min and x < x_max:
      n += 1
      avg += y

  return avg / n

plt.scatter(X, Y, color='b')

plt.plot([0.3, 0.3], [-0.2, 1.2], 'g--')
plt.plot([0.6, 0.6], [-0.2, 1.2], 'g--')

y = avg(X, Y, 0, 0.3)
plt.plot([0.0, 0.3], [y, y], 'r')

y = avg(X, Y, 0.3, 0.6)
plt.plot([0.3, 0.6], [y, y], 'r')

y = avg(X, Y, 0.6, 1)
plt.plot([0.6, 1.0], [y, y], 'r')
plt.show()

    Alternatively, one could do linear regression for split

Growing a tree

    The idea is similar as for numerical values in classification problems

    For each feature we check all possible splits and calculate variance

    We choose a binary split which minimzes variance

from sklearn.tree import DecisionTreeRegressor

# create a decision tree regressor
fit = DecisionTreeRegressor()

# and grow it (note that X must be reshaped)
fit.fit(np.reshape(X, (-1, 1)), Y)
plt.show()

# prepare test sample with "newaxis" trick
X_test = np.arange(0.0, 1.0, 0.01)[:, np.newaxis]
Y_test = fit.predict(X_test)

plt.scatter(X, Y, color='b')
plt.plot(X_test, Y_test)
plt.show()

    And this is a perfect example of overfitting

    Each point was classified as a separate target

    Beacause without any stopping criterion the tree is growing until there is a single point in a leaf

    There are several strategies to pre-prune a tree:

        define a max depth of a tree

        define a minimum number of samples in a leaf

        define a minimum impurity

        define a minimum impurity decrease

    Whatever method is chosen you get a hyperparameter

    And we already know how to find an optimal hyperparameter: cross-validation

Tree: cross-validation

    To make it easier to check all possible methods lets create a simple class to do that for us

    It takes training data and hyperparameter name (as named in scikit-learn)

    It can change hyperparameter

    It can perform a cross-validation for a set of hyperparameter values

    It can make accuracy and best fit plots

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

class TreeCV:
  """Perform a cross-validation for chosen hyperparameter"""
  
  def __init__(self, X, Y, hp="max_depth"):
    """Save training data"""
    self.X = X    # features
    self.Y = Y    # targets
    self.hp = hp  # hyperparameter
    

  def set_method(self, hp):
    """Set hyperparameter to use"""
    self.hp = hp
    
  
  def cross_me(self, *hp_vals):
    """Perform cross validation for given hyperparameter values"""
    self.scores = []  # the accuracy table
    self.best = None  # the best fit
    
    best_score = 0
    
    for hp in hp_vals:
      # create a tree with given hyperparameter cut
      fit = DecisionTreeRegressor(**{self.hp: hp})
      
      # calculate a cross validation scores and a mean value
      score = cross_val_score(fit, np.reshape(X, (-1, 1)), Y).mean()
      
      # update best fit if necessary
      if score > best_score:
        self.best = fit
        best_score = score
      
      self.scores.append([hp, score])
    
    # train the best fit
    self.best.fit(np.reshape(X, (-1, 1)), Y)
      
      
  def plot(self):
    """Plot accuracy as a function of hyperparameter values and best fit"""
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
        
    plt.xlabel(self.hp)
    plt.ylabel("accuracy")

    plt.plot(*zip(*self.scores))

    plt.subplot(1, 2, 2)

    X_test = np.arange(0.0, 1.0, 0.01)[:, np.newaxis]
    Y_test = self.best.predict(X_test)

    plt.scatter(self.X, self.Y, color='b', marker='.', label="Training data")
    plt.plot(X_test, X_test * X_test, 'g', label="True distribution")    
    plt.plot(X_test, Y_test, 'r', label="Decision tree")

    plt.legend()

Traning dataset

X = np.random.sample(200)
Y = np.array([x**2 + np.random.normal(0, 0.05) for x in X])

max_depth

tree_handler = TreeCV(X, Y)
tree_handler.cross_me(*range(1, 10))
tree_handler.plot()

min_samples_leaf

tree_handler.set_method("min_samples_leaf")
tree_handler.cross_me(*range(1, 10))
tree_handler.plot()

min_impurity_split

# min_impurity_split is depracated so lets disable warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

tree_handler.set_method("min_impurity_split")
tree_handler.cross_me(*np.arange(0.0, 5e-3, 1e-4))
tree_handler.plot()

min_impurity_decrease

tree_handler.set_method("min_impurity_decrease")
tree_handler.cross_me(*np.arange(0.0, 5e-4, 1e-5))
tree_handler.plot()

Bias-Variance trade-off

        +================+================+
       /\                |                /\
      /  \               |               /  \
     /    \              |              /    \
    /      \             |             /      \
   /        \            |            /        \
  / variance \           |           /   bias   \
  ^^^^^^^^^^^^           |           ^^^^^^^^^^^^
                         |
                         |
                         |
overfitting   <----------+--------->   underfitting

    Bias is an error coming from wrong model assumptions, which do not allow an algorithm to learn all patterns from training data.

    Variance is an error coming from sensivity to features specific for training data.

    High bias leads to underfitting and high variance to overfitting.

    Total error also depends on irreducible error (noise that can not be reduced by algorithm)

    Ultmiate goal is to minimize the total error

# fake bias, variance and noise
complexity = np.arange(1, 2, 0.1)
variance = np.power(complexity, 5)
bias2 = variance[::-1]
irreducible = [10*np.random.normal(abs(x - 1.5), 0.01) for x in complexity]

# total error = variance + bias^2 + irreducible
total = variance + bias2 + irreducible

plt.xticks([])
plt.yticks([])

plt.xlabel("Algorithm complexity")
plt.ylabel("Error")

plt.plot(complexity, variance, 'C0o-', label='Variance')
plt.plot(complexity, bias2, 'C1o-', label="Bias^2")
plt.plot(complexity, total, 'C2o-', label="Total = Bias^2 + Variance + Irreducible error")

plt.plot([1.5, 1.5], [0, 25], 'C3--')

plt.text(1.0, 7, "$\longleftarrow$ better chance of generalizing", color='C0')
plt.text(1.6, 7, "better chance of approximating $\longrightarrow$", color='C1')

plt.legend()
plt.show()

    Decision trees are sensitive to splits - small changes in training data may change a tree structure

        deep trees tend to have high variance and low bias

        shallow trees tend to have low variance and high bias

Quick math
Basic

    The general goal of regression is to find how some dependent variable (target, 

) is changing when independent variable (feature,

) varies

Lets assume there is some true relationship describing this dependence

We want to find
from observations of

pairs

Although, in real life we get some noisy observation, so

As we do not know function
we want to approximate it with some other function

(estimator)

In general,

is a parametrized model which can take many possible functional form

    e.g.

        can take different coefficients (based on a training dataset)

Bias and variance

    Lets imagine there are 

possible training datasets

For a given dataset one gets an estimators

Lets denote the expected estimator by

If

is large we can approximate it by an average over all datasets (law of large numbers)



The variance of an estimator tells us how far particular predictions are from the mean value



Thus, if the training does not depend on the choice of a dataset the variance is low

The bias of an estimator tells us how far the mean value is from the true value



Thus, if the model decribes data accurately the bias is low

Please note the hidden assumption that all possible values of

    are equally likely

Goodness of a model

    The common practice to determine the goodness of a model fit is to calculate mean squared error

    The mean squared error is, well, the mean value of error squared:



Lets consider MSE for a particlar point
,

, so



Here, we used the linearity of the expected value operator. Lets use another common property:

So the first term can be rewritten in the form



And the last term



Here, we used the fact that

(noise would average out when averaging over infinite number of datasets)

For the middle term we use the fact that for independent
and : , so

Taking all together we get



Example

    Lets consider 

With a noise given by a zero-mean Gaussian with a variance

So the observation

from math import sin, cos, pi, exp

def get_dataset(N=20, sigma=0.1):
  """Generate N training samples"""
  # X is a set of random points from [-1, 1]
  X = 2 * np.random.sample(N) - 1
  # Y are corresponding target values (with noise included)
  Y = np.array([sin(pi*x) + np.random.normal(0, sigma) for x in X])
  
  return X, Y

# plot a sample
X, Y = get_dataset()

x_ = np.arange(-1, 1, 0.01)

plt.scatter(X, Y, color='C1')
plt.plot(x_, np.sin(np.pi * x_), 'C0--')
plt.show()

    We do not know 

We assume it is a polynomial

Lets consider polynomials of orders:

    ...

Lets assume we have 100 independent dataset

Each one has 20 points

# generate 100 datasets with default settings
datasets = [get_dataset() for i in range(100)]

# and plot them all together with true signal
for i in range(100):
  plt.scatter(datasets[i][0], datasets[i][1], marker='.')

plt.plot(x_, np.sin(np.pi * x_), 'C0--')
plt.show()

    Now we need to fit each polynomial to each dataset separately

def get_fit(N, data):
  """Find a fit of polynomial of order N to data = (X, Y)"""
  return np.poly1d(np.polyfit(data[0], data[1], N))

# for the whole range of possible polynomials orders
# create a list of fits to different datasets
fits = [[get_fit(order, data) for data in datasets] for order in range(1, 10)]

plt.figure(figsize=(13, 10))

for order in range(1, 10):
  plt.subplot(3, 3, order)
  plt.ylim([-1.5,1.5])

  for g in fits[order - 1]:
    plt.plot(x_, g(x_), 'C1-', linewidth=0.1)

  plt.plot(x_, np.sin(np.pi * x_), 'C0--')
  
  plt.title("Polynomial of order {}".format(order))
  plt.show()
  
plt.tight_layout()
plt.show()

Training and test errors

    In real life is impossible (unless one creates data by hand) to calculate true variance and bias

    One would need all possible datasets 

and all possible input values

    Thus, usually one looks at training and test errors

        Training error is measured on the data used to make a fit

        Test/validation error is measured on unseen data

# fake error
complexity = np.arange(0.1, 2, 0.1)
train_error = -np.log(complexity)
test_error = -np.log(complexity) + np.power(complexity, 1)

plt.xticks([])
plt.yticks([])

plt.xlabel("Algorithm complexity")
plt.ylabel("Error")

plt.plot(complexity, train_error, 'C0o-', label='Training error')
plt.plot(complexity, test_error, 'C1o-', label="Test error")

plt.text(0.1, 0.25, "$\longleftarrow$ high bias", color='C0')
plt.text(1.5, 0.25, "high variance $\longrightarrow$", color='C1')

plt.legend()
plt.show()

    High training error indicates high bias (which means underfitting)

    Training error must decrease with model complexity

    If the training error is high:

        Use more complex model (or new model architecture)

        Use more features - maybe there is just not enough information to make a good prediction

        Train longer (if the algorithm is an iterative optimization problem)

        Decrease regularization (next lecture)

    Test error deacreses with model complexity up to a point when algorithm is to sensitive to features seen in training data

    If test error starts to increase it indicates high variance (which means overfitting)

    If test error is high:

        Use more data - easy to say hard to do...

        Use less features

        Increase regularization

        Use different model

Ensemble learning

    Lets first define a weak learner as a classifier which is just slighlty better than random guessing

    The idea behind ensemble learning is to create a strong learner as a combination of many weak learners

    We will discuss two popular ensemble methods:

        Bagging (bootstrap aggregating), e.g. random forest

        Boosting, e.g. boosted decision tress

Random forest

    Once we know a way to produce a tree we can create a forest

    And each tree contributes to a final prediction

    It is a random forest, because each tree is randomly incomplete - trained only on a random subsets of samples and features (features bagging)

    The final prediction of a random forest is an avearge predictions (for regression) or a majority vote (classification)

Intuitive / naive example

    Imagine you want to go to a cinema and need to choose a movie to watch

    You can ask a friend about the recommendation

        She/he would ask you about movies you watched in the past

        and (based on your answers) create a set of rules (a decision tree)

        to finally recommend you a movie (make a prediction)

    Alternatively, you can ask many friends for an advice

        Each friend would ask you random questions to give an answer

        At the end, you choose a movie with most votes

The algorithm

    Lets imagine we have 

samples in our dataset (e.g.

movies you watched)

Each sample has

features (e.g. do you like a movie? do you like the leading actor / actress or director?)

To create a tree take
random samples from the dataset and at each node select features (

    ) to find the best predictor

    Repeat the procedure for next trees until you reach desired size of a forest

                    +------------+
                    |            |
                    |   Dataset  |
         +----------+            +----------+
         |          | N features |          |
         |          |            |          |
         v          +------------+          v                    Hyperparameters:

+-----------------+                 +-----------------+
|                 |                 |                 |
| Random subset 1 |      . . .      | Random subset T |
|                 |                 |                 |              - the number of trees
|   N features    |                 |   N features    |              - the size of subsets
|                 |                 |                 |
+--------+--------+                 +--------+--------+
         |                                   |
         v                                   v

+-----------------+                 +-----------------+
|                 |                 |                 |
|     Tree 1      |      . . .      |     Tree T      |
|                 |                 |                 |
+--------+--------+                 +-----------------+
         |
         |          +-------------+          +--------+
         |          |             |          |        |
         +--------> | M1 features +--------> | Node 1 |              - the number of random features
         |          |             |          |        |              - the size of a single tree
         |          +-------------+          +--------+
         |
         |          +-------------+          +--------+
         |          |             |          |        |
         +--------> | M2 features +--------> | Node 2 |
         |          |             |          |        |
         |          +-------------+          +--------+

                           .
                           .
                           .

Boosted trees

    The idea is similar to bagging

    The key differences are:

        Data is reweighted every time a weak learner is added (so future learners focus on misclassified samples)

        The final prediction is weighted average (better classifiers have higher weights)

                            Bagging (parallel)

       +--------------------+                +----------------+
       |                    |                |                |
+----> |      Dataset       +--------------> | Weak learner 1 |
|      |                    |                |                |
|      +--------------------+                +----------------+
|
|
|      +--------------------+                +----------------+
|      |                    |                |                |
+----> |      Dataset       +------------->  | Weak learner 2 |
|      |                    |                |                |
|      +--------------------+       .        +----------------+
|                                   .
|                                   .
|      +--------------------+                +----------------+
|      |                    |                |                |
+----> |      Dataset       +------------->  | Weak learner N |
       |                    |                |                |
       +--------------------+                +----------------+

                          Boosting (sequential)

      +--------------------+                +----------------+
      |                    |                |                |
      |      Dataset       +--------------> | Weak learner 1 |
      |                    |                |                |
      +--------------------+                +--------+-------+
                                                     |
                +------------------------------------+
                |
                v

      +--------------------+                +----------------+
      |                    |                |                |
      | Reweighted dataset +------------->  | Weak learner 2 |
      |                    |                |                |
      +--------------------+                +--------+-------+
                                                     |
                +------------     . . .      --------+
                |
                v

      +--------------------+                +----------------+
      |                    |                |                |
      | Reweighted dataset +------------->  | Weak learner N |
      |                    |                |                |
      +--------------------+                +----------------+
                                                                        

AdaBoost

    AdaBoost is on of the most famous algorithms in machine learning

    Y. Freund and R. Schapire got a Gödel Prize for this

    Lets consider 

labled training examples
, where
and

The initial distribution is initizlized with
, where

(so every sample is equaly likely)

For

:

    train a weak learner using

,

choose the one which minimizes the weighted error

calculate

For

update weights according to

is a normilization factor so

is a distribution

The final hyptohesis

is computes the sign of a weighted combination of weak hypotheses

Out-of-bag error

    Out-of-bag (OOB) error may be used for machine learning models using bootstrap aggregation (like random forest and boosted trees) instead of cross-validation

    Bagging involves random sampling with replacement

    Some samples are not used in the training process (out-of-bag samples) and therefore can be used to calculate test error

    OOB error is the average error over all training samples calculated using predictions from weak classifiers which do not contain particular sample in their bootstrap samples

Example

    Lets consider some fake data generated with make_blobs from scikit-learn

    and then apply decision trees with different maximum depths

    and random forests with different maximum depths

Dataset

    sklearn.datasets.make_blobs allows to generate random Gaussian blobs

    We generate 8 blobs with fixed random generator (just to make sure we get the same set every time)

from sklearn.datasets import make_blobs

# generate 5 blobs with fixed random generator
X, Y = make_blobs(n_samples=500, centers=8, random_state=300)

plt.scatter(*X.T, c=Y, marker='.', cmap='Dark2')
plt.show()

Train and visualize

    To make our life easier we create a function to

        plot training data on existing axes or new one (if not provided)

        train given classifier on given dataset

        create countours representing predictions of the classifier

def train_and_look(classifier, X, Y, ax=None, title='', cmap='Dark2'):
  """Train classifier on (X,Y). Plot data and prediction."""
  # create new axis if not provided
  ax = ax or plt.gca()
  plt.show()
  
  ax.set_title(title)
    
  # plot training data
  ax.scatter(*X.T, c=Y, marker='.', cmap=cmap)
  
  # train a cliassifier
  classifier.fit(X, Y)

  # create a grid of testing points
  x_, y_ = np.meshgrid(np.linspace(*ax.get_xlim(), num=200),
                       np.linspace(*ax.get_ylim(), num=200))

  # convert to an array of 2D points
  test_data = np.vstack([x_.ravel(), y_.ravel()]).T
  
  # make a prediction and reshape to grid structure 
  z_ = classifier.predict(test_data).reshape(x_.shape)
  
  # arange z bins so class labels are in the middle
  z_levels = np.arange(len(np.unique(Y)) + 1) - 0.5
  
  # plot contours corresponding to classifier prediction
  ax.contourf(x_, y_, z_, alpha=0.25, cmap=cmap, levels=z_levels)

    Let check how it works on a decision tree classifier with default sklearn setting

from sklearn.tree import DecisionTreeClassifier as DT

train_and_look(DT(), X, Y)

Decision tree

    We consider decision trees with fixed maximum depths from 1 to 9

# create a figure with 9 axes 3x3
fig, ax = plt.subplots(3, 3, figsize=(15,15))

# train and look at decision trees with different max depth
for max_depth in range(0, 9):
  train_and_look(DT(max_depth=max_depth + 1), X, Y,
                 ax=ax[max_depth // 3][max_depth % 3],
                 title="Max depth = {}".format(max_depth + 1))

    max_depth <= 3 - undefitting
    max_depth <= 6 - quite good
    max_depth > 6 - overfitting

Random forest

    Lets do the same with random forests (100 trees in each forest)

from sklearn.ensemble import RandomForestClassifier as RF

# create a figure with 9 axes 3x3
fig, ax = plt.subplots(3, 3, figsize=(15,15))

# train and look at decision trees with different max depth
for max_depth in range(0, 9):
  train_and_look(RF(n_estimators=100, max_depth=max_depth + 1), X, Y,
                 ax=ax[max_depth // 3][max_depth % 3],
                 title="Max depth = {}".format(max_depth + 1))

    The combination of shallow trees (weak learners) does a good job

    Overfitting is somehow prevented

Summary

    The most important lesson today: bias-variance trade-off

        For the lecture easy examples are chosen so they can be visualize

        In real life problems, it is hard / impossible to determine using "bye eye" method if the model is underfitted or overfitted

        Note, that actually you should never used this method even if you think "your eye" is right - you would be surprised how it is not

        One needs a way to measure the goodnes of a model - usually mean squared error

        In practice, most people use cross-calidation technique

    The biggest advantages of decision trees algoritms is that they are east to interpret (it is easy to explain even to non-experts how they work, which is not the case with e.g. deep neural networks)

    Usually, decision trees are used as weak learners in ensemble learning

    The most famous boosting algorithm is AdaBoost, because it is a good one and the first one. Although, there are many other boosting methods on market right now with XGBoost being one of the most popular one

    As for today, deep learning has better publicity, but boosted trees are still one of the most common algorithms used in Kaggle competitions

    Boosted trees are also popular among physicist and used by them as an alternative to neural networks for experimental elementary particle physics in event reconstruction procedures


'''

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
