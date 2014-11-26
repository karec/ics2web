IcalManage package
==================

Using the parser
----------------

The parser is based on the great lib icalendar_. for parsing the ICS file, but it only use the parsing part for loading
an existing valid ics file.

The function is prototyped like this :

.. code-block:: python

    def ical_to_dict(stream)

The `stream` parameter is stream of an ical file, you can set it with a request stream, like this :

.. code-block:: python

    r = requests.get(ical_url, stream=True)
    data = ical_to_dict(r)

Or you can simply read an local ical file

If the file content cannot be read or parsed by icalendar, the function will log an error and return `False`

The `ical_to_dict` function will return  a `dict` like this :

.. code-block:: python

    {
        'current_events': list_of_events,
        'next_events': list_of_mini_events
    }

The `current_events` contain a list containing dict with full informations about events in progress.
The event in progress dict look like this :


And the `list_of_mini_events` is a list containing basics information about incoming events like this :

.. code-block:: python

    {
        "end": "2014-11-26T17:30:00",
        "name": "ert",
        "place": "Salle 301",
        "start": "2014-11-26T16:30:00"
    }

In the actual version of the api, the parser is directly expose in JSON and returned by the `get` api function
But you can use it in other place by importing it

.. code-block:: python

    from icalmanage.icalparser import ical_to_dict
.. _icalendar: https://pypi.python.org/pypi/icalendar

The parser as been tested on google agenda ical file. But because of a bug when retrieving dates from the ical file, the
api.icalmanage.helpers file contain a simple function for managing utc offset :

.. code-block:: python

    def set_utc(dt):
        utc_of = timezone('Europe/Paris')
        now = datetime.now()
        return dt + utc_of.utcoffset(now)


This function allow you to manually add the utc offset to the returned datetime object. Unfortunately the module don't
has any configuration file (yet), so the timezone is hardcoded (sadly), but configuration is coming soon !

This function is call by default by the `ical_to_dict` function, which is the main function of the parser.

api.icalmanage.helpers module
-----------------------------

.. automodule:: api.icalmanage.helpers
    :members:
    :undoc-members:

api.icalmanage.icalparser module
--------------------------------

.. automodule:: api.icalmanage.icalparser
    :members:
    :undoc-members:
