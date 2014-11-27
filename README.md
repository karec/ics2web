ics2web
=======

[![doc](https://readthedocs.org/projects/ics2web/badge/?version=latest)](http://ics2web.readthedocs.org/en/latest/index.html)

a small api for working with ical file

Presentation
------------

The goal of this project is simple : a light api for returning JSON object of currents events, next events, etc... from an ical file. The purpose of the project was to be able to simply get informations about specific calendars to display it with differents devices.

The client folder contain an actual client in html / javascript for testing the API

External tools
--------------

Full requirements are avaible in requirements.txt file.
For this project we use :

* [Flask](http://flask.pocoo.org/) for the api with [Flask-Cors](https://pypi.python.org/pypi/Flask-Cors)
* [icalendar](https://pypi.python.org/pypi/icalendar) for parsing ical files
* [requests](http://docs.python-requests.org/en/latest/) for gettings icals from url
* [requests-cache](https://pypi.python.org/pypi/requests-cache) for simple caching http requests

TODO
----

* Adding routes for more options in API
* Add unit testing for the api
* Deployement script for others backends like apache
* More support for more ical providers
* Create more generic parser
* Refactore code
