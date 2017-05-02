# Web requests utility

import requests


class WebRequest(object):

    def get(self, url):
        try:
            return requests.get(url)
        except:
            return None
