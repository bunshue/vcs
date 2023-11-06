from flask import Flask
 
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello World!"
@app.route("/callback")
def callback():
    return "Callback"
@app.route("/user/<username>")
def user(username):
    return "使用者名稱: " + str(username)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
