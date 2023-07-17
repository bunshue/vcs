from flask import Flask
from flask import request
app = Flask(__name__)

from flask import render_template
@app.route('/get1', methods=['GET'])
def get1():
    name = request.args.get('name')
    city = request.args.get('city')
    return render_template('get1.html', **locals())

if __name__ == '__main__':
    app.run()
