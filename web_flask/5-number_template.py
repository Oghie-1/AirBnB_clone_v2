#!/usr/bin/python3
"""Starts Flask web app
listening on 0.0.0.0, port 5000
routes: /: display 'hELLO hbnb!'
	'/hbnb': display 'HBNB'
	'/C/<TEXT>': displays 'C', followed by the value of the text variable
	'/python/(<text>)': display "Python", followed by the value of the text variable
	'/number/<n>': display 'n is a number' only if n is an integer
	'/number_template/<n>': displays a html page only if n is an integer:
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""displays 'Hello HBNB!'"""
	return "Hello HBNB!"



@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""displays 'HBNB'"""
	return "HBNB"



@app.route('/c/<text>', strict_slashes=False)
def c(text):
	"""displays 'C' followed by the value of the text variable"""
	text = text.replace("_", " ")
	return "C {}".format(text)



@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
	"""displays 'python' followed by the value of the text variable"""
	text = text.replace("_", " ")
	return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
	"""Displays 'n is a number' only if 'n' is an interger"""
	return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
	"""displays HTML page only if 'n' is an interger"""
	return render_template("5-number.html", n=n)


if __name__ == "main":
	app.run(host="0.0.0.0")
