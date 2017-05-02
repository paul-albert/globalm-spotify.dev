# Spotify search Web API's parsing utility

import json
from flask_api import status

from config import config_instance
from .web_request import WebRequest

web_request = WebRequest()


def parse(query, search_type):
    response = web_request.get(
        str(config_instance.API_SPOTIFY_URL).format(
            query,
            search_type,
            config_instance.API_SPOTIFY_URL_LIMIT,
            config_instance.API_SPOTIFY_URL_OFFSET)
    )
    if response.status_code == status.HTTP_200_OK:
        d = json.loads(response.text)
        search_type = '{}s'.format(search_type)
        items = d[search_type]['items']
    else:
        d, items = {}, []

    if config_instance.USE_PAGINATION:
        while True:
            if d and 'next' in d[search_type]:
                if d[search_type]['next']:
                    response = web_request.get(d[search_type]['next'])
                    if response.status_code == status.HTTP_200_OK:
                        d = json.loads(response.text)
                        items += d[search_type]['items']
                    else:
                        items += []
                        break
                else:
                    break
            else:
                break

    return items
