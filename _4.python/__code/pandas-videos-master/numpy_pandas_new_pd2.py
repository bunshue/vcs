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
'''
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

# merge DataFrames

print('電影資料')
movie_cols = ['movie_id', 'title']
movies = pd.read_table('data/u.item', sep='|', header=None, names=movie_cols, usecols=[0, 1])
cc = movies.head()
print(cc)

cc = movies.shape
print(cc)

cc = movies.movie_id.nunique()
print(cc)

#Ratings

rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('data/u.data', sep='\t', header=None, names=rating_cols)
cc = ratings.head()
print(cc)

cc = ratings.shape
print(cc)

cc = ratings.movie_id.nunique()
print(cc)

cc = ratings.loc[ratings.movie_id == 1, :].head()
print(cc)

#Merging Movies and Ratings

cc = movies.columns
print(cc)

#Index(['movie_id', 'title'], dtype='object')

cc = ratings.columns
print(cc)

#Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')

movie_ratings = pd.merge(movies, ratings)
cc = movie_ratings.columns
print(cc)

#Index(['movie_id', 'title', 'user_id', 'rating', 'timestamp'], dtype='object')

cc = movie_ratings.head()
print(cc)

cc = movie_ratings.shape
print(cc)

print(movies.shape)
print(ratings.shape)
print(movie_ratings.shape)

print('3個df都不一樣大')

movies.columns = ['m_id', 'title']
cc = movies.columns
print(cc)

#Index(['m_id', 'title'], dtype='object')

cc = ratings.columns
print(cc)

#Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')

cc = pd.merge(movies, ratings, left_on='m_id', right_on='movie_id').head()
print(cc)



#What if you want to join on one index?

movies = movies.set_index('m_id')
cc = movies.head()
print(cc)

cc = pd.merge(movies, ratings, left_index=True, right_on='movie_id').head()
print(cc)


#What if you want to join on two indexes?

ratings = ratings.set_index('movie_id')
cc = ratings.head()
print(cc)

cc = pd.merge(movies, ratings, left_index=True, right_index=True).head()
print(cc)

print("------------------------------------------------------------")  # 60個

#Four Types of Joins

A = pd.DataFrame({'color': ['green', 'yellow', 'red'], 'num':[1, 2, 3]})

B = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size':['S', 'M', 'L']})

print("Inner join")
#Only include observations found in both A and B:
cc = pd.merge(A, B, how='inner')
print(cc)

print("Outer join")
#Include observations found in either A or B:
cc = pd.merge(A, B, how='outer')
print(cc)

print("Left join")
#Include all observations found in A:
cc = pd.merge(A, B, how='left')
print(cc)

print("Right join")
#Include all observations found in B:
cc = pd.merge(A, B, how='right')
print(cc)

print("------------------------------------------------------------")  # 60個

print("Create a datetime column from a DataFrame")

# create an example DataFrame
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],
                  columns=['month', 'day', 'year', 'hour'])
print(df)

# new: create a datetime column from the entire DataFrame
print(pd.to_datetime(df))

# new: create a datetime column from a subset of columns
print(pd.to_datetime(df[['month', 'day', 'year']]))

print(df)

print("------------------------------------------------------------")  # 60個

print("Create a category column during file reading")

# read the drinks dataset into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
cc = drinks.head()
print(cc)


# data types are automatically detected
cc = drinks.dtypes
print(cc)


# old way to create a category (after file reading)
drinks['continent'] = drinks.continent.astype('category')
cc = drinks.dtypes
print(cc)

# new way to create a category (during file reading)
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'continent':'category'})
cc = drinks.dtypes
print(cc)

print("------------------------------------------------------------")  # 60個

print("Convert the data type of multiple columns at once")

# read the drinks dataset into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
cc = drinks.dtypes
print(cc)

# old way to convert data types (one at a time)
drinks['beer_servings'] = drinks.beer_servings.astype('float')
drinks['spirit_servings'] = drinks.spirit_servings.astype('float')
cc = drinks.dtypes
print(cc)

# new way to convert data types (all at once)
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = drinks.astype({'beer_servings':'float', 'spirit_servings':'float'})
cc = drinks.dtypes
print(cc)

print("------------------------------------------------------------")  # 60個

print("Apply multiple aggregations on a Series or DataFrame")

# example of a single aggregation function after a groupby
cc = drinks.groupby('continent').beer_servings.mean()
print(cc)


# multiple aggregation functions can be applied simultaneously
cc = drinks.groupby('continent').beer_servings.agg(['mean', 'min', 'max'])
print(cc)


# new: apply the same aggregations to a Series
cc = drinks.beer_servings.agg(['mean', 'min', 'max'])
print(cc)


""" NG
# new: apply the same aggregations to a DataFrame
cc = drinks.agg(['mean', 'min', 'max'])
print(cc)
"""

# DataFrame describe method provides similar functionality but is less flexible
cc = drinks.describe()
print(cc)

'''

print("------------------------------------------------------------")  # 60個

