from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello and welcome to Alexandra's Docker Project"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

