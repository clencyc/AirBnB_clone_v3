#!/usr/bin/python3
'''
creating Flask app: and register the blueprint
'''
from flask import Flask #type:ignore
from models import storage #type:ignore
from api.v1.views import app_views #type:ignore

app = Flask(__name__) #type:ignore
app.register_blueprint(app_views) #type:ignore

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')  #type:ignore
    PORT = int(getenv('HBNB_API_PORT', 5000))  #type:ignore
    app.run(hosts=HOST, port=PORT, threaded=True)  #type:ignore