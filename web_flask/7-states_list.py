#!/usr/bin/python3
"""Starts a flask web app
listening on 0.0.0.0, port 5000
Routes:
/states_list: HTML page with a list of all State objects in DBStorage

"""

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
	"""Displays an HTML page with a list of all State obj in DBStorage.
	states are sorted by name"""
	states = storage.all("State")
	return render_template("7-states_list.html", states=states)



@app.teardown_appcontext
def teardown(exc):
	"""Remove the current SQLALchemy seessiom"
	
