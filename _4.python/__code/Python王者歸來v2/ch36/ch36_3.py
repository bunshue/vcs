# ch36_3.py
from flask import Flask
app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"Hi! {name} 歡迎光臨深智數位"

if __name__ == "__main__":
    app.run()





