from sklearn.feature_extraction.text import CountVectorizer

texts = ["dog and fish, dog and dog", "dog and dog", "dog and cat"]
count_vectorizer = CountVectorizer(ngram_range=(1, 1), stop_words='english')
count_train = count_vectorizer.fit_transform(texts)
print(count_vectorizer.get_feature_names())
print(count_vectorizer.vocabulary_)
print(count_train)