#Load example datasets

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
movies = pd.read_csv('http://bit.ly/imdbratings')
orders = pd.read_csv('http://bit.ly/chiporders', sep='\t')
orders['item_price'] = orders.item_price.str.replace('$', '').astype('float')
stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
titanic = pd.read_csv('http://bit.ly/kaggletrain')
ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])

cc = pd.__version__
print(cc)

cc = pd.show_versions()
print(cc)

#2. Create an example DataFrame

df = pd.DataFrame({'col one':[100, 200], 'col two':[300, 400]})
print(df)

cc = pd.DataFrame(np.random.rand(4, 8))
print(cc)

cc = pd.DataFrame(np.random.rand(4, 8), columns=list('abcdefgh'))
print(cc)

#3. Rename columns

# 承上 df
print(df)

df = df.rename({'col one':'col_one', 'col two':'col_two'}, axis='columns')
print(df)

cc = df.columns = ['col_one', 'col_two']
print(cc)

# replace

cc = df.columns = df.columns.str.replace(' ', '_')
print(cc)

print(df)

cc = df.add_prefix('X_')
print(cc)

cc = df.add_suffix('_Y')
print(cc)


#4. Reverse row order

#the drinks DataFrame:

cc = drinks.head()
print(cc)

cc = drinks.loc[::-1].head()
print(cc)

cc = drinks.loc[::-1].reset_index(drop=True).head()
print(cc)

#5. Reverse column order

cc = drinks.loc[:, ::-1].head()
print(cc)

#6. Select columns by data type

#the drinks DataFrame:

cc = drinks.dtypes
print(cc)

cc = drinks.select_dtypes(include='number').head()
print(cc)

cc = drinks.select_dtypes(include='object').head()
print(cc)

cc = drinks.select_dtypes(include=['number', 'object', 'category', 'datetime']).head()
print(cc)

cc = drinks.select_dtypes(exclude='number').head()
print(cc)

#7. Convert strings to numbers

df = pd.DataFrame({'col_one':['1.1', '2.2', '3.3'],
                   'col_two':['4.4', '5.5', '6.6'],
                   'col_three':['7.7', '8.8', '-']})
print(df)

print(df.dtypes)

cc = df.astype({'col_one':'float', 'col_two':'float'}).dtypes
print(cc)

cc = pd.to_numeric(df.col_three, errors='coerce')
print(cc)

cc = pd.to_numeric(df.col_three, errors='coerce').fillna(0)
print(cc)

df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
print(df)

print(df.dtypes)

#8. Reduce DataFrame size

cc = drinks.info(memory_usage='deep')
print(cc)

cols = ['beer_servings', 'continent']
small_drinks = pd.read_csv('http://bit.ly/drinksbycountry', usecols=cols)
small_drinks.info(memory_usage='deep')

dtypes = {'continent':'category'}
smaller_drinks = pd.read_csv('http://bit.ly/drinksbycountry', usecols=cols, dtype=dtypes)
smaller_drinks.info(memory_usage='deep')

#9. Build a DataFrame from multiple files (row-wise)

cc = pd.read_csv('data/stocks1.csv')
print(cc)

#Here's the second day:

cc = pd.read_csv('data/stocks2.csv')
print(cc)

#And here's the third day:

cc = pd.read_csv('data/stocks3.csv')
print(cc)

from glob import glob

stock_files = sorted(glob('data/stocks*.csv'))
print(stock_files)

#['data/stocks1.csv', 'data/stocks2.csv', 'data/stocks3.csv']

cc = pd.concat((pd.read_csv(file) for file in stock_files))
print(cc)

#Unfortunately, there are now duplicate values in the index. To avoid that, we can tell the concat() function to ignore the index and instead use the default integer index:

cc = pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True)
print(cc)

#10. Build a DataFrame from multiple files (column-wise)

cc = pd.read_csv('data/drinks1.csv').head()
print(cc)

cc = pd.read_csv('data/drinks2.csv').head()
print(cc)

drink_files = sorted(glob('data/drinks*.csv'))

cc = pd.concat((pd.read_csv(file) for file in drink_files), axis='columns').head()
print(cc)

#11. Create a DataFrame from the clipboard

df = pd.read_clipboard()
print(df)

print(df.dtypes)

df = pd.read_clipboard()
print(df)

#Amazingly, pandas has even identified the first column as the index:

print(df.index)

#Index(['Alice', 'Bob', 'Charlie'], dtype='object')


#12. Split a DataFrame into two random subsets

cc = len(movies)
print(cc)

#We can use the sample() method to randomly select 75% of the rows and assign them to the "movies_1" DataFrame:

movies_1 = movies.sample(frac=0.75, random_state=1234)

#Then we can use the drop() method to drop all rows that are in "movies_1" and assign the remaining rows to "movies_2":

movies_2 = movies.drop(movies_1.index)

#You can see that the total number of rows is correct:

cc = len(movies_1) + len(movies_2)
print(cc)

#And you can see from the index that every movie is in either "movies_1":

