"""A tiny Flask web app used as the example to containerize in this lab."""
import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        message="Hello from Docker!",
        environment=os.environ.get("APP_ENV", "dev"),
        database_url=os.environ.get("DATABASE_URL", "not set"),
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # Dev server. In production we run this with gunicorn (see the multi-stage exercise).
    app.run(host="0.0.0.0", port=5000)
