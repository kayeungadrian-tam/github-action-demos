from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>Hello, World! Testing</p>"
