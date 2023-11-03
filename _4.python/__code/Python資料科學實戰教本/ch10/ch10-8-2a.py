import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("anscombe")

sns.set()
sns.lmplot(x="x", y="y", data=df.query("dataset=='II'"), order=2)
plt.show()
