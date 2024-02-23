from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 可接受跨域

@app.route('/', methods=['GET', 'POST'])
def hello():
    a = request.args
    return a


#app.run(port=3000, host='0.0.0.0', debug=True) # host 可以改 ip
app.run(port=3000, debug=True)
