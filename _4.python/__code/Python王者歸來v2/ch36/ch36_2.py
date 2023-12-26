# ch36_2.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/hello")
def hello():
    return "歡迎來到深智數位"

if __name__ == "__main__":
    app.run()





