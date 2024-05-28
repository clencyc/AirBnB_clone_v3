#!/usr/bin/python3
'''
creating Flask app: and register the blueprint
'''

from flask import Flask #type:ignore
from flask import Blueprint #type:ignore
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1') #type:ignore
from api.v1.views.index import *

