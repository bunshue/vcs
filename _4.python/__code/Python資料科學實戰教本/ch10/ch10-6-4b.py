import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.catplot(x="sex", y="total_bill", data=df,
               kind="bar", col="day", col_wrap=2)
plt.show()
