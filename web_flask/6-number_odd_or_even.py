#!/usr/bin/python3
"""Starts Flask WEB APP
routes: '/': display 'Hello HBNB!'
	'/hbnb': displays 'HBNB'
	'/c/<text>': display 'C' followed by the text variable
	'/python/(<text>)': display 'python', followed by the text variable
	'/number/<n>': display 'n is a number' only if 'n' is an interger
	'/number_template/<n>': displays a html page only if n is an interger
	'/number_odd_or_even/<n>': display html page only if n is an integer
"""


from flask import Flask


app = Flask(__name__)



app.route('/', strict_slashes=False)
def hello_hbnb():
	"""displays 'Hello HBNB!' """
	return "Hello HBNB!"



app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""displays 'HBNB' """
	return "HBNB"


app.route('/c/<text>', strict_slashes=False)
def c(text):
	"""Displays 'C' followed by the text variable"""
	text = text.replace("_", " ")
	return "C {}".format(text)



app.route('/python/', strict_slashes=False)
def python(text="is cool"):
	"""Displays"
