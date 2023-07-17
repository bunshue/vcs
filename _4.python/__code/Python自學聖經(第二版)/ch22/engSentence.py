from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
data = cv.fit_transform(['code is is easy, i like python', 'code is too hard, i dislike python'])
print('one-hot編碼：')
print(data.toarray())
print('特徵名稱：')
print(cv.get_feature_names())
