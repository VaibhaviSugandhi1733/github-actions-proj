"""Flask application for the dev environment."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return the environment identifier."""
    return "Dev Environment ClarityTTS by Vaibhavi123"


@app.route("/health")
def health():
    """Return the application health status."""
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
