# Controllers

from flask import Blueprint

from utils.encode import quote
from utils.session import Session
from utils.parse import parse


controllers = Blueprint('controllers', __name__)
session = Session()
query_quote = quote
spotify_parse = parse

from .search import *
