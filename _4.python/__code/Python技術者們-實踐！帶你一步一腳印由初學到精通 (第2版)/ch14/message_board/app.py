from flask import Flask, render_template, request, url_for, redirect
import app_module as m

app = Flask(__name__)


@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = m.ReviewForm()
        says = m.sqlite_read()
        return render_template('index.html', says=says, form=form)
    else:
        form = m.ReviewForm(request.form)
        if request.method == 'POST' and form.validate():
            title = request.form['title']
            username = request.form['username']
            email = request.form['email']
            message_text = request.form['message_text']
            m.sqlite_insert(title, username, email, message_text)
            return redirect(url_for('index'))
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
