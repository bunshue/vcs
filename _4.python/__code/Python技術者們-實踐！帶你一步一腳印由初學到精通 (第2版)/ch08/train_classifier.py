import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import joblib

train_df = pd.read_csv('Fake_news_data/train.csv')

train_df.dropna()

train_text = train_df['text'].astype(str)
train_label = train_df['label']

count_vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
count_train = count_vectorizer.fit_transform(train_text)

joblib.dump(count_vectorizer, 'count_vectorizer.pkl')

X_train, X_test, Y_train, Y_test = train_test_split(
    count_train, train_label, test_size=0.2, random_state=7)

classifier = LogisticRegression()
classifier.fit(X_train, Y_train)
pred = classifier.predict(X_test)

score = metrics.accuracy_score(Y_test, pred)
print("accuracy:%0.3f" % score)

joblib.dump(classifier, 'classifier.pkl')
