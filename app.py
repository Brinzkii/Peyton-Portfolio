from flask import Flask, render_template, flash, redirect, session
import os

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = "password"

#################### App Setup ####################

@app.context_processor
def inject_frames():
    """Make frames for art available"""

    frames = []
    directory = os.path.join(app.static_folder, "artwork/frames")
    
    for filename in os.listdir(directory):
        f = f'/static/artwork/frames/{filename}'
        frames.append(f)

    return dict(frames = frames)

@app.context_processor
def inject_graphic_design():
    """Make graphic design pieces available"""

    graphic_design = []
    directory = os.path.join(app.static_folder, "artwork/graphic-design")
    
    for filename in os.listdir(directory):
        f = f'/static/artwork/graphic-design/{filename}'
        graphic_design.append(f)

    return dict(graphic_design = graphic_design)

@app.context_processor
def inject_illustration():
    """Make illustration pieces available"""

    illustration = []
    directory = os.path.join(app.static_folder, "artwork/illustration")
    
    for filename in os.listdir(directory):
        f = f'/static/artwork/illustration/{filename}'
        illustration.append(f)

    return dict(illustration = illustration)

@app.context_processor
def inject_print_making():
    """Make print making pieces available"""

    printmaking = []
    directory = os.path.join(app.static_folder, "artwork/printmaking")
    
    for filename in os.listdir(directory):
        f = f'/static/artwork/printmaking/{filename}'
        printmaking.append(f)

    return dict(printmaking = printmaking)

@app.context_processor
def inject_random():
    """Make random pieces available"""

    random = []
    directory = os.path.join(app.static_folder, "artwork/random")
    
    for filename in os.listdir(directory):
        f = f'/static/artwork/random/{filename}'
        random.append(f)

    return dict(random = random)

#################### Routes ####################

@app.route("/")
def show_home():
    """Show homepage"""

    return render_template("home.html")

@app.route("/graphic-design")
def show_designs():
    """Show designs"""

    return render_template("graphic-design.html")

@app.route("/printmaking")
def show_print_making():
    """Show print making"""

    return render_template("printmaking.html")

@app.route("/illustration")
def show_illustrations():
    """Show illustrations"""

    return render_template("illustration.html")

@app.route("/random")
def show_random():
    """Show random pieces"""

    return render_template("random.html")