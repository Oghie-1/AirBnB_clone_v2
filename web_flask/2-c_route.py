#!/usr/bin/python3
"""starts flask web app
must be lisstening on 0.0.0.0 port 5000

routes: /: display “Hello HBNB!”
	/hbnb: display “HBNB”
	/c/<text>
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=Flase)
def hello_hbnb():
	"""Returns 'Hello HBNB!'"""
	return "Hello HBNB!"


def hbnb():
	"""Returns 'HBNB' """
	return "HBNB"

def c_text(text):
	"""Retruns 'C' followed by the value of <text>"""
	text = text.replace("_"," ")
	return "C {}".format(text)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
