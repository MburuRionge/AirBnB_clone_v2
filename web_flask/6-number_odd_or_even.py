#!/usr/bin/python3
""" A script that starts flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ function to return Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def text_var(text):
    """displays a text variable"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text="is cool"):
    """
    displays the txt variable with defaault "is cool"
    """
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """displays an int variable"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """ display a html page """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """displays html page"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port:'5000'
