"""Endpoints of the application"""

from flask import render_template
import flask
import requests

from . import app


@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/create', methods=['POST'])
def create():
    r = requests.post(app.config['CONTAINER_MANAGER_URL'])
    print(r.content)
    return flask.Response(status=r.status_code)