from flask import Flask
from flask import request
from data import CLASS

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users/<name>", methods=["GET", "POST", "DELETE"])
def user(name: str):

    if request.method == "GET":
        return f"<p>Get! Name: {name}</p>"


@app.route("/docs", methods=["GET", "POST"])
def get_params():
    email = request.form.get("email")
    password = request.form.get("password")

    print(email)
    print(password)

    args = request.args
    name = args.get("name", default="", type=str)
    args.get("price", default=0, type=int)
    print(name)
    return "<p>Docs!</p>"
