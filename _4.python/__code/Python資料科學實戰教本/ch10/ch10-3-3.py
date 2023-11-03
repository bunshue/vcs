import seaborn as sns

df = sns.load_dataset("tips")
print(df.head())
df.head().to_html("ch10-3-3.html")


