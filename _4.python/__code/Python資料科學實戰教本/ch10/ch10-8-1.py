import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.regplot(x="total_bill", y="tip", data=df)
sns.lmplot(x="total_bill", y="tip", data=df)
plt.show()
