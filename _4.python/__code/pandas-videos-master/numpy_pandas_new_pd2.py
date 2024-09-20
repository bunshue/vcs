"""
numpy的使用

numpy: 數值計算的標準套件
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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import pandas as pd
cc = pd.__version__

print(cc)

print('pd直接讀取網頁上的資料')
# read a dataset of Chipotle orders directly from a URL and store the results in a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')

print('檢視前幾行')
cc = orders.head()
print(cc)

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

print('檢視前幾行')
cc = users.head()
print(cc)


print("------------------------------------------------------------")  # 60個

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_table('http://bit.ly/uforeports', sep=',')

# read_csv is equivalent to read_table, except it assumes a comma separator
ufo = pd.read_csv('http://bit.ly/uforeports')

print('檢視前幾行')
cc = ufo.head()
print(cc)

# select the 'City' Series using bracket notation
ufo['City']

# or equivalently, use dot notation
cc = ufo.City
print(cc)

# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo['Location'] = ufo.City + ', ' + ufo.State
cc = ufo.head()
print(cc)


print("------------------------------------------------------------")  # 60個

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')

# example method: show the first 5 rows
cc = movies.head()
print(cc)

# example method: calculate summary statistics
cc = movies.describe() # 方法有()
print(cc)

# example attribute: number of rows and columns
cc = movies.shape # 屬性無()
print(cc)

# example attribute: data type of each column
cc = movies.dtypes
print(cc)

# use an optional parameter to the describe method to summarize only 'object' columns
cc = movies.describe(include=['object'])
print(cc)

print("------------------------------------------------------------")  # 60個

print('rename pd 之 df')

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')

print('檢查欄名')
cc = ufo.columns
print(cc)

#Index([u'City', u'Colors Reported', u'Shape Reported', u'State', u'Time'], dtype='object')

# rename two of the columns by using the 'rename' method
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
cc = ufo.columns
print(cc)

#Index([u'City', u'Colors_Reported', u'Shape_Reported', u'State', u'Time'], dtype='object')

#Documentation for rename

# replace all of the column names by overwriting the 'columns' attribute
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols

print(ufo.columns)


# replace the column names during the file reading process by using the 'names' parameter
ufo = pd.read_csv('http://bit.ly/uforeports', header=0, names=ufo_cols)
cc = ufo.columns
print(cc)

#Index([u'city', u'colors reported', u'shape reported', u'state', u'time'], dtype='object')

#Documentation for read_csv

# replace all spaces with underscores in the column names by using the 'str.replace' method
ufo.columns = ufo.columns.str.replace(' ', '_')
cc = ufo.columns

print(cc)

print("------------------------------------------------------------")  # 60個

#How do I remove columns from a pandas DataFrame? (video)

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
cc = ufo.head()
print(cc)

# remove a single column (axis=1 refers to columns)
ufo.drop('Colors Reported', axis=1, inplace=True)
cc = ufo.head()
print(cc)

# remove multiple columns at once
ufo.drop(['City', 'State'], axis=1, inplace=True)
cc = ufo.head()
print(cc)

# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
cc = ufo.head()
print(cc)

print("------------------------------------------------------------")  # 60個

#How do I sort a pandas DataFrame or a Series? (video)

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
cc = movies.head()
print(cc)

# sort the 'title' Series in ascending order (returns a Series)
cc = movies.title.sort_values().head()
print(cc)

# sort in descending order instead
cc = movies.title.sort_values(ascending=False).head()
print(cc)

# sort the entire DataFrame by the 'title' Series (returns a DataFrame)
cc = movies.sort_values('title').head()
print(cc)

# sort in descending order instead
cc = movies.sort_values('title', ascending=False).head()
print(cc)

# sort the DataFrame first by 'content_rating', then by 'duration'
cc = movies.sort_values(['content_rating', 'duration']).head()
print(cc)

print("------------------------------------------------------------")  # 60個

#How do I filter rows of a pandas DataFrame by column value? (video)

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
cc = movies.head()
print(cc)

# examine the number of rows and columns
cc = movies.shape
print(cc)

# create a list in which each element refers to a DataFrame row: True if the row satisfies the condition, False otherwise
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

# confirm that the list has the same length as the DataFrame
cc = len(booleans)
print(cc)

# examine the first five list elements
cc = booleans[0:5]
print(cc)

# convert the list to a Series
is_long = pd.Series(booleans)
cc = is_long.head()
print(cc)

# use bracket notation with the boolean Series to tell the DataFrame which rows to display
cc = movies[is_long]
print(cc)

# simplify the steps above: no need to write a for loop to create 'is_long' since pandas will broadcast the comparison
is_long = movies.duration >= 200
cc = movies[is_long]
print(cc)

# or equivalently, write it in one line (no need to create the 'is_long' object)
cc = movies[movies.duration >= 200]
print(cc)

# select the 'genre' Series from the filtered DataFrame
cc = movies[movies.duration >= 200].genre
print(cc)

# or equivalently, use the 'loc' method
cc = movies.loc[movies.duration >= 200, 'genre']
print(cc)


print("------------------------------------------------------------")  # 60個


#9. How do I apply multiple filter criteria to a pandas DataFrame? (video)

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
cc = movies.head()
print(cc)

# filter the DataFrame to only show movies with a 'duration' of at least 200 minutes
cc = movies[movies.duration >= 200]
print(cc)


# CORRECT: use the '&' operator to specify that both conditions are required
cc = movies[(movies.duration >=200) & (movies.genre == 'Drama')]
print(cc)

# 錯誤
# INCORRECT: using the '|' operator would have shown movies that are either long or dramas (or both)
cc = movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()
print(cc)

# use the '|' operator to specify that a row can match any of the three criteria
cc = movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')].head(10)
print(cc)

# or equivalently, use the 'isin' method
cc = movies[movies.genre.isin(['Crime', 'Drama', 'Action'])].head(10)
print(cc)

print("------------------------------------------------------------")  # 60個

# read a dataset of UFO reports into a DataFrame, and check the columns
ufo = pd.read_csv('http://bit.ly/uforeports')
cc = ufo.columns
print(cc)

# specify which columns to include by name
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])
print(ufo)

# or equivalently, specify columns by position
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0, 4])
cc = ufo.columns
print(cc)

# 只讀一部份
# specify how many rows to read
ufo = pd.read_csv('http://bit.ly/uforeports', nrows=3)
print(ufo)


# Series are directly iterable (like a list)
for c in ufo.City:
    print(c)


# various methods are available to iterate through a DataFrame
for index, row in ufo.iterrows():
    print(index, row.City, row.State)

#Question: How do I drop all non-numeric columns from a DataFrame?

# read a dataset of alcohol consumption into a DataFrame, and check the data types
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
cc = drinks.dtypes
print(cc)

# only include numeric columns in the DataFrame
import numpy as np
cc = drinks.select_dtypes(include=[np.number]).dtypes
print(cc)


# describe all of the numeric columns
drinks.describe()


# pass the string 'all' to describe all columns
drinks.describe(include='all')

# pass a list of data types to only describe certain types
drinks.describe(include=['object', 'float64'])

# pass a list even if you only want to describe a single data type
drinks.describe(include=['object'])

print("------------------------------------------------------------")  # 60個

print('使用 axis')

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
cc = drinks.head()
print(cc)

# drop a column (temporarily)
drinks.drop('continent', axis=1).head()

# drop a row (temporarily)
drinks.drop(2, axis=0).head()

"""
# calculate the mean of each numeric column
#cc = drinks.mean()  NG
#print(cc)

