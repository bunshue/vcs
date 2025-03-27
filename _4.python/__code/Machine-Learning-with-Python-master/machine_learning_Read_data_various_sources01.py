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

# Pandas vs. PyArrow file reading speed comparison

import pyarrow.parquet as pq
import matplotlib as mpl
mpl.rcParams['figure.dpi']=125

# Create CSV files of various sizes

for i in range(1,11):
    a = np.random.normal(size=(int(5325*i), int(1e2)))
    df = pd.DataFrame(a, columns=["C" + str(i) for i in range(100)])
    fname = "tmp_test"+str(i)+".csv"
    df.to_csv(fname)
    print(f"Size of file with {5325*i} rows: {round(os.path.getsize(fname)/(1024*1024),3)} MB")

# Create Parquet (compressed) files from the same CSV files

for i in range(1,11):
    fname = "tmp_test"+str(i)+".csv"
    parquet_name = "tmp_test"+str(i)+"_parquet.zip"
    df = pd.read_csv(fname)
    df.to_parquet(parquet_name,compression="gzip")
    print(f"Created {parquet_name}")

#The directory should look like this now...

#Reading speed of CSV (in Pandas) and Parquet files (with PyArrow)

t_read_pd,t_read_arrow = [],[]

for i in range(1,11):
    fname = "tmp_test"+str(i)+".csv"
    parquet_name = "tmp_test"+str(i)+"_parquet.zip"
    t1 = time.time()
    df1 = pd.read_csv(fname)
    t2 = time.time()
    delta_t = round((t2 - t1), 3)
    t_read_pd.append(delta_t)
    t1 = time.time()
    df2 = pq.read_table(parquet_name)
    t2 = time.time()
    delta_t = round((t2 - t1), 3)
    t_read_arrow.append(delta_t)
    print(f"Done for file # {i}")

t_read_pd = np.array(t_read_pd)
t_read_arrow = np.array(t_read_arrow)

plt.figure(figsize=(11, 5))
plt.plot(
    [10*i for i in range(1, 11)], t_read_pd/t_read_arrow, "bo--", linewidth=2, markersize=8
)
plt.grid(True)
plt.title(
    "Ratio of Pandas to Arrow time to read files with increasing size",
    fontsize=16,
)
plt.xticks([10*i for i in range(1, 11)],fontsize=14)
plt.xlabel("Size (MB)", fontsize=14)
plt.ylabel("Ratio of Pandas/Arrow read time", fontsize=14)
show()

# What's the order of read time? Seconds, milliseconds?

t1 = time.time()
df1 = pd.read_csv("tmp_test10.csv", usecols=["C1", "C99"])
t2 = time.time()
delta_t = round((t2 - t1), 3)
print(
    "Time taken to read 2 columns of a 100 MB (53250 rows) CSV file with Pandas:",
    delta_t,
    "seconds",
)

# Time taken to read 2 columns of a 100 MB (53250 rows) CSV file with Pandas: 1.114 seconds

# The reading speed of the 100 MB CSV file with pd.read_csv() is about 1.114 seconds.

df1.head()


t1 = time.time()
df2 = pq.read_table("tmp_test10_parquet.zip", columns=["C1", "C99"])
t2 = time.time()
delta_t = round((t2 - t1), 3)
print(
    "Time taken to read 2 columns of the identical 53250 rows zipped parquet file with PyArrow:",
    delta_t,
    "seconds",
)

# Time taken to read 2 columns of the identical 53250 rows zipped parquet file with PyArrow: 0.026 seconds

# The reading speed of the same file (in the parquet gzipped version) with pq.read_table() is about 0.026 seconds!

# Convert from PyArrow table to dataframe
df3 = df2.to_pandas()
df3.head()

#The dataframes df1 and df3 are the same, as expected.

#Reading a small number of columns is much faster with Arrow

all_cols = ["C" + str(i) for i in range(100)]
t_pandas, t_arrow = [], []
for i in range(2, 100, 2):
    cols = list(np.random.choice(all_cols, size=i))
    t1 = time.time()
    df1 = pd.read_csv("tmp_test10.csv", usecols=cols)
    t2 = time.time()
    delta_t_pandas = round((t2 - t1), 3)
    t_pandas.append(delta_t_pandas)
    t1 = time.time()
    df2 = pq.read_table("tmp_test10_parquet.zip", columns=cols)
    t2 = time.time()
    delta_t_arrow = round((t2 - t1), 3)
    t_arrow.append(delta_t_arrow)
    print(f"Done for {i} columns")

