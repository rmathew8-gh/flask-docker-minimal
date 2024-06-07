#!/usr/bin/python
# coding: utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def entry_point():
    return "Hello World!"


@app.route("/", methods=["GET"])
def index():
    return jsonify({"msg": "Server is alive"}), 200


@app.route("/oauth/token", methods=["POST"])
def login():
    data = request.get_json()

    # Validate the request parameters
    if (
        data.get("grant_type") != "password"
        or data.get("client_id") != "your_client_id"
        or data.get("client_secret") != "your_client_secret"
    ):
        return jsonify({"error": "Invalid request parameters"}), 400

    # Validate the username and password
    if data.get("username") != "test_user" or data.get("password") != "test_password":
        return jsonify({"error": "Invalid credentials"}), 401

    # Return a mock access token
    return (
        jsonify(
            {
                "access_token": "mock_access_token",
                "token_type": "Bearer",
                "expires_in": 86400,
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
