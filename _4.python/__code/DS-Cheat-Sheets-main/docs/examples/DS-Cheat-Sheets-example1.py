"""
DS-Cheat-Sheets-example1

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Array Manipulation

# Example values for arrays
a = np.array([3, 1, 2])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
h = np.array([[1, 2, 3], [4, 5, 6]])
g = np.array([7, 8, 9])
d = np.array([4, 5, 6])
e = np.array([10, 11])
f = np.array([12, 13])
c = np.array([(3, 1, 2), (6, 4, 5)], dtype=int)

# Transposing Array
transposed_b = np.transpose(b)
transposed_b_T = transposed_b.T

# Changing Array Shape
flattened_h = h.ravel()
reshaped_g = g.reshape(3, -2)

# Adding/Removing Elements
resized_h = np.resize(h, (2, 6))  # Using np.resize to avoid the error
appended_array = np.append(h, g)
inserted_array = np.insert(a, 1, 5)
deleted_array = np.delete(a, [1])

# Combining Arrays
concatenated_arrays = np.concatenate((a, d), axis=0)
vstacked_arrays = np.vstack((a, b))
hstacked_arrays = np.hstack((e, f))
column_stacked_arrays = np.column_stack((a, d))
c_stacked_arrays = np.c_[a, d]

# Splitting Arrays
hsplit_array = np.hsplit(a, 3)
vsplit_array = np.vsplit(c, 2)

print("transposed_b:")
print(transposed_b)

print("\ntransposed_b_T:")
print(transposed_b_T)

print("\nflattened_h:")
print(flattened_h)

print("\nreshaped_g:")
print(reshaped_g)

print("\nresized_h:")
print(resized_h)

print("\nappended_array:")
print(appended_array)

print("\ninserted_array:")
print(inserted_array)

print("\ndeleted_array:")
print(deleted_array)

print("\nconcatenated_arrays:")
print(concatenated_arrays)

print("\nvstacked_arrays:")
print(vstacked_arrays)

print("\nhstacked_arrays:")
print(hstacked_arrays)

print("\ncolumn_stacked_arrays:")
print(column_stacked_arrays)

print("\nc_stacked_arrays:")
print(c_stacked_arrays)

print("\nhsplit_array:")
print(hsplit_array)

print("\nvsplit_array:")
print(vsplit_array)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Saving & Loading

# On Disk

# Save a NumPy array to a file
a = np.array([1, 2, 3])
np.save("my_array", a)

# Save multiple NumPy arrays to a compressed file
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
np.savez("array.npz", a=a, b=b)

# Load a NumPy array from a file
loaded_array = np.load("my_array.npy")
"""
# Text Files

# Load data from a text file
loaded_txt = np.loadtxt("myfile.txt")

# Load data from a CSV file with specified delimiter
loaded_csv = np.genfromtxt("my_file.csv", delimiter=",")

# Save a NumPy array to a text file
a = np.array([1, 2, 3])
np.savetxt("myarray.txt", a, delimiter=" ")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Polars

import polars as pl

# Creating/reading DataFrames

# Create DataFrame
df = pl.DataFrame(
    {
        "nrs": [1, 2, 3, None, 5],
        "names": ["foo", "ham", "spam", "egg", None],
        "random": [0.3, 0.7, 0.1, 0.9, 0.6],
        "groups": ["A", "A", "B", "C", "B"],
    }
)

"""
# Read CSV
df = pl.read_csv("data/iris.csv", has_header=True)
print(df)
"""
"""
# Read parquet
df = pl.read_parquet("path.parquet", columns=["select", "columns"])
"""

# Expressions

# Polars expressions can be performed in sequence. This improves readability of code.

df.filter(pl.col("nrs") < 4).group_by("groups").agg(pl.all().sum())

# Subset Observations - rows

# Filter: Extract rows that meet logical criteria.
df.filter(pl.col("random") > 0.5)
df.filter((pl.col("groups") == "B") & (pl.col("random") > 0.5))

