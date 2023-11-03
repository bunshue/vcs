import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("anscombe")

sns.set()
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, height=4)
plt.show()