cc = movies_1.index.sort_values()
print(cc)

cc = movies_2.index.sort_values()

#Keep in mind that this approach will not work if your index values are not unique.


#13. Filter a DataFrame by multiple categories

#the movies DataFrame:

cc = movies.head()
print(cc)

#One of the columns is genre:
cc = movies.genre.unique()
print(cc)

cc = movies[(movies.genre == 'Action') |
       (movies.genre == 'Drama') |
       (movies.genre == 'Western')].head()

print(cc)

cc = movies[movies.genre.isin(['Action', 'Drama', 'Western'])].head()
print(cc)

#And if you want to reverse this filter, so that you are excluding (rather than including) those three genres, you can put a tilde in front of the condition:

cc = movies[~movies.genre.isin(['Action', 'Drama', 'Western'])].head()
print(cc)


#14. Filter a DataFrame by largest categories

counts = movies.genre.value_counts()
print(counts)

cc = counts.nlargest(3)
print(cc)

#And all we actually need from this Series is the index:
cc = counts.nlargest(3).index
print(cc)

#Finally, we can pass the index object to isin(), and it will be treated like a list of genres:

cc = movies[movies.genre.isin(counts.nlargest(3).index)].head()
print(cc)

#15. Handle missing values

#Let's look at a dataset of UFO sightings:

cc = ufo.head()
print(cc)

cc = ufo.isna().sum()
print(cc)

cc = ufo.isna().mean()
print(cc)

cc = ufo.dropna(axis='columns').head()
print(cc)

cc = ufo.dropna(thresh=len(ufo)*0.9, axis='columns').head()
print(cc)

#len(ufo) returns the total number of rows, and then we multiply that by 0.9 to tell pandas to only keep columns in which at least 90% of the values are not missing.

#16. Split a string into multiple columns

df = pd.DataFrame({'name':['John Arthur Doe', 'Jane Ann Smith'],
                   'location':['Los Angeles, CA', 'Washington, DC']})
print(df)

cc = df.name.str.split(' ', expand=True)
print(cc)

df[['first', 'middle', 'last']] = df.name.str.split(' ', expand=True)
print(df)

cc = df.location.str.split(', ', expand=True)
print(cc)

df['city'] = df.location.str.split(', ', expand=True)[0]
print(df)

#17. Expand a Series of lists into a DataFrame

#Let's create another example DataFrame:

df = pd.DataFrame({'col_one':['a', 'b', 'c'], 'col_two':[[10, 40], [20, 50], [30, 60]]})
print(df)

df_new = df.col_two.apply(pd.Series)
print(df_new)

cc = pd.concat([df, df_new], axis='columns')
print(cc)

#18. Aggregate by multiple functions

#Let's look at a DataFrame of orders from the Chipotle restaurant chain:

cc = orders.head(10)
print(cc)

cc = orders[orders.order_id == 1].item_price.sum()
print(cc)

cc = orders.groupby('order_id').item_price.sum().head()
print(cc)

cc = orders.groupby('order_id').item_price.agg(['sum', 'count']).head()
print(cc)

#19. Combine the output of an aggregation with a DataFrame

cc = orders.head(10)
print(cc)

cc = orders.groupby('order_id').item_price.sum().head()
print(cc)

#In other words, the output of the sum() function:

cc = len(orders.groupby('order_id').item_price.sum())
print(cc)

cc = len(orders.item_price)
print(cc)

total_price = orders.groupby('order_id').item_price.transform('sum')
cc = len(total_price)
print(cc)

orders['total_price'] = total_price
cc = orders.head(10)
print(cc)

orders['percent_of_total'] = orders.item_price / orders.total_price
cc = orders.head(10)
print(cc)

#20. Select a slice of rows and columns

#Let's take a look at another dataset:

cc = titanic.head()
print(cc)

cc = titanic.describe()
print(cc)

cc = titanic.describe().loc['min':'max']
print(cc)

cc = titanic.describe().loc['min':'max', 'Pclass':'Parch']
print(cc)

#21. Reshape a MultiIndexed Series

cc = titanic.Survived.mean()
print(cc)

#0.3838383838383838