# Sample
# Randomly select fraction of rows.
#df.sample(frac=0.5)

# Randomly select n rows.
df.sample(n=2)

# Select first n rows
df.head(n=2)

# Select last n rows.
df.tail(n=2)

# Subset Variables - columns

# Select multiple columns with specific names.
df.select(["nrs", "names"])

# Select columns whose name matches regular expression regex.
df.select(pl.col("^n.*$"))

# Subsets - rows and columns

# Select rows 2-4.
df[2:4, :]

# Select columns in positions 1 and 3 (first column is 0).
df[:, [1, 3]]

# Select rows meeting logical condition, and only the specific columns.
# NG df[df["random"] > 0.5, ["names", "groups"]]

# Reshaping Data – Change layout, sorting, renaming

df2 = pl.DataFrame(
    {
        "nrs": [6],
        "names": ["wow"],
        "random": [0.9],
        "groups": ["B"],
    }
)

df3 = pl.DataFrame(
    {
        "primes": [2, 3, 5, 7, 11],
    }
)

# Append rows of DataFrames.
pl.concat([df, df2])

# Append columns of DataFrames
pl.concat([df, df3], how="horizontal")

# Gather columns into rows
# NG df.melt(id_vars="nrs", value_vars=["names", "groups"])

# Spread rows into columns
df.pivot(values="nrs", index="groups", columns="names")

# Order rows by values of a column (low to high)
df.sort("random")

# Order rows by values of a column (high to low)
df.sort("random")

# Rename the columns of a DataFrame
df.rename({"nrs": "idx"})

# Drop columns from DataFrame
df.drop(["names", "random"])

# Summarize Data

# Count number of rows with each unique value of variable
df["groups"].value_counts()

# # of rows in DataFrame
len(df)
# or
df.height

# Tuple of # of rows, # of columns in DataFrame
df.shape

# # of distinct values in a column
df["groups"].n_unique()

# Basic descriptive and statistics for each column
df.describe()

# Aggregation functions
df.select(
    [
        # Sum values
        pl.sum("random").alias("sum"),
        # Minimum value
        pl.min("random").alias("min"),
        # Maximum value
        pl.max("random").alias("max"),
        # or
        pl.col("random").max().alias("other_max"),
        # Standard deviation
        pl.std("random").alias("std_dev"),
        # Variance
        pl.var("random").alias("variance"),
        # Median
        pl.median("random").alias("median"),
        # Mean
        pl.mean("random").alias("mean"),
        # Quantile
        pl.quantile("random", 0.75).alias("quantile_0.75"),
        # or
        pl.col("random").quantile(0.75).alias("other_quantile_0.75"),
        # First value
        pl.first("random").alias("first"),
    ]
)

# Group Data

# Group by values in column named "col", returning a GroupBy object
df.group_by("groups")

# All of the aggregation functions from above can be applied to a group as well
df.group_by(by="groups").agg(
    [
        # Sum values
        pl.sum("random").alias("sum"),
        # Minimum value
        pl.min("random").alias("min"),
        # Maximum value
        pl.max("random").alias("max"),
        # or
        pl.col("random").max().alias("other_max"),
        # Standard deviation
        pl.std("random").alias("std_dev"),
        # Variance
        pl.var("random").alias("variance"),
        # Median
        pl.median("random").alias("median"),
        # Mean
        pl.mean("random").alias("mean"),
        # Quantile
        pl.quantile("random", 0.75).alias("quantile_0.75"),
        # or
        pl.col("random").quantile(0.75).alias("other_quantile_0.75"),
        # First value
        pl.first("random").alias("first"),
    ]
)

# Additional GroupBy functions
df.group_by(by="groups").agg(
    [
        # Count the number of values in each group
        pl.count("random").alias("size"),
        # Sample one element in each group
        # NG pl.col("names").apply(lambda group_df: group_df.sample(1)),
    ]
)

# Handling Missing Data

# Drop rows with any column having a null value
df.drop_nulls()

# Replace null values with given value
df.fill_null(42)

