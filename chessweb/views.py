"""Endpoints of the application"""

from flask import render_template
import flask

from . import app


@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/create', methods=['POST'])
def create():
    print('requesting resource')
    return flask.Response(status=204)