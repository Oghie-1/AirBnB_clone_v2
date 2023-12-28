#!/usr/bin/python3
"""Starts flask web app
listening on 0.0.0.0, port 5000
routes: '/': displays "Hello HBNB!"
	'/hbnb': displays "HBNB"
	'/c/<text>': displays 'C' followed by the value of the text variable
	'/python/(text)': displays 'Python' followed by the value of the text variable
	'/number/<n>': displays 'n is a number' only if n is an interger"""


from flask import Flask, abort


app = Flask(__name__)



@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB'"""
	return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""Displays 'HBNB'"""
	return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
	"""Displays 'C' followed by the value of <text>"""
	text = text.replace("_", " ")
	return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
	"""Displays 'Python' followed by the value of text"""
	return "Python {}".format(text)




@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
	"""Displays 'n is a number' only if n is an integer"""
	return "{} is a number".format(n)



if __name__ == "__main__":
	app.run(host="0.0.0.0")
