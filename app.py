from crypt import methods
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "nestototalnorandom"

@app.route("/hello")
def index():
    flash(" enter your name: ")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + " , great to have you here! ")
    return render_template("index.html")
