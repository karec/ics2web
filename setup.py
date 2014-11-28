#! /usr/bin/env python
descr = "Light api for ics parsing"
from distutils.core import setup
setup(
    name='ics2web',
    version='0.1',
    maintainer='valett_e pigot_a bene_t',
    packages=['api', 'api.icalmanage', 'api.helpers'],
    description=descr, requires=[
        'flask',
        'werkzeug', 'requests', 'pytz', 'icalendar'
    ]
)