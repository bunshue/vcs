from flask import Flask, render_template, request
from wtforms import Form, StringField, validators

app = Flask(__name__)


class ReviewForm(Form):
    name = StringField('請輸入名字：', validators=[
        validators.DataRequired()])


@ app.route('/')
def index():
    form = ReviewForm()
    return render_template('index.html', form=form)


@ app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        return render_template('results.html', name=name)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
