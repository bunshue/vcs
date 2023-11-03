import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.jointplot(x="petal_length", y="petal_width", kind="hex", data=df)
plt.show()
