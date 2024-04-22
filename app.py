from flask import Flask, render_template, flash, redirect, session
import os

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = "password"


#################### Routes ####################

@app.route("/")
def show_home():
    """Show homepage"""

    return render_template("home.html")

@app.route("/design")
def show_designs():
    """Show designs"""

    return render_template("designs.html")

@app.route("/print_making")
def show_print_making():
    """Show print making"""

    return render_template("print-making.html")

@app.route("/illustrations")
def show_illustrations():
    """Show illustrations"""

    return render_template("illustrations.html")