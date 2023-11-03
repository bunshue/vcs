import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.kdeplot(df["total_bill"], label="default")
sns.kdeplot(df["total_bill"], bw_adjust=2, label="bw_adjust: 2")
sns.kdeplot(df["total_bill"], bw_adjust=5, label="bw_adjust: 5")
plt.legend()
plt.show()
