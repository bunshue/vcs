from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET': 
        return 'Hello ' + request.values['username']  # http://localhost:3000/?username=oxxo

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)   