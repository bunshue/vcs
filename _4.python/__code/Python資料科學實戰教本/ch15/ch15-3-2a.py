import pandas as pd
import numpy as np

raw_df = pd.read_csv("boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
print(X.head())
X.head().to_html("ch15-3-2a-01.html")
print("---------------------------")
target = pd.DataFrame(target, columns=["MEDV"])
print(target.head())
target.head().to_html("ch15-3-2a-02.html")