import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.catplot(x="day", y="total_bill", data=df,
               kind="bar", col="sex")
plt.show()
