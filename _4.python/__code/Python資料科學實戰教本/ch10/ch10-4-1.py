import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.relplot(x="total_bill", y="tip", data=df)
plt.show()
