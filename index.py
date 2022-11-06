from flask import Flask
from data import CLASS

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/users")
def get_users(name: str):
    return f"<p>Hello, {name}!</p>"
