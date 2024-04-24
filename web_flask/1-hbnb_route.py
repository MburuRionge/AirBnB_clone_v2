#!/usr/bin/python3
""" a script that starts a flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ function returns Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function to return HBNB """
    return "HBNB"


if __name__ == '__main__':
    appp.run(host='0.0.0.0', port=5000)
