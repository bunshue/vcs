import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

iris.boxplot(column="sepal_length",
             by="target",
             figsize=(6,5))
plt.show()
