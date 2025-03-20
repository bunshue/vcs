"""
machine_learning_Read_data_various_sources01

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

# How to read data from different text based (and non-text based) sources

df1 = pd.read_csv("data/CSV_EX_1.csv")

df1

# Read data from a CSV where headers are missing

df2 = pd.read_csv("data/CSV_EX_2.csv")
df2

df2 = pd.read_csv("data/CSV_EX_2.csv", header=None)
df2

df2 = pd.read_csv(
    "data/CSV_EX_2.csv", header=None, names=["Bedroom", "Sq.ft", "Locality", "Price($)"]
)
df2

# Read data from a CSV where delimiters/separators are not comma

df3 = pd.read_csv("data/CSV_EX_3.csv")
df3

df3 = pd.read_csv("data/CSV_EX_3.csv", sep=";")
df3

# How to bypass given headers with your own?

df4 = pd.read_csv("data/CSV_EX_1.csv", names=["A", "B", "C", "D"])
df4

df4 = pd.read_csv("data/CSV_EX_1.csv", header=0, names=["A", "B", "C", "D"])
df4

# Skip initial rows

df5 = pd.read_csv("data/CSV_EX_skiprows.csv")
df5

df5 = pd.read_csv("data/CSV_EX_skiprows.csv", skiprows=2)
df5

# Skip footers

df6 = pd.read_csv("data/CSV_EX_skipfooter.csv")
df6

df6 = pd.read_csv(
    "data/CSV_EX_skipfooter.csv", skiprows=2, skipfooter=1, engine="python"
)
df6

# Read only first n rows (especially useful for large files)

df7 = pd.read_csv("data/CSV_EX_1.csv", nrows=2)
df7

# How to combine skiprows and nrows to read data in small chunks

# List where DataFrames will be stored
list_of_dataframe = []
# Number of rows to be read in one chunk
rows_in_a_chunk = 10
# Number of chunks to be read (this many separate DataFrames will be produced)
num_chunks = 5
# Dummy DataFrame to get the column names
df_dummy = pd.read_csv("data/Boston_housing.csv", nrows=2)
colnames = df_dummy.columns
# Loop over the CSV file to read only specified number of rows at a time
# Note how the iterator variable i is set up inside the range
for i in range(0, num_chunks * rows_in_a_chunk, rows_in_a_chunk):
    df = pd.read_csv(
        "data/Boston_housing.csv",
        header=0,
        skiprows=i,
        nrows=rows_in_a_chunk,
        names=colnames,
    )
    list_of_dataframe.append(df)

list_of_dataframe[0]

list_of_dataframe[1]

# Setting the option skip_blank_lines

df9 = pd.read_csv("data/CSV_EX_blankline.csv")
df9

df9 = pd.read_csv("data/CSV_EX_blankline.csv", skip_blank_lines=False)
df9

# Read CSV from inside a compressed (.zip/.gz/.bz2/.xz) file

# df10 = pd.read_csv('data/CSV_EX_1.zip')
# df10

# Reading from an Excel file - how to use sheet_name

df11_1 = pd.read_excel("data/Housing_data.xlsx", sheet_name="Data_Tab_1")
df11_2 = pd.read_excel("data/Housing_data.xlsx", sheet_name="Data_Tab_2")
df11_3 = pd.read_excel("data/Housing_data.xlsx", sheet_name="Data_Tab_3")

df11_1.shape

# (9, 14)

df11_2.shape

# (4, 14)

df11_3.shape

# (16, 14)

# If sheet_name is set to None then an Ordered Dictionary of DataFrame is returned if the Excel file has distinct sheets

dict_df = pd.read_excel("data/Housing_data.xlsx", sheet_name=None)

dict_df.keys()

# odict_keys(['Data_Tab_1', 'Data_Tab_2', 'Data_Tab_3'])

# General delimated text file can be read same as a CSV

df13 = pd.read_table("data/Table_EX_1.txt")
df13

df13 = pd.read_table("data/Table_EX_1.txt", sep=",")
df13

df13 = pd.read_table(
    "data/Table_tab_separated.txt",
)
df13

# Read HTML tables directly from an URL

url = "http://www.fdic.gov/bank/individual/failed/banklist.html"
list_of_df = pd.read_html(url)

df14 = list_of_df[0]
df14.head()

# Mostly, read_html returns more than one table and further wrangling is needed to get the desired data

list_of_df = pd.read_html(
    "https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table", header=0
)

len(list_of_df)

# 6

for t in list_of_df:
    print(t.shape)

df15 = list_of_df[1]
df15.head()

"""
# Read in a JSON file

df16 = pd.read_json("movies.json")

df16.head()

df16[df16["title"] == "The Avengers"]["cast"]

cast_of_avengers = df16[(df16["title"] == "The Avengers") & (df16["year"] == 2012)][
    "cast"
]

print(list(cast_of_avengers))

# [['Robert Downey, Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Tom Hiddleston', 'Clark Gregg', 'Cobie Smulders', 'Stellan SkarsgÃ¥rd', 'Samuel L. Jackson']]
"""

"""
# Read Stata file (.dta)

df17 = pd.read_stata("data/rscfp2016.dta")

df17.head()
"""

"""
# Read tabular data from PDF file using the Tabula-py package
# For more information about tabula-py, please see this link: https://github.com/chezou/tabula-py

from tabula import read_pdf

df18_1 = read_pdf("data/Housing_data.pdf", pages=[1], pandas_options={"header": None})

df18_1

df18_2 = read_pdf("data/Housing_data.pdf", pages=[2], pandas_options={"header": None})

df18_2

df18 = pd.concat([df18_1, df18_2], axis=1)

df18

# With PDF extraction, most of the time, headres will be difficult to extract automatically. You have to pass on the list of headres as the names argument in the read-pdf function as pandas_option,

names = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
    "PRICE",
]

df18_1 = read_pdf(
    "data/Housing_data.pdf",
    pages=[1],
    pandas_options={"header": None, "names": names[:10]},
)
df18_2 = read_pdf(
    "data/Housing_data.pdf",
    pages=[2],
    pandas_options={"header": None, "names": names[10:]},
)
df18 = pd.concat([df18_1, df18_2], axis=1)

df18

# Exercise 19: In a complex page, you may have multiple tables and use Tabula to extract a list of DataFrames and then process the DataFrames further

list_of_tables = read_pdf("data/WDI-2016.pdf", pages=70, multiple_tables=True)

type(list_of_tables)

# list

list_of_tables[1].head(10)

df19 = list_of_tables[1]
df19.columns = [
    "Country",
    "Population",
    "Surface area",
    "Population density",
    "Urban pop %",
    "GNI Atlas Method (Billions)",
    "GNI Atlas Method (Per capita)",
    "Purchasing power (Billions)",
    "Purchasing power (Per capita)",
    "GDP % growth",
    "GDP per capita growth",
]
df19.head(10)
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
