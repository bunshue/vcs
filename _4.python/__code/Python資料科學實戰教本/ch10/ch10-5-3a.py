import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.pairplot(df, kind="scatter", diag_kind="kde",
             hue="species", palette="husl")
plt.show()
