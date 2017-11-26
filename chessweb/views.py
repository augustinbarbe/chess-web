"""Endpoints of the application"""

from flask import render_template
import flask
import requests

from . import app

def event_stream(gameid):
    pubsub = red.pubsub()
    pubsub.subscribe(gameid)
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        yield message['data']



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
    r.content
    return flask.Response(status=r.status_code)

@app.route('/update/<gameid>', methods=['GET'])
def stream(gameid):
    return flask.Response(event_stream(gameid))