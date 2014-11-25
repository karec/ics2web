from flask import Flask, jsonify, request
from helpers.log import get_status_code
from werkzeug.exceptions import BadRequest
from icalmanage.icalparser import ical_to_dict
from requests.exceptions import MissingSchema, InvalidURL
import requests
import requests_cache

app = Flask(__name__)

URL_BASE = "https://www.google.com/calendar/ical/"

requests_cache.install_cache('/tmp/ics-api-cache', expire_after=600)


@app.route('/')
def index():
    return "Server is Running"


@app.route('/api/get/', methods=['GET'])
def get():
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


if __name__ == '__main__':
    app.run(debug=True)