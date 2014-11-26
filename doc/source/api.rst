api package
===========
API Routes where you define each route and their functions.

We also use a Cache file who are invalidate every 10minutes. Feel free to modificate it at your ease.
You can find it in the begginning of the api.py file.

.. code-block:: python

    requests_cache.install_cache('/tmp/ics-api-cache', expire_after=600)

1. Argument: Location of the cache directory.
2. Argument: Time before expiration in seconds.

API Routes
----------
.. code-block:: python

    @app.route('/')

Return "Server Running"

.. code-block:: python

    @app.route('/api/get/doc/')

Redirect to the `Doc ics2web <http://ics2web.readthedocs.org/en/latest/#indices-and-tables/>`_.

.. code-block:: python

    @app.route('/api/get/', methods=['GET'])
    def get():
        get_return_request = request.args.get('url', "")

Take the link provided in the URL like: "/api/get?url= <URL>"
This function handle multiple error like "*Bad URL Provided*", "*Bad ICS File*", "*HTTP Exception*".
If everything went well, it return a json dictionnary.
Else and exception is raise.

Add Routes to api
-----------------
To add a route in the api go to api.py and add something like:

.. code-block:: python

    @app.route('/api/get/doc/')


Which will do something when you are in the "/api/get/doc/". To be able to do some action define a function under that:

.. code-block:: python

    def doc():


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

