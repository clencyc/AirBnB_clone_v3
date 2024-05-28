#!/usr/bin/python3
'''
creating Flask app: and register the blueprint
'''
from flask import jsonify #type:ignore
from api.v1.views import app_views #type:ignore
@app_views.route('/status', methods=['GET'] ) # type: ignore
def api_status(): # type: ignore
    return jsonify({"status": "OK"}) # type: ignore