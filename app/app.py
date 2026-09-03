from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Server is alive"})


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)