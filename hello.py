from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>My app</h1>"


@app.route("/run")
def show():
    return "<p>lorem span</p>"


@app.route("/login")
def login(name=None):
    return render_template("base.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
