"""
TFM DevSecOps - Demo application
Minimal application to demonstrate the complete CI/CD cycle: build, vulnerability scanning, push, and deployment.
"""
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "1.0.0")


@app.route("/")
def root():
    return jsonify({
        "service": "tfm-demo-app",
        "version": VERSION,
        "hostname": socket.gethostname(),
        "status": "ok"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
