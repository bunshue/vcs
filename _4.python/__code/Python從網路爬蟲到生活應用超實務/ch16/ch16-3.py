from flask import Flask, jsonify
 
app = Flask(__name__)
@app.route("/")
def main():
    return jsonify({"name": "Joe Chen",
                    "email": "hueyan@ms2.hinet.net"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