# or equivalently, specify the axis explicitly
drinks.mean(axis=0)

# calculate the mean of each row
drinks.mean(axis=1).head()


# 'index' is an alias for axis 0
drinks.mean(axis='index')


# 'columns' is an alias for axis 1
drinks.mean(axis='columns').head()
"""

print("------------------------------------------------------------")  # 60個

#How do I use string methods in pandas? (video)

# read a dataset of Chipotle orders into a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()

# string methods for pandas Series are accessed via 'str'
orders.item_name.str.upper().head()




# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()

# use the boolean Series to filter the DataFrame
orders[orders.item_name.str.contains('Chicken')].head()

# string methods can be chained together
orders.choice_description.str.replace('[', '').str.replace(']', '').head()


# many pandas string methods support regular expressions (regex)
orders.choice_description.str.replace('[\[\]]', '').head()





print("------------------------------------------------------------")  # 60個

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()

# examine the data type of each Series
print('檢視資料型態')
cc = drinks.dtypes
print(cc)

# change the data type of an existing Series
drinks['beer_servings'] = drinks.beer_servings.astype(float)
drinks.dtypes

# alternatively, change the data type of a Series while reading in a file
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks.dtypes

# read a dataset of Chipotle orders into a DataFrame
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()

# examine the data type of each Series
cc = orders.dtypes
print(cc)

# convert a string to a number in order to do math
orders.item_price.str.replace('$', '').astype(float).mean()

# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()

# convert a boolean Series to an integer (False = 0, True = 1)
orders.item_name.str.contains('Chicken').astype(int).head()

print("------------------------------------------------------------")  # 60個

#When should I use a "groupby" in pandas? (video)

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()

"""
# calculate the mean beer servings across the entire dataset
drinks.beer_servings.mean()

