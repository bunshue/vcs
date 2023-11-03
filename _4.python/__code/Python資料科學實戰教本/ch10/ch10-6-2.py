import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.boxplot(x="species", y="petal_length", data=df)
plt.show()
