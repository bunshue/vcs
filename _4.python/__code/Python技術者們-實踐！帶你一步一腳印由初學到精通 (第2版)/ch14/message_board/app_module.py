from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import EmailField
import sqlite3


def sqlite_insert(title, username, email, message_text):
    connect = sqlite3.connect('database.sqlite')
    connect.execute("INSERT INTO message_board (title, username, email, message_text, date) VALUES (?, ?, ?, ?, DATETIME('now'))",
                    (title, username, email, message_text))
    connect.commit()
    connect.close()


def sqlite_read():
    conn = sqlite3.connect('database.sqlite')
    creat_sql = 'create table if not exists message_board ("title" TEXT, "username" TEXT, "email" TEXT, "message_text" TEXT, "date" TEXT)'
    conn.execute(creat_sql)
    read_sql = 'select * from message_board'
    read_data = conn.execute(read_sql)
    dataset = read_data.fetchall()
    conn.close()
    return list(dataset)


class ReviewForm(Form):
    title = StringField(
        '標題：', validators=[validators.DataRequired(message='Not Null')])
    username = StringField('作者：', validators=[
                           validators.DataRequired(message='Not Null')])
    email = EmailField('email：', validators=[
                       validators.DataRequired(message='Not Null')])
    message_text = TextAreaField(
        '留言：', [validators.DataRequired(message='Not Null')])
