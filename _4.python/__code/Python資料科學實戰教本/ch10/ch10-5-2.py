import seaborn as sns

df = sns.load_dataset("iris")
print(df.head())
df.head().to_html("ch10-5-2.html")
