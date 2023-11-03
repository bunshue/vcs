import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

print('------------------------------------------------------------')	#60個

neg_data = u'data/neg.csv'
pos_data = u'data/pos.csv'

import pandas as pd

import codecs

import jieba


corpus = []
with codecs.open(neg_data,encoding='utf-8') as f:
    for line in f:
        words = list(jieba.cut(line.replace('|','')))
        corpus.append(' '.join(words))

neg_df = pd.DataFrame()
neg_df['content'] = corpus
neg_df['label'] = 0

corpus2 = []
with codecs.open(pos_data,encoding='utf-8') as f:
    for line in f:
        words = list(jieba.cut(line.replace('|','')))
        corpus2.append(' '.join(words))

pos_df = pd.DataFrame()
pos_df['content']=corpus2
pos_df['label'] = 1   

tt = neg_df.head(5)
print(tt)

tt = pos_df.head(5)
print(tt)

corpus_df = pd.concat((neg_df,pos_df))

tt = corpus_df.head(5)
print(tt)


print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
counts = cv.fit_transform(corpus_df['content'].values)

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
targets = corpus_df['label'].values
classifier.fit(counts, targets)

examples = [u'这 本 书 真差', u"这个 电影 还 可 以"]
example_counts = cv.transform(examples)
predictions = classifier.predict(example_counts)

print(predictions)


sys.exit()

print('------------------------------------------------------------')	#60個

import pandas as pd
import numpy as np

# Create an empty dataframe
data = pd.DataFrame()

# Create our target variable
data['Gender'] = ['male','male','male','male','female','female','female','female']

# Create our feature variables
data['Height'] = [6,5.92,5.58,5.92,5,5.5,5.42,5.75]
data['Weight'] = [180,190,170,165,100,150,130,150]
data['Size'] = [12,11,12,10,6,8,7,9]
data['Team'] = ['i100','i100','i500','i100','i500','i100','i500','i100']

# View the data
print(data)

print('------------------------------------------------------------')	#60個

person = pd.DataFrame()

# Create some feature values for this single row
person['Height'] = [6]
person['Weight'] = [130]
person['Size'] = [8]
person['Gender'] = ['female']
# View the data 
print(person)


print('------------------------------------------------------------')	#60個

df1 = data.groupby(['Team','Gender']).size().rename('cnt').reset_index().set_index('Team')
df2 = pd.DataFrame(data.groupby(['Team']).size().rename('total'))

df3 = df1.merge(df2,left_index=True,right_index=True)
df3['p'] = df3['cnt'] * 1.0 /df3['total']
df3=df3.reset_index()
print(df3)


print('------------------------------------------------------------')	#60個


def p_x_given_y_1(team,gender):
     return df3['p'][df3['Team'] == team][df3['Gender']== gender].values[0]

print(p_x_given_y_1('i100','female'))
#0.4



print('------------------------------------------------------------')	#60個


#计算先验
# Number of i100
n_i100 = data['Team'][data['Team'] == 'i100'].count()

# Number of i500
n_i500 = data['Team'][data['Team'] == 'i500'].count()

# Total rows
total_ppl = data['Team'].count()



# Number of males divided by the total rows
P_i100 = n_i100*1.0/total_ppl

# Number of females divided by the total rows
P_i500 = n_i500*1.0/total_ppl

print(P_i100,P_i500)




print('------------------------------------------------------------')	#60個

# Group the data by gender and calculate the means of each feature
data_means = data.groupby('Team').mean()

# View the values
print(data_means)

print('------------------------------------------------------------')	#60個


# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby('Team').var()

# View the values
print(data_variance)



print('------------------------------------------------------------')	#60個


#计算我们需要的均值方差
# Means for i100
i100_height_mean = data_means['Height'][data_means.index == 'i100'].values[0]
i100_weight_mean = data_means['Weight'][data_means.index == 'i100'].values[0]
i100_size_mean = data_means['Size'][data_means.index == 'i100'].values[0]

# Variance for i100
i100_height_variance = data_variance['Height'][data_variance.index == 'i100'].values[0]
i100_weight_variance = data_variance['Weight'][data_variance.index == 'i100'].values[0]
i100_size_variance = data_variance['Size'][data_variance.index == 'i100'].values[0]

# Means for i500
i500_height_mean = data_means['Height'][data_means.index == 'i500'].values[0]
i500_weight_mean = data_means['Weight'][data_means.index == 'i500'].values[0]
i500_size_mean = data_means['Size'][data_means.index == 'i500'].values[0]

# Variance for i500
i500_height_variance = data_variance['Height'][data_variance.index == 'i500'].values[0]
i500_weight_variance = data_variance['Weight'][data_variance.index == 'i500'].values[0]
i500_size_variance = data_variance['Size'][data_variance.index == 'i500'].values[0]



print('------------------------------------------------------------')	#60個


#接下来，我们写个公式来计算高斯分布的概率

def p_x_given_y_2(x, mean_y, variance_y):

    # Input the arguments into a probability density function
    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))
    
    # return p
    return p

tt = person['Gender'][0]
print(tt)


print('------------------------------------------------------------')	#60個

P_i100 * p_x_given_y_1('i100',person['Gender'][0]) * \
p_x_given_y_2(person['Height'][0], i100_height_mean, i100_height_variance) * \
p_x_given_y_2(person['Weight'][0], i100_weight_mean, i100_weight_variance) * \
p_x_given_y_2(person['Size'][0], i100_size_mean, i100_size_variance)



print('------------------------------------------------------------')	#60個

# Numerator of the posterior if the unclassified observation is a female
P_i500 * p_x_given_y_1('i500',person['Gender'][0]) *\
p_x_given_y_2(person['Height'][0], i500_height_mean, i500_height_variance) * \
p_x_given_y_2(person['Weight'][0], i500_weight_mean, i500_weight_variance) * \
p_x_given_y_2(person['Size'][0], i500_size_mean, i500_size_variance)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

