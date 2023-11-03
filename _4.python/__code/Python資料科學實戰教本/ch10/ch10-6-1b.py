import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.swarmplot(x="species", y="sepal_length", data=df)
plt.show()
