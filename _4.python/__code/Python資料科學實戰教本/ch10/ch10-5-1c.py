import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.histplot(df["total_bill"], kde=True)
plt.show()