# Replace null values using forward strategy
df.fill_null(strategy="forward")
# Other fill strategies are "backward", "min", "max", "mean", "zero" and "one"

# Replace floating point NaN values with given value
df.fill_nan(42)

# Make New Columns

# Add a new column to the DataFrame
df.with_columns((pl.col("random") * pl.col("nrs")).alias("product"))

# Add several new columns to the DataFrame
df.with_columns(
    [
        (pl.col("random") * pl.col("nrs")).alias("product"),
        # pl.col("names").str.lengths().alias("names_lengths"),
    ]
)

# Add a column at index 0 that counts the rows
df.with_row_count()

# Rolling Functions

# The following rolling functions are available

df.select(
    [
        pl.col("random"),
        # Rolling maximum value
        pl.col("random").rolling_max(window_size=2).alias("rolling_max"),
        # Rolling mean value
        pl.col("random").rolling_mean(window_size=2).alias("rolling_mean"),
        # Rolling median value
        pl.col("random")
        .rolling_median(window_size=2, min_periods=2)
        .alias("rolling_median"),
        # Rolling minimum value
        pl.col("random").rolling_min(window_size=2).alias("rolling_min"),
        # Rolling standard deviation
        pl.col("random").rolling_std(window_size=2).alias("rolling_std"),
        # Rolling sum values
        pl.col("random").rolling_sum(window_size=2).alias("rolling_sum"),
        # Rolling variance
        pl.col("random").rolling_var(window_size=2).alias("rolling_var"),
        # Rolling quantile
        pl.col("random")
        .rolling_quantile(quantile=0.75, window_size=2, min_periods=2)
        .alias("rolling_quantile"),
        # Rolling skew
        pl.col("random").rolling_skew(window_size=2).alias("rolling_skew"),
        # Rolling custom function
        pl.col("random")
        .rolling_map(function=np.nanstd, window_size=2)
        .alias("rolling_apply"),
    ]
)

# Window functions

# Window functions allow to group by several columns simultaneously
df.select(
    [
        "names",
        "groups",
        pl.col("random").sum().over("names").alias("sum_by_names"),
        pl.col("random").sum().over("groups").alias("sum_by_groups"),
    ]
)

# Combine Data Sets

df4 = pl.DataFrame(
    {
        "nrs": [1, 2, 5, 6],
        "animals": ["cheetah", "lion", "leopard", "tiger"],
    }
)

# Inner join
# Retains only rows with a match in the other set.
df.join(df4, on="nrs")
# or
df.join(df4, on="nrs", how="inner")

# Left join
# Retains each row from "left" set (df).
df.join(df4, on="nrs", how="left")

# Outer join
# Retains each row, even if no other matching row exists.
df.join(df4, on="nrs", how="outer")

# Anti join
# Contains all rows from df that do not have a match in df4.
df.join(df4, on="nrs", how="anti")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Pandas

# Pandas Data Structures

# Series

# A one-dimensional labeled array a capable of holding any data type.

# Create a pandas Series
s = pd.Series(
    [3, -5, 7, 4],
    index=['a', 'b', 'c', 'd']
)

# Print the pandas Series
print("s:", s)

# DataFrame

# two-dimensional labeled data structure with columns of potentially different types.

# Create a pandas DataFrame
data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasília'],
    'Population': [11190846, 1303171035, 207847528]
}
df = pd.DataFrame(
    data,
    columns=['Country', 'Capital', 'Population']
)

# Print the DataFrame 'df'
print("df:", df)

# Getting Elements

# Get one element from a Series
s['b']

# Get subset of a DataFrame
df[1:]

# Selecting, Boolean Indexing & Setting

# Select single value by row & 'Belgium' column
df.iloc[[0],[0]]
# Output: 'Belgium'

# Select single value by row & 'Belgium' column labels
df.loc[[0], ['Country']]
# Output: 'Belgium'

# Select single row of subset of rows
df.loc[2]
# Output:
# Country     Brazil
# Capital    Brasília
# Population 207847528

