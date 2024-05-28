#!/usr/bin/python3
'''
creating Flask app: and register the blueprint
'''
from flask import jsonify #type:ignore
from api.v2.views import app_views #type:ignore

@app_views.route('/status') # type: ignore
def api_status(): # type: ignore
    '''
    
    '''
    response = {'status': "OK"}
    return jsonify(response) # type: ignore