'''
If you wanted to calculate the survival rate by a single category such as "Sex", you would use a groupby():

titanic.groupby('Sex').Survived.mean()

Sex
female    0.742038
male      0.188908
Name: Survived, dtype: float64

And if you wanted to calculate the survival rate across two different categories at once, you would groupby() both of those categories:

titanic.groupby(['Sex', 'Pclass']).Survived.mean()

Sex     Pclass
female  1         0.968085
        2         0.921053
        3         0.500000
male    1         0.368852
        2         0.157407
        3         0.135447
Name: Survived, dtype: float64

This shows the survival rate for every combination of Sex and Passenger Class. It's stored as a MultiIndexed Series, meaning that it has multiple index levels to the left of the actual data.

It can be hard to read and interact with data in this format, so it's often more convenient to reshape a MultiIndexed Series into a DataFrame by using the unstack() method:

titanic.groupby(['Sex', 'Pclass']).Survived.mean().unstack()

Pclass 	1 	2 	3
Sex 			
female 	0.968085 	0.921053 	0.500000
male 	0.368852 	0.157407 	0.135447

This DataFrame contains the same exact data as the MultiIndexed Series, except that now you can interact with it using familiar DataFrame methods.
22. Create a pivot table

If you often create DataFrames like the one above, you might find it more convenient to use the pivot_table() method instead:

titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean')

Pclass 	1 	2 	3
Sex 			
female 	0.968085 	0.921053 	0.500000
male 	0.368852 	0.157407 	0.135447

With a pivot table, you directly specify the index, the columns, the values, and the aggregation function.

An added benefit of a pivot table is that you can easily add row and column totals by setting margins=True:

titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean',
                    margins=True)

Pclass 	1 	2 	3 	All
Sex 				
female 	0.968085 	0.921053 	0.500000 	0.742038
male 	0.368852 	0.157407 	0.135447 	0.188908
All 	0.629630 	0.472826 	0.242363 	0.383838

This shows the overall survival rate as well as the survival rate by Sex and Passenger Class.

Finally, you can create a cross-tabulation just by changing the aggregation function from "mean" to "count":

titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='count',
                    margins=True)

Pclass 	1 	2 	3 	All
Sex 				
female 	94 	76 	144 	314
male 	122 	108 	347 	577
All 	216 	184 	491 	891

This shows the number of records that appear in each combination of categories.
23. Convert continuous data into categorical data

Let's take a look at the Age column from the Titanic dataset:

titanic.Age.head(10)

0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
5     NaN
6    54.0
7     2.0
8    27.0
9    14.0
Name: Age, dtype: float64

It's currently continuous data, but what if you wanted to convert it into categorical data?

One solution would be to label the age ranges, such as "child", "young adult", and "adult". The best way to do this is by using the cut() function:

pd.cut(titanic.Age, bins=[0, 18, 25, 99], labels=['child', 'young adult', 'adult']).head(10)

0    young adult
1          adult
2          adult
3          adult
4          adult
5            NaN
6          adult
7          child
8          adult
9          child
Name: Age, dtype: category
Categories (3, object): [child < young adult < adult]

This assigned each value to a bin with a label. Ages 0 to 18 were assigned the label "child", ages 18 to 25 were assigned the label "young adult", and ages 25 to 99 were assigned the label "adult".

Notice that the data type is now "category", and the categories are automatically ordered.
24. Change display options

Let's take another look at the Titanic dataset:

titanic.head()

	PassengerId 	Survived 	Pclass 	Name 	Sex 	Age 	SibSp 	Parch 	Ticket 	Fare 	Cabin 	Embarked
0 	1 	0 	3 	Braund, Mr. Owen Harris 	male 	22.0 	1 	0 	A/5 21171 	7.2500 	NaN 	S
1 	2 	1 	1 	Cumings, Mrs. John Bradley (Florence Briggs Th... 	female 	38.0 	1 	0 	PC 17599 	71.2833 	C85 	C
2 	3 	1 	3 	Heikkinen, Miss. Laina 	female 	26.0 	0 	0 	STON/O2. 3101282 	7.9250 	NaN 	S
3 	4 	1 	1 	Futrelle, Mrs. Jacques Heath (Lily May Peel) 	female 	35.0 	1 	0 	113803 	53.1000 	C123 	S
4 	5 	0 	3 	Allen, Mr. William Henry 	male 	35.0 	0 	0 	373450 	8.0500 	NaN 	S

Notice that the Age column has 1 decimal place and the Fare column has 4 decimal places. What if you wanted to standardize the display to use 2 decimal places?

You can use the set_option() function:

pd.set_option('display.float_format', '{:.2f}'.format)

The first argument is the name of the option, and the second argument is a Python format string.

titanic.head()

	PassengerId 	Survived 	Pclass 	Name 	Sex 	Age 	SibSp 	Parch 	Ticket 	Fare 	Cabin 	Embarked
0 	1 	0 	3 	Braund, Mr. Owen Harris 	male 	22.00 	1 	0 	A/5 21171 	7.25 	NaN 	S
1 	2 	1 	1 	Cumings, Mrs. John Bradley (Florence Briggs Th... 	female 	38.00 	1 	0 	PC 17599 	71.28 	C85 	C
2 	3 	1 	3 	Heikkinen, Miss. Laina 	female 	26.00 	0 	0 	STON/O2. 3101282 	7.92 	NaN 	S
3 	4 	1 	1 	Futrelle, Mrs. Jacques Heath (Lily May Peel) 	female 	35.00 	1 	0 	113803 	53.10 	C123 	S
4 	5 	0 	3 	Allen, Mr. William Henry 	male 	35.00 	0 	0 	373450 	8.05 	NaN 	S

You can see that Age and Fare are now using 2 decimal places. Note that this did not change the underlying data, only the display of the data.

You can also reset any option back to its default:

pd.reset_option('display.float_format')

There are many more options you can specify is a similar way.
25. Style a DataFrame

The previous trick is useful if you want to change the display of your entire notebook. However, a more flexible and powerful approach is to define the style of a particular DataFrame.

Let's return to the stocks DataFrame:

stocks

	Date 	Close 	Volume 	Symbol
0 	2016-10-03 	31.50 	14070500 	CSCO
1 	2016-10-03 	112.52 	21701800 	AAPL
2 	2016-10-03 	57.42 	19189500 	MSFT
3 	2016-10-04 	113.00 	29736800 	AAPL
4 	2016-10-04 	57.24 	20085900 	MSFT
5 	2016-10-04 	31.35 	18460400 	CSCO
6 	2016-10-05 	57.64 	16726400 	MSFT
7 	2016-10-05 	31.59 	11808600 	CSCO
8 	2016-10-05 	113.05 	21453100 	AAPL

We can create a dictionary of format strings that specifies how each column should be formatted:

format_dict = {'Date':'{:%m/%d/%y}', 'Close':'${:.2f}', 'Volume':'{:,}'}

And then we can pass it to the DataFrame's style.format() method:

stocks.style.format(format_dict)

	Date 	Close 	Volume 	Symbol
0 	10/03/16 	$31.50 	14,070,500 	CSCO
1 	10/03/16 	$112.52 	21,701,800 	AAPL
2 	10/03/16 	$57.42 	19,189,500 	MSFT
3 	10/04/16 	$113.00 	29,736,800 	AAPL
4 	10/04/16 	$57.24 	20,085,900 	MSFT
5 	10/04/16 	$31.35 	18,460,400 	CSCO
6 	10/05/16 	$57.64 	16,726,400 	MSFT
7 	10/05/16 	$31.59 	11,808,600 	CSCO
8 	10/05/16 	$113.05 	21,453,100 	AAPL

Notice that the Date is now in month-day-year format, the closing price has a dollar sign, and the Volume has commas.

We can apply more styling by chaining additional methods:

(stocks.style.format(format_dict)
 .hide_index()
 .highlight_min('Close', color='red')
 .highlight_max('Close', color='lightgreen')
)

Date 	Close 	Volume 	Symbol
10/03/16 	$31.50 	14,070,500 	CSCO
10/03/16 	$112.52 	21,701,800 	AAPL
10/03/16 	$57.42 	19,189,500 	MSFT
10/04/16 	$113.00 	29,736,800 	AAPL
10/04/16 	$57.24 	20,085,900 	MSFT
10/04/16 	$31.35 	18,460,400 	CSCO
10/05/16 	$57.64 	16,726,400 	MSFT
10/05/16 	$31.59 	11,808,600 	CSCO
10/05/16 	$113.05 	21,453,100 	AAPL

We've now hidden the index, highlighted the minimum Close value in red, and highlighted the maximum Close value in green.

Here's another example of DataFrame styling:

(stocks.style.format(format_dict)
 .hide_index()
 .background_gradient(subset='Volume', cmap='Blues')
)

Date 	Close 	Volume 	Symbol
10/03/16 	$31.50 	14,070,500 	CSCO
10/03/16 	$112.52 	21,701,800 	AAPL
10/03/16 	$57.42 	19,189,500 	MSFT
10/04/16 	$113.00 	29,736,800 	AAPL
10/04/16 	$57.24 	20,085,900 	MSFT
10/04/16 	$31.35 	18,460,400 	CSCO
10/05/16 	$57.64 	16,726,400 	MSFT
10/05/16 	$31.59 	11,808,600 	CSCO
10/05/16 	$113.05 	21,453,100 	AAPL

The Volume column now has a background gradient to help you easily identify high and low values.

And here's one final example:

(stocks.style.format(format_dict)
 .hide_index()
 .bar('Volume', color='lightblue', align='zero')
 .set_caption('Stock Prices from October 2016')
)

Stock Prices from October 2016 Date 	Close 	Volume 	Symbol
10/03/16 	$31.50 	14,070,500 	CSCO
10/03/16 	$112.52 	21,701,800 	AAPL
10/03/16 	$57.42 	19,189,500 	MSFT
10/04/16 	$113.00 	29,736,800 	AAPL
10/04/16 	$57.24 	20,085,900 	MSFT
10/04/16 	$31.35 	18,460,400 	CSCO
10/05/16 	$57.64 	16,726,400 	MSFT
10/05/16 	$31.59 	11,808,600 	CSCO
10/05/16 	$113.05 	21,453,100 	AAPL

There's now a bar chart within the Volume column and a caption above the DataFrame.

Note that there are many more options for how you can style your DataFrame.
Bonus: Profile a DataFrame

Let's say that you've got a new dataset, and you want to quickly explore it without too much work. There's a separate package called pandas-profiling that is designed for this purpose.

First you have to install it using conda or pip. Once that's done, you import pandas_profiling:

import pandas_profiling

Then, simply run the ProfileReport() function and pass it any DataFrame. It returns an interactive HTML report:

    The first section is an overview of the dataset and a list of possible issues with the data.
    The next section gives a summary of each column. You can click "toggle details" for even more information.
    The third section shows a heatmap of the correlation between columns.
    And the fourth section shows the head of the dataset.

pandas_profiling.ProfileReport(titanic)

Overview

Dataset info
Number of variables 	12
Number of observations 	891
Total Missing (%) 	8.1%
Total size in memory 	83.6 KiB
Average record size in memory 	96.1 B

Variables types
Numeric 	6
Categorical 	4
Boolean 	1
Date 	0
Text (Unique) 	1
Rejected 	0
Unsupported 	0

Warnings

    Age has 177 / 19.9% missing values Missing
    Cabin has 687 / 77.1% missing values Missing
    Cabin has a high cardinality: 148 distinct values Warning
    Fare has 15 / 1.7% zeros Zeros
    Parch has 678 / 76.1% zeros Zeros
    SibSp has 608 / 68.2% zeros Zeros
    Ticket has a high cardinality: 681 distinct values Warning

Variables

Age
Numeric
Distinct count 	89
Unique (%) 	10.0%
Missing (%) 	19.9%
Missing (n) 	177
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	29.699
Minimum 	0.42
Maximum 	80
Zeros (%) 	0.0%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	0.42
5-th percentile 	4
Q1 	20.125
Median 	28
Q3 	38
95-th percentile 	56
Maximum 	80
Range 	79.58
Interquartile range 	17.875

Descriptive statistics
Standard deviation 	14.526
Coef of variation 	0.48912
Kurtosis 	0.17827
Mean 	29.699
MAD 	11.323
Skewness 	0.38911
Sum 	21205
Variance 	211.02
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
24.0 	30 	3.4% 	
 
22.0 	27 	3.0% 	
 
18.0 	26 	2.9% 	
 
28.0 	25 	2.8% 	
 
19.0 	25 	2.8% 	
 
30.0 	25 	2.8% 	
 
21.0 	24 	2.7% 	
 
25.0 	23 	2.6% 	
 
36.0 	22 	2.5% 	
 
29.0 	20 	2.2% 	
 
Other values (78) 	467 	52.4% 	
 
(Missing) 	177 	19.9% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
0.42 	1 	0.1% 	
 
0.67 	1 	0.1% 	
 
0.75 	2 	0.2% 	
 
0.83 	2 	0.2% 	
 
0.92 	1 	0.1% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
70.0 	2 	0.2% 	
 
70.5 	1 	0.1% 	
 
71.0 	2 	0.2% 	
 
74.0 	1 	0.1% 	
 
80.0 	1 	0.1% 	
 

Cabin
Categorical
Distinct count 	148
Unique (%) 	16.6%
Missing (%) 	77.1%
Missing (n) 	687
G6 	
 
4
C23 C25 C27 	
 
4
B96 B98 	
 
4
Other values (144) 	
192
(Missing) 	
687
Toggle details
Value 	Count 	Frequency (%) 	 
G6 	4 	0.4% 	
 
C23 C25 C27 	4 	0.4% 	
 
B96 B98 	4 	0.4% 	
 
D 	3 	0.3% 	
 
F2 	3 	0.3% 	
 
F33 	3 	0.3% 	
 
E101 	3 	0.3% 	
 
C22 C26 	3 	0.3% 	
 
C124 	2 	0.2% 	
 
D35 	2 	0.2% 	
 
Other values (137) 	173 	19.4% 	
 
(Missing) 	687 	77.1% 	
 

Embarked
Categorical
Distinct count 	4
Unique (%) 	0.4%
Missing (%) 	0.2%
Missing (n) 	2
S 	
644
C 	
168
Q 	
 
77
(Missing) 	
 
2
Toggle details
Value 	Count 	Frequency (%) 	 
S 	644 	72.3% 	
 
C 	168 	18.9% 	
 
Q 	77 	8.6% 	
 
(Missing) 	2 	0.2% 	
 

Fare
Numeric
Distinct count 	248
Unique (%) 	27.8%
Missing (%) 	0.0%
Missing (n) 	0
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	32.204
Minimum 	0
Maximum 	512.33
Zeros (%) 	1.7%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	0
5-th percentile 	7.225
Q1 	7.9104
Median 	14.454
Q3 	31
95-th percentile 	112.08
Maximum 	512.33
Range 	512.33
Interquartile range 	23.09

Descriptive statistics
Standard deviation 	49.693
Coef of variation 	1.5431
Kurtosis 	33.398
Mean 	32.204
MAD 	28.164
Skewness 	4.7873
Sum 	28694
Variance 	2469.4
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
8.05 	43 	4.8% 	
 
13.0 	42 	4.7% 	
 
7.8958 	38 	4.3% 	
 
7.75 	34 	3.8% 	
 
26.0 	31 	3.5% 	
 
10.5 	24 	2.7% 	
 
7.925 	18 	2.0% 	
 
7.775 	16 	1.8% 	
 
26.55 	15 	1.7% 	
 
0.0 	15 	1.7% 	
 
Other values (238) 	615 	69.0% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
0.0 	15 	1.7% 	
 
4.0125 	1 	0.1% 	
 
5.0 	1 	0.1% 	
 
6.2375 	1 	0.1% 	
 
6.4375 	1 	0.1% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
227.525 	4 	0.4% 	
 
247.5208 	2 	0.2% 	
 
262.375 	2 	0.2% 	
 
263.0 	4 	0.4% 	
 
512.3292 	3 	0.3% 	
 

Name
Categorical, Unique
First 3 values
Mockler, Miss. Helen Mary "Ellie"
Baclini, Miss. Eugenie
Mayne, Mlle. Berthe Antonine ("Mrs de Villiers")
Last 3 values
Hoyt, Mrs. Frederick Maxfield (Jane Anne Forby)
Gustafsson, Mr. Karl Gideon
Dowdell, Miss. Elizabeth
Toggle details

First 10 values
Value 	Count 	Frequency (%) 	 
Abbing, Mr. Anthony 	1 	0.1% 	
 
Abbott, Mr. Rossmore Edward 	1 	0.1% 	
 
Abbott, Mrs. Stanton (Rosa Hunt) 	1 	0.1% 	
 
Abelson, Mr. Samuel 	1 	0.1% 	
 
Abelson, Mrs. Samuel (Hannah Wizosky) 	1 	0.1% 	
 

Last 10 values
Value 	Count 	Frequency (%) 	 
de Mulder, Mr. Theodore 	1 	0.1% 	
 
de Pelsmaeker, Mr. Alfons 	1 	0.1% 	
 
del Carlo, Mr. Sebastiano 	1 	0.1% 	
 
van Billiard, Mr. Austin Blyler 	1 	0.1% 	
 
van Melkebeke, Mr. Philemon 	1 	0.1% 	
 

Parch
Numeric
Distinct count 	7
Unique (%) 	0.8%
Missing (%) 	0.0%
Missing (n) 	0
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	0.38159
Minimum 	0
Maximum 	6
Zeros (%) 	76.1%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	0
5-th percentile 	0
Q1 	0
Median 	0
Q3 	0
95-th percentile 	2
Maximum 	6
Range 	6
Interquartile range 	0

Descriptive statistics
Standard deviation 	0.80606
Coef of variation 	2.1123
Kurtosis 	9.7781
Mean 	0.38159
MAD 	0.58074
Skewness 	2.7491
Sum 	340
Variance 	0.64973
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
0 	678 	76.1% 	
 
1 	118 	13.2% 	
 
2 	80 	9.0% 	
 
5 	5 	0.6% 	
 
3 	5 	0.6% 	
 
4 	4 	0.4% 	
 
6 	1 	0.1% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
0 	678 	76.1% 	
 
1 	118 	13.2% 	
 
2 	80 	9.0% 	
 
3 	5 	0.6% 	
 
4 	4 	0.4% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
2 	80 	9.0% 	
 
3 	5 	0.6% 	
 
4 	4 	0.4% 	
 
5 	5 	0.6% 	
 
6 	1 	0.1% 	
 

PassengerId
Numeric
Distinct count 	891
Unique (%) 	100.0%
Missing (%) 	0.0%
Missing (n) 	0
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	446
Minimum 	1
Maximum 	891
Zeros (%) 	0.0%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	1
5-th percentile 	45.5
Q1 	223.5
Median 	446
Q3 	668.5
95-th percentile 	846.5
Maximum 	891
Range 	890
Interquartile range 	445

Descriptive statistics
Standard deviation 	257.35
Coef of variation 	0.57703
Kurtosis 	-1.2
Mean 	446
MAD 	222.75
Skewness 	0
Sum 	397386
Variance 	66231
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
891 	1 	0.1% 	
 
293 	1 	0.1% 	
 
304 	1 	0.1% 	
 
303 	1 	0.1% 	
 
302 	1 	0.1% 	
 
301 	1 	0.1% 	
 
300 	1 	0.1% 	
 
299 	1 	0.1% 	
 
298 	1 	0.1% 	
 
297 	1 	0.1% 	
 
Other values (881) 	881 	98.9% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
1 	1 	0.1% 	
 
2 	1 	0.1% 	
 
3 	1 	0.1% 	
 
4 	1 	0.1% 	
 
5 	1 	0.1% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
887 	1 	0.1% 	
 
888 	1 	0.1% 	
 
889 	1 	0.1% 	
 
890 	1 	0.1% 	
 
891 	1 	0.1% 	
 

Pclass
Numeric
Distinct count 	3
Unique (%) 	0.3%
Missing (%) 	0.0%
Missing (n) 	0
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	2.3086
Minimum 	1
Maximum 	3
Zeros (%) 	0.0%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	1
5-th percentile 	1
Q1 	2
Median 	3
Q3 	3
95-th percentile 	3
Maximum 	3
Range 	2
Interquartile range 	1

Descriptive statistics
Standard deviation 	0.83607
Coef of variation 	0.36215
Kurtosis 	-1.28
Mean 	2.3086
MAD 	0.76197
Skewness 	-0.63055
Sum 	2057
Variance 	0.69902
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
3 	491 	55.1% 	
 
1 	216 	24.2% 	
 
2 	184 	20.7% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
1 	216 	24.2% 	
 
2 	184 	20.7% 	
 
3 	491 	55.1% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
1 	216 	24.2% 	
 
2 	184 	20.7% 	
 
3 	491 	55.1% 	
 

Sex
Categorical
Distinct count 	2
Unique (%) 	0.2%
Missing (%) 	0.0%
Missing (n) 	0
male 	
577
female 	
314
Toggle details
Value 	Count 	Frequency (%) 	 
male 	577 	64.8% 	
 
female 	314 	35.2% 	
 

SibSp
Numeric
Distinct count 	7
Unique (%) 	0.8%
Missing (%) 	0.0%
Missing (n) 	0
Infinite (%) 	0.0%
Infinite (n) 	0
Mean 	0.52301
Minimum 	0
Maximum 	8
Zeros (%) 	68.2%
Toggle details

    Statistics
    Histogram
    Common Values
    Extreme Values

Quantile statistics
Minimum 	0
5-th percentile 	0
Q1 	0
Median 	0
Q3 	1
95-th percentile 	3
Maximum 	8
Range 	8
Interquartile range 	1

Descriptive statistics
Standard deviation 	1.1027
Coef of variation 	2.1085
Kurtosis 	17.88
Mean 	0.52301
MAD 	0.71378
Skewness 	3.6954
Sum 	466
Variance 	1.216
Memory size 	7.0 KiB
Value 	Count 	Frequency (%) 	 
0 	608 	68.2% 	
 
1 	209 	23.5% 	
 
2 	28 	3.1% 	
 
4 	18 	2.0% 	
 
3 	16 	1.8% 	
 
8 	7 	0.8% 	
 
5 	5 	0.6% 	
 

Minimum 5 values
Value 	Count 	Frequency (%) 	 
0 	608 	68.2% 	
 
1 	209 	23.5% 	
 
2 	28 	3.1% 	
 
3 	16 	1.8% 	
 
4 	18 	2.0% 	
 

Maximum 5 values
Value 	Count 	Frequency (%) 	 
2 	28 	3.1% 	
 
3 	16 	1.8% 	
 
4 	18 	2.0% 	
 
5 	5 	0.6% 	
 
8 	7 	0.8% 	
 

Survived
Boolean
Distinct count 	2
Unique (%) 	0.2%
Missing (%) 	0.0%
Missing (n) 	0
Mean 	0.38384
0 	
549
1 	
342
Toggle details
Value 	Count 	Frequency (%) 	 
0 	549 	61.6% 	
 
1 	342 	38.4% 	
 

Ticket
Categorical
Distinct count 	681
Unique (%) 	76.4%
Missing (%) 	0.0%
Missing (n) 	0
347082 	
 
7
1601 	
 
7
CA. 2343 	
 
7
Other values (678) 	
870
Toggle details
Value 	Count 	Frequency (%) 	 
347082 	7 	0.8% 	
 
1601 	7 	0.8% 	
 
CA. 2343 	7 	0.8% 	
 
CA 2144 	6 	0.7% 	
 
347088 	6 	0.7% 	
 
3101295 	6 	0.7% 	
 
S.O.C. 14879 	5 	0.6% 	
 
382652 	5 	0.6% 	
 
349909 	4 	0.4% 	
 
LINE 	4 	0.4% 	
 
Other values (671) 	834 	93.6% 	
 
Correlations
Sample
	PassengerId 	Survived 	Pclass 	Name 	Sex 	Age 	SibSp 	Parch 	Ticket 	Fare 	Cabin 	Embarked
0 	1 	0 	3 	Braund, Mr. Owen Harris 	male 	22.0 	1 	0 	A/5 21171 	7.2500 	NaN 	S
1 	2 	1 	1 	Cumings, Mrs. John Bradley (Florence Briggs Th... 	female 	38.0 	1 	0 	PC 17599 	71.2833 	C85 	C
2 	3 	1 	3 	Heikkinen, Miss. Laina 	female 	26.0 	0 	0 	STON/O2. 3101282 	7.9250 	NaN 	S
3 	4 	1 	1 	Futrelle, Mrs. Jacques Heath (Lily May Peel) 	female 	35.0 	1 	0 	113803 	53.1000 	C123 	S
4 	5 	0 	3 	Allen, Mr. William Henry 	male 	35.0 	0 	0 	373450 	8.0500 	NaN 	S
Want more tricks? Watch 21 more pandas tricks or Read the notebook

© 2019 Data School. All rights reserved.
'''
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