# Select a single column of subset of columns
df.loc[:,'Capital']
# Output:
# 0     Brussels
# 1    New Delhi
# 2     Brasília

# Boolean indexing - Series s where value is not > 1
s[~(s > 1)]

# Boolean indexing - s where value is <-1 or >2
s[(s < -1) | (s > 2)]

# Use filter to adjust DataFrame
df[df['Population'] > 1200000000]

# Setting index a of Series s to 6
s['a'] = 6
s

# Dropping

# Drop values from rows (axis=0)
s.drop(['a', 'c'])

# Drop values from columns (axis=1)
df.drop('Country', axis=1)

# Sort & Rank

# Sort by labels along an axis
df.sort_index()

# Sort by the values along an axis
df.sort_values(by='Country')

# Assign ranks to entries
df.rank()

# Applying Functions

# Define a function
f = lambda x: x*2

# Apply function to DataFrame
df.apply(f)

# Apply function element-wise
df.applymap(f)

# Basic Information

# Get the shape (rows, columns)
df.shape

# Describe index
df.index

# Describe DataFrame columns
df.columns

# Info on DataFrame
df.info()

# Number of non-NA values
df.count()

# Summary

# Sum of values
sum_values = df['Population'].sum()

# Cumulative sum of values
cumulative_sum_values = df['Population'].cumsum()

# Minimum/maximum values
min_values = df['Population'].min()
max_values = df['Population'].max()

# Index of minimum/maximum values
idx_min_values = df['Population'].idxmin()
idx_max_values = df['Population'].idxmax()

# Summary statistics
summary_stats = df['Population'].describe()

# Mean of values
mean_values = df['Population'].mean()

# Median of values
median_values = df['Population'].median()

print("Example DataFrame:")
print(df)

print("\nSum of values:")
print(sum_values)

print("\nCumulative sum of values:")
print(cumulative_sum_values)

print("\nMinimum values:")
print(min_values)

print("\nMaximum values:")
print(max_values)

print("\nIndex of minimum values:")
print(idx_min_values)

print("\nIndex of maximum values:")
print(idx_max_values)

print("\nSummary statistics:")
print(summary_stats)

print("\nMean values:")
print(mean_values)

print("\nMedian values:")
print(median_values)

# Internal Data Alignment

# Create Series with different indices
s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
s3

# Add two Series with different indices
result = s + s3
result

# Arithmetic Operations with Fill Methods

# Example Series
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
s3 = pd.Series([10, 2, 4, 8], index=['a', 'b', 'd', 'e'])

# Perform arithmetic operations with fill methods
result_add = s.add(s3, fill_value=0)
result_sub = s.sub(s3, fill_value=2)
result_div = s.div(s3, fill_value=4)
result_mul = s.mul(s3, fill_value=3)

print("result_add:")
print(result_add)

print("\nresult_sub:")
print(result_sub)

print("\nresult_div:")
print(result_div)

print("\nresult_mul:")
print(result_mul)

# Asking For Help

# Display help for a function or object
help(pd.Series.loc)

# Read and Write

# CSV

"""
# Read from CSV
df_read = pd.read_csv(
    'file.csv',
     header=None, 
     nrows=5
)
"""

# Write to CSV
df.to_csv('myDataFrame.csv')

# Excel

# Read from Excel
# df_read_excel = pd.read_excel('file.xlsx')

# Write to Excel
df.to_excel(
    'tmp_myDataFrame.xlsx', 
    sheet_name='Sheet1'
)

"""
# Read multiple sheets from the same file
xlsx = pd.ExcelFile('file.xls')
df_from_sheet1 = pd.read_excel(xlsx, 'Sheet1')
"""

""" SQL
# SQL Query

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')

# Read from SQL Query
pd.read_sql("SELECT * FROM my_table;", engine)

# Read from Database Table
pd.read_sql_table('my_table', engine)

# Read from SQL Query using read_sql_query()
pd.read_sql_query("SELECT * FROM my_table;", engine)

# Write DataFrame to SQL Table
pd.to_sql('myDf', engine)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
