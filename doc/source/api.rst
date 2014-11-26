api package
===========
API Routes where you define each route and their functions.

We also use a Cache file who are invalidate every 10minutes. Feel free to modificate it at your ease.
You can find it in the begginning of the api.py file.

.. code-block:: python

    requests_cache.install_cache('/tmp/ics-api-cache', expire_after=600)

1. Argument: Location of the cache directory.
2. Argument: Time before expiration in seconds.

See requests-cache_ doc for more information.

.. _requests-cache: http://requests-cache.readthedocs.org/en/latest/

API Routes
----------
.. code-block:: python

    @app.route('/')

Return "Server Running"

.. code-block:: python

    @app.route('/api/get/doc/')

Redirect to `Doc ics2web <http://ics2web.readthedocs.org/en/latest/#indices-and-tables/>`_.

.. code-block:: python

    @app.route('/api/get/', methods=['GET'])
    def get():
        get_return_request = request.args.get('url', "")

Take the link provided in the URL like: "/api/get?url= <URL>"
This function handle multiple error like "*Bad URL Provided*", "*Bad ICS File*", "*HTTP Exception*".
It will also return a 400 : Bad request error

If everything went well, it return a json dictionnary.
Else an exception is raised.

Example of json returned by the api :

.. code-block:: python

    {
      "current_events": [
        {
          "end": "2014-11-26T19:00:00",
          "name": "Test1",
          "personnes": [
            "pigot_a",
            "valett_e",
            "bene_t"
          ],
          "place": "",
          "start": "2014-11-26T16:00:00"
        },
        {
          "end": "2014-11-26T19:30:00",
          "name": "Test3",
          "personnes": [
            "pigot_a",
            "valett_e",
            "bene_t"
          ],
          "place": "",
          "start": "2014-11-26T15:30:00"
        }
      ],
      "next_events": [
        {
          "end": "2014-11-26T23:30:00",
          "name": "Test0",
          "place": "",
          "start": "2014-11-26T19:30:00"
        }
      ]
    }

Add Routes to api
-----------------
Since the api run Flask_, to add a route in the api go to api.py and add your function like this:

.. _Flask: http://flask.pocoo.org/

.. code-block:: python

    @app.route('/api/get/doc/')
    def doc():
        # logic here
        pass

Which will do something when you are in the "/api/get/doc/". To be able to do some action define a function like this:

.. code-block:: python

    def doc():


And add your route decorator :

.. code-block:: python

    @app.route('/api/get/doc/')



Under that, put your logic in it. For exemple:

.. code-block:: python

    return redirect('http://ics2web.readthedocs.org/en/latest/#indices-and-tables')


Here's the complete code:

.. code-block:: python

    @app.route('/api/get/doc/')
    def doc():
        return redirect('http://ics2web.readthedocs.org/en/latest/#indices-and-tables')

**Explanation :**
    Here you declare a route to "/api/get/doc".
    You make a function named doc() who will redirect you to `Doc ics2web <http://ics2web.readthedocs.org/en/latest/#indices-and-tables/>`_.


api module
----------

.. automodule:: api.api
    :members:
    :undoc-members:

Subpackages
-----------

.. toctree::

    api.helpers
    api.icalmanage

