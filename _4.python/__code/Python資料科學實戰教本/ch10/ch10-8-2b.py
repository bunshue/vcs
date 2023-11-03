import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("anscombe")

sns.set()
sns.residplot(x="x", y="y", data=df.query("dataset=='III'"))
plt.show()
