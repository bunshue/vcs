import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.boxplot(x="petal_length", y="species", data=df)
plt.show()
