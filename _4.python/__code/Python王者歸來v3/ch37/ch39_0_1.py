# ch39_0_1.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "歡迎來到深智數位"

if __name__ == "__main__":
    app.run()





