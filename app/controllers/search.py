# Search controller

from flask import jsonify, make_response, render_template, request
from flask_api import status

from . import controllers, query_quote, session, spotify_parse
from config import config_instance


default_filter = config_instance.TYPES[0]


@controllers.route('/', methods=['GET'])
def index():
    session.set('filter', session.get('filter') or default_filter, default_filter)
    return render_template('index.html',
                           title=config_instance.APP_TITLE,
                           types=config_instance.TYPES,
                           filter=session.get('filter'))


@controllers.route('/set-filter', methods=['POST'])
def set_filter():
    filter_value = request.form['filter']
    session.set('filter', filter_value, default_filter)
    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'filter': filter_value,
    }), response_status)


@controllers.route('/search', methods=['POST'])
def search():
    query = query_quote(request.form['query'])
    search_type = session.get('filter') or default_filter

    items = spotify_parse(query, search_type)

    response_status = status.HTTP_200_OK
    return make_response(jsonify({
        'type':     search_type,
        'query':    query,
        'items':    items,
        'counter':  len(items),
    }), response_status)
