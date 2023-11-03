import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.displot(df["total_bill"], kde=True, rug=True)
plt.show()

