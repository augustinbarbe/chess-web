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
    chessdocker_service = 'http://' +\
                          app.config['CONTAINER_MANAGER_HOSTNAME'] + \
                          ':' + app.config['CONTAINER_MANAGER_PORT'] +\
                          '/create'
    r = requests.post(chessdocker_service)
    return flask.Response(status=r.status_code)