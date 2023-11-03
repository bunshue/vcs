import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("fmri")

sns.set()
sns.relplot(x="timepoint", y="signal", data=df, kind="line")

sns.relplot(x="timepoint", y="signal", ci=None, data=df, kind="line")
sns.relplot(x="timepoint", y="signal", ci="sd", data=df, kind="line")

sns.relplot(x="timepoint", y="signal", 
            estimator=None, data=df, kind="line")

plt.show()
