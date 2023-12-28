#!/usr/bin/python3
"""Start Flask webapp
app must be listening on 0.0.0.0 port 5000

routes: /: display “Hello HBNB!”
	/hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""Displays 'HBNB'"""
	return "HBNB"



if __name__ == "__main__"
	app.run(host="0.0.0.0")