# calculate the mean beer servings just for countries in Africa
drinks[drinks.continent=='Africa'].beer_servings.mean()

# calculate the mean beer servings for each continent
drinks.groupby('continent').beer_servings.mean()

# other aggregation functions (such as 'max') can also be used with groupby
drinks.groupby('continent').beer_servings.max()

# multiple aggregation functions can be applied simultaneously
drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max'])

# specifying a column to which the aggregation function should be applied is not required
drinks.groupby('continent').mean()

# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')

"""


print("------------------------------------------------------------")  # 60個

#How do I explore a pandas Series? (video)

# read a dataset of top-rated IMDb movies into a DataFrame
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

# examine the data type of each Series
cc = movies.dtypes
print(cc)

# count the non-null values, unique values, and frequency of the most common value
movies.genre.describe()

# count how many times each value in the Series occurs
movies.genre.value_counts()


# display percentages instead of raw counts
movies.genre.value_counts(normalize=True)

# 'value_counts' (like many pandas methods) outputs a Series
type(movies.genre.value_counts())

# thus, you can add another Series method on the end
movies.genre.value_counts().head()

# display the unique values in the Series
movies.genre.unique()


# count the number of unique values in the Series
movies.genre.nunique()

# compute a cross-tabulation of two Series
pd.crosstab(movies.genre, movies.content_rating)



# calculate various summary statistics
movies.duration.describe()

# many statistics are implemented as Series methods
cc = movies.duration.mean()
print(cc)

# 'value_counts' is primarily useful for categorical data, not numerical data
movies.duration.value_counts().head()


# histogram of the 'duration' Series (shows the distribution of a numerical variable)
movies.duration.plot(kind='hist')

plt.show()

# bar plot of the 'value_counts' for the 'genre' Series
movies.genre.value_counts().plot(kind='bar')

plt.show()

print("------------------------------------------------------------")  # 60個

#How do I handle missing values in pandas? (video)

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
cc = ufo.tail()
print(cc)


print('找出缺少資料的項目')
# 'isnull' returns a DataFrame of booleans (True if missing, False if not missing)
cc = ufo.isnull().tail()
print(cc)

print('找出缺少資料的項目')
# 'nonnull' returns the opposite of 'isnull' (True if not missing, False if missing)
cc = ufo.notnull().tail()
print(cc)

# count the number of missing values in each Series
ufo.isnull().sum()

# use the 'isnull' Series method to filter the DataFrame rows
ufo[ufo.City.isnull()].head()

# examine the number of rows and columns
cc = ufo.shape
print(cc)

# if 'any' values are missing in a row, then drop that row
ufo.dropna(how='any').shape

# 'inplace' parameter for 'dropna' is False by default, thus rows were only dropped temporarily
ufo.shape

# if 'all' values are missing in a row, then drop that row (none are dropped in this case)
ufo.dropna(how='all').shape

# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape

# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='all').shape

# 'value_counts' does not include missing values by default
ufo['Shape Reported'].value_counts().head()

# explicitly include missing values
ufo['Shape Reported'].value_counts(dropna=False).head()

# fill in missing values with a specified value
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)

# confirm that the missing values were filled in
ufo['Shape Reported'].value_counts().head()

print("------------------------------------------------------------")  # 60個

#pandas index

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()

# every DataFrame has an index (sometimes called the "row labels")
drinks.index

# column names are also stored in a special "index" object
drinks.columns

# neither the index nor the columns are included in the shape
drinks.shape

# index and columns both default to integers if you don't define them
pd.read_table('http://bit.ly/movieusers', header=None, sep='|').head()

# identification: index remains with each row when filtering the DataFrame
drinks[drinks.continent=='South America']

# selection: select a portion of the DataFrame using the index
drinks.loc[23, 'beer_servings']

# set an existing column as the index
drinks.set_index('country', inplace=True)
drinks.head()

# 'country' is now the index
drinks.index

# 'country' is no longer a column
drinks.columns

# 'country' data is no longer part of the DataFrame contents
drinks.shape

# country name can now be used for selection
drinks.loc['Brazil', 'beer_servings']

# index name is optional
drinks.index.name = None
drinks.head()

# restore the index name, and move the index back to a column
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
drinks.head()

# many DataFrame methods output a DataFrame
drinks.describe()

# you can interact with any DataFrame using its index and columns
cc = drinks.describe().loc['25%', 'beer_servings']
print(cc)

print("------------------------------------------------------------")  # 60個

#pandas index

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()

# every DataFrame has an index
cc = drinks.index
print(cc)
#RangeIndex(start=0, stop=193, step=1)

# every Series also has an index (which carries over from the DataFrame)
drinks.continent.head()

# set 'country' as the index
drinks.set_index('country', inplace=True)

# Series index is on the left, values are on the right
drinks.continent.head()

# another example of a Series (output from the 'value_counts' method)
drinks.continent.value_counts()

# access the Series index
drinks.continent.value_counts().index

# access the Series values
drinks.continent.value_counts().values

# elements in a Series can be selected by index (using bracket notation)
drinks.continent.value_counts()['Africa']

# any Series can be sorted by its values
drinks.continent.value_counts().sort_values()

# any Series can also be sorted by its index
drinks.continent.value_counts().sort_index()

# 'beer_servings' Series contains the average annual beer servings per person
drinks.beer_servings.head()



# create a Series containing the population of two countries
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
people

# calculate the total annual beer servings for each country
(drinks.beer_servings * people).head()

# concatenate the 'drinks' DataFrame with the 'population' Series (aligns by the index)
pd.concat([drinks, people], axis=1).head()

print("------------------------------------------------------------")  # 60個

#How do I select multiple rows and columns from a pandas DataFrame? (video)

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head(3)

# row 0, all columns
ufo.loc[0, :]

# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]

# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]

# this implies "all columns", but explicitly stating "all columns" is better
ufo.loc[0:2]

# rows 0 through 2 (inclusive), column 'City'
ufo.loc[0:2, 'City']

# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ['City', 'State']]

# accomplish the same thing using double brackets - but using 'loc' is preferred since it's more explicit
ufo[['City', 'State']].head(3)

# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, 'City':'State']

# accomplish the same thing using 'head' and 'drop'
ufo.head(3).drop('Time', axis=1)

# rows in which the 'City' is 'Oakland', column 'State'
ufo.loc[ufo.City=='Oakland', 'State']


# accomplish the same thing using "chained indexing" - but using 'loc' is preferred since chained indexing can cause problems
ufo[ufo.City=='Oakland'].State

# rows in positions 0 and 1, columns in positions 0 and 3
ufo.iloc[[0, 1], [0, 3]]

# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
ufo.iloc[0:2, 0:4]


# rows in positions 0 through 2 (exclusive), all columns
ufo.iloc[0:2, :]


# accomplish the same thing - but using 'iloc' is preferred since it's more explicit
ufo[0:2]

# read a dataset of alcohol consumption into a DataFrame and set 'country' as the index
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
drinks.head()


print("------------------------------------------------------------")  # 60個

#"inplace"

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()


ufo.shape


# remove the 'City' column (doesn't affect the DataFrame since inplace=False)
ufo.drop('City', axis=1).head()

# confirm that the 'City' column was not actually removed
ufo.head()

# remove the 'City' column (does affect the DataFrame since inplace=True)
ufo.drop('City', axis=1, inplace=True)

# confirm that the 'City' column was actually removed
ufo.head()


# drop a row if any value is missing from that row (doesn't affect the DataFrame since inplace=False)
ufo.dropna(how='any').shape

(2490, 4)

# confirm that no rows were actually removed
ufo.shape

(18241, 4)

# use an assignment statement instead of the 'inplace' parameter
ufo = ufo.set_index('Time')
ufo.tail()

# fill missing values using "backward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='bfill').tail()

# compare with "forward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='ffill').tail()


print("------------------------------------------------------------")  # 60個

# How do I make my pandas DataFrame smaller and faster? (video)

# read a dataset of alcohol consumption into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()

# exact memory usage is unknown because object columns are references elsewhere
drinks.info()

# force pandas to calculate the true memory usage
drinks.info(memory_usage='deep')



# calculate the memory usage for each Series (in bytes)
drinks.memory_usage(deep=True)


# use the 'category' data type (new in pandas 0.15) to store the 'continent' strings as integers
drinks['continent'] = drinks.continent.astype('category')
drinks.dtypes

# 'continent' Series appears to be unchanged
drinks.continent.head()



# strings are now encoded (0 means 'Africa', 1 means 'Asia', 2 means 'Europe', etc.)
drinks.continent.cat.codes.head()


# memory usage has been drastically reduced
drinks.memory_usage(deep=True)


# repeat this process for the 'country' Series
drinks['country'] = drinks.country.astype('category')
drinks.memory_usage(deep=True)


# memory usage increased because we created 193 categories
drinks.country.cat.categories

#字典轉df
# create a small DataFrame from a dictionary
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})
df

# sort the DataFrame by the 'quality' Series (alphabetical order)
df.sort_values('quality')

# sort the DataFrame by the 'quality' Series (logical order)
df.sort_values('quality')

# comparison operators work with ordered categories
df.loc[df.quality > 'good', :]

print("------------------------------------------------------------")  # 60個

#How do I use pandas with scikit-learn to create Kaggle submissions? (video)

# read the training dataset from Kaggle's Titanic competition into a DataFrame
train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()

# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ['Pclass', 'Parch']
X = train.loc[:, feature_cols]
X.shape

# create a response vector 'y' by selecting a Series
y = train.Survived
y.shape


# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, y)


# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv('http://bit.ly/kaggletest')
test.head()

# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
X_new.shape

# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)

# create a DataFrame of passenger IDs and testing set predictions
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).head()

# ensure that PassengerID is the first column by setting it as the index
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).set_index('PassengerId').head()

print('df轉csv')
pd.DataFrame({'PassengerId':test.PassengerId, 'Survived':new_pred_class}).set_index('PassengerId').to_csv('tmp_sub.csv')

print('df轉pickle')
train.to_pickle('tmp_train.pkl')

print('pickle轉df')
cc = pd.read_pickle('tmp_train.pkl').head()
print(cc)

print("------------------------------------------------------------")  # 60個

#How do I work with dates and times in pandas? (video)

# read a dataset of UFO reports into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()

# 'Time' is currently stored as a string
ufo.dtypes


# hour could be accessed using string slicing, but this approach breaks too easily
cc = ufo.Time.str.slice(-5, -3).astype(int).head()
print(cc)



# convert 'Time' to datetime format
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()

ufo.dtypes

# convenient Series attributes are now available
cc = ufo.Time.dt.hour.head()
print(cc)

""" NG
cc = ufo.Time.dt.weekday_name.head()
print(cc)
"""
cc = ufo.Time.dt.dayofyear.head()
print(cc)

# convert a single string to datetime format (outputs a timestamp object)
ts = pd.to_datetime('1/1/1999')
print(ts)


# compare a datetime Series with a timestamp
cc = ufo.loc[ufo.Time >= ts, :].head()
print(cc)

# perform mathematical operations with timestamps (outputs a timedelta object)
cc = ufo.Time.max() - ufo.Time.min()
print(cc)

#Timedelta('25781 days 01:59:00')

# timedelta objects also have attributes you can access
cc = (ufo.Time.max() - ufo.Time.min()).days
print(cc)
#25781L

# count the number of UFO reports per year
ufo['Year'] = ufo.Time.dt.year
cc = ufo.Year.value_counts().sort_index().head()
print(cc)

# plot the number of UFO reports per year (line plot is the default)
ufo.Year.value_counts().sort_index().plot()

#plt.show()

print("------------------------------------------------------------")  # 60個

#How do I create a pandas DataFrame from another object? (video)

# create a DataFrame from a dictionary (keys become column names, values become data)
df = pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'red']})
print(df)



# optionally specify the order of columns and define the index
df = pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'red']}, columns=['id', 'color'], index=['a', 'b', 'c'])
print(df)

# create a DataFrame from a list of lists (each inner list becomes a row)
pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color'])


# create a NumPy array (with shape 4 by 2) and fill it with random numbers between 0 and 1
import numpy as np
arr = np.random.rand(4, 2)
print(arr)



# create a DataFrame from the NumPy array
pd.DataFrame(arr, columns=['one', 'two'])

# create a DataFrame of student IDs (100 through 109) and test scores (random integers between 60 and 100)
pd.DataFrame({'student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101, 10)})

# 'set_index' can be chained with the DataFrame constructor to select an index
pd.DataFrame({'student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101, 10)}).set_index('student')


# create a new Series using the Series constructor
s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
print(s)

# concatenate the DataFrame and the Series (use axis=1 to concatenate columns)
pd.concat([df, s], axis=1)
print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
