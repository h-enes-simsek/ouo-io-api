"""
Copyright (c) 2022 Hasan Enes Şimşek
Released under MIT License
"""

import requests
from urllib.parse import urlparse

class Ouo:
    
    def __init__(self, key):
        self.key = key
        
    def short(self, url):
     
        # use ouo.io api
        result = requests.get('http://ouo.io/api/' + self.key + '?s=' + url)
        
        # control if the operation is successful
        shortened_url = urlparse(result.text)
        
        if shortened_url.scheme and shortened_url.netloc:
            return result.text
        else:
            return ''