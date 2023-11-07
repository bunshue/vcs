from sklearn.feature_extraction.text import CountVectorizer
import joblib

count_vectorizer = joblib.load('count_vectorizer.pkl')
classifier = joblib.load('classifier.pkl')


def classify(document):
    label = {0: 'reliable', 1: 'unreliable'}
    document_text = count_vectorizer.transform([document])
    y = classifier.predict(document_text)[0]
    return label[y]


document = input("Please enter your news description:")
print("This news review is " + classify(document) + ".")
