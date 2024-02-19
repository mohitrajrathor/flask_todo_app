from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home(title=None):
    return render_template("base.html", title="To-Do App")



@app.route("/login")
def login(name=None):
    return render_template("base.html", name=name)

@app.route("/register", method=["POST", "GET"])
def register():
    return "<h1>Rregister Form</h1>"

@app.route("/test")
def test():
    return "<p>this is for testing purpose</p>"


if __name__ == "__main__":
    app.run(debug=True)
