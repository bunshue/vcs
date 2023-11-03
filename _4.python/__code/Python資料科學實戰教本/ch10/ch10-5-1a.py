import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.histplot(df["total_bill"], kde=False)
sns.histplot(df["total_bill"], kde=False, bins=20, color="red")
sns.histplot(df["total_bill"], kde=False, bins=30, color="green")
plt.show()

