from sklearn.feature_extraction.text import CountVectorizer

texts = ["One of the confiscated drafts was a story about stoning women to death for adultery – never published, never presented to anyone, the article stated. The narrative followed the story of a protagonist that watched a movie about stoning of women under Islamic law for adultery."]

count_vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
count_train = count_vectorizer.fit_transform(texts)
print(count_vectorizer.get_feature_names())
print(count_vectorizer.vocabulary_)
print(count_train)
