# Title: Flask Lab Part 1
# Name: Shane Skare
# Abstract: Initial test using Flask.
#  Much of the lab was a refresher from internet programming class.
#  Only struggle was getting the image to appear. Worked once I used
#  the static file.
# Date: 07/06/2024

# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return '<p> Shane S. : jjdidtiebuckle <br> Smith J. : fomo <br> Hector P. : asap </p>' 

@app.route('/shane')
def acronym():
    return '<p> jjdidtiebuckle </P>'

@app.route('/template')
def template():
    return render_template('template.html')