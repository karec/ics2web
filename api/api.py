from flask import Flask, jsonify, request, redirect
from helpers.log import get_status_code
from werkzeug.exceptions import BadRequest
from icalmanage.icalparser import ical_to_dict
from requests.exceptions import MissingSchema, InvalidURL
from flask_cors import CORS
from helpers.room_list import room_dict as dico
import requests
import requests_cache


app = Flask(__name__)
cors = CORS(app, ressources={r"/api/*": {"origins": "*"}})

requests_cache.install_cache('/tmp/ics-api-cache', expire_after=600)

@app.route('/')
def index():
    """
    Simple message to make sure the server is running

    :return: Simple string message
    """

    return "Server is Running"

@app.route('/api/doc/')
def doc():
    """
    Redirect to the ics2web Documentation

    :return: None
    """
    return redirect('http://ics2web.readthedocs.org/en/latest/#indices-and-tables')


@app.route('/api/get/', methods=['GET'])
def get():
    """
    Simple method who take a ICS URL and and return a JSON Dictionnary. Also handle some error.

    :return: Json Dictionnary
    """
    get_return_request = request.args.get('url', "")
    try:
        r = requests.get(get_return_request, stream=True)
    except MissingSchema:
        raise BadRequest("Bad URL Provided")
    except InvalidURL:
        raise BadRequest("Bad URL Provided")
    if get_status_code(r):
        event = ical_to_dict(r)
        if not event:
            raise BadRequest("Bad ICS Provided")
        return jsonify(event)
    else:
        raise BadRequest("HTTP Exception")


@app.route('/api/get/<room>', methods=['GET'])
def read_conf(room=None):
    room_dict = dico
    selected_room = dico.get(room, None)
    if room:
        try:
            r = requests.get(selected_room, stream=True)
        except MissingSchema:
            raise BadRequest("Bad URL Provided")
        except InvalidURL:
            raise BadRequest("Bad URL Provided")
        if get_status_code(r):
            event = ical_to_dict(r)
        if not event:
            raise BadRequest("Bad ICS Provided")
        return jsonify(event)
    else:
        raise BadRequest("No Room Found, check your room id")


if __name__ == '__main__':
    app.run(debug=True)