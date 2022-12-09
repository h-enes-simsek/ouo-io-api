

Ouo.io API 
=====================
An api for the ouo.io link shortener service that you can make money for each click on your shortened links.

Installing
==========

.. code-block:: bash

    # windows
    pip install ouo-io-api
    
    # linux
    pip3 install ouo-io-api

Usage
=====

.. code-block:: python

    from ouo.api import Ouo

    # add your api key
    ouo = Ouo("your_api_key")

    # this is blocking call
    link = ouo.short("https://hesimsek.com")

    # result is either empty string '' or shortened URL string
    if(link):
        print("ouo link: " + link)
    else:
        print("failed")
        
Notes 
=====

1. Ouo.io generates different outputs for http:// and https:// URLs.

2. Ouo.io assumes URLs with no scheme (http or https) as an http URL.