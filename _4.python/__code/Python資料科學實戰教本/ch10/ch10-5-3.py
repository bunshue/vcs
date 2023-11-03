import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.pairplot(df)
plt.show()
