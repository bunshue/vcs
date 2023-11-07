from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from sklearn.feature_extraction.text import CountVectorizer
import os
import joblib

cur_dir = os.path.dirname(__file__)
count_vectorizer = joblib.load(open(os.path.join(cur_dir,
                                                 'count_vectorizer.pkl'), 'rb'))

classifier = joblib.load(open(os.path.join(cur_dir,
                                           'classifier.pkl'), 'rb'))


def classify(document):
    label = {0: 'reliable', 1: 'unreliable'}
    document_text = count_vectorizer.transform([document])
    y = classifier.predict(document_text)[0]
    proba = classifier.predict_proba(document_text).max()
    return label[y], proba


app = Flask(__name__)


class ReviewForm(Form):
    review = TextAreaField(
        '', [validators.DataRequired(), validators.length(min=15)])


@ app.route('/')
def index():
    form = ReviewForm()
    return render_template('reviewform.html', form=form)


@ app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['review']
        label, proba = classify(review)
        return render_template('results.html',
                               content=review,
                               prediction=label,
                               probability=round(proba*100, 2))
    return render_template('reviewform.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