t_pandas = np.array(t_pandas)
t_arrow = np.array(t_arrow)

plt.figure(figsize=(11, 5))
plt.plot(
    [i for i in range(2, 100, 2)], t_pandas / t_arrow, "bo--", linewidth=2, markersize=8
)
plt.grid(True)
plt.title(
    "Ratio of Pandas to Arrow time to read a 100 MB CSV file with increasing # of columns",
    fontsize=15,
)
plt.xticks([i for i in range(0, 100, 10)],fontsize=14)
plt.xlabel("No. of columns", fontsize=14)
plt.ylabel("Ratio of Pandas/Arrow read time", fontsize=14)
show()

# PyArrow (Parquet) reading time varies with sparsity in the file

pct_nan = []
for i in range(11,21):
    a = np.random.normal(size=(int(5325*5), int(1e2)))
    cutoff = -2+0.4*(i-11)
    a = np.where(a < cutoff, np.nan, a)
    p_nan = round(100*np.count_nonzero(np.isnan(a))/a.size,2)
    pct_nan.append(p_nan)
    df = pd.DataFrame(a, columns=["C" + str(i) for i in range(100)])
    fname = "tmp_test"+str(i)+".csv"
    df.to_csv(fname)
    print(f"NaN-filled file written with {p_nan}%")

for i in range(11,21):
    fname = "tmp_test"+str(i)+".csv"
    parquet_name = "tmp_test"+str(i)+"_parquet.zip"
    df = pd.read_csv(fname)
    df.to_parquet(parquet_name,compression="gzip")
    print(f"Created {parquet_name}")

t_read_nan = []
# m_read_nan = []

for i in range(11,21):
    parquet_name = "tmp_test"+str(i)+"_parquet.zip"
    t1 = time.time()
    df2 = pq.read_table(parquet_name)
    t2 = time.time()
    delta_t = round(1000*(t2 - t1), 3)
    t_read_nan.append(delta_t)
    # m_read_nan.append()
    print(f"Done for file # {i}")
t_read_nan=np.array(t_read_nan)

plt.figure(figsize=(11, 5))
plt.plot(pct_nan,t_read_nan, "bo--", linewidth=2, markersize=8)
plt.grid(True)
plt.title("PyArrow (Parquet) reading time varies with sparsity in the file",fontsize=16,)
#plt.xticks([10*i for i in range(1, 11)],fontsize=14)
plt.xlabel("Sparsity (% of NaN values)", fontsize=14)
plt.ylabel("Read time (milliseconds)", fontsize=14)
plt.ylim(int(t_read_nan.min()*0.9),int(t_read_nan.max()*1.1))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PDF table reading and processing demo

# Read tabular data from a PDF report of World Bank for doing some analysis

from tabula import read_pdf

# Define a list of page numbers to read
pages_to_read = [68,69,70,71,72]

column_names = ['Country','Population','Surface area','Population density','Urban pop %',
                'GNI Atlas Method (Billions)','GNI Atlas Method (Per capita)','Purchasing power (Billions)',
                'Purchasing power (Per capita)','GDP % growth', 'GDP per capita growth']

# Test a PDF table extraction by using the read_pdf function from Tabula

lst_tbl1=read_pdf("data/WDI-2016.pdf",pages=70,multiple_tables=True)

cc = len(lst_tbl1)
print(cc)

cc = lst_tbl1[0]
print(cc)

lst_tbl1[1]

# It looks like that the 2nd element of the list is the table we want to extract. Let's assign it to a DataFrame and check first few rows using head method

df = lst_tbl1[1]

df.head()

# You should observe that the column headers are just numbers. Here, we need to use the defined list of variables we created earlier. Assign that list as column names of this DataFrame.

df.columns = column_names

df.head()

# Next, write a loop to create such DataFrames by reading data tables from the pages 68-72 of the PDF file. You can store those DataFrames in a list for concatenating later.

# Empty list to store DataFrames
list_of_df = []
# Loop for reading tables from the PDF file page by page
for pg in pages_to_read:
    lst_tbl=read_pdf("data/WDI-2016.pdf",pages=pg,multiple_tables=True)
    df = lst_tbl[1]
    df.columns=column_names
    list_of_df.append(df)
    print("Finished processing page: {}".format(pg))

# Examine individual DataFrames from the list. Does the last DataFrame look alright?

list_of_df[4]

# Concetenate all the DataFrames in the list into a single DataFrame so that we can use it for further wrangling and analysis.

df = pd.concat(list_of_df,axis=0)

df.shape

df.head()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
