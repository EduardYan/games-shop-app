"""
This file have the server code.

Execute the file 'main.py' for the server.
"""

from flask import Flask
from routes.shop import shop_routes


# creating the server
app = Flask(__name__)


# using routes
app.register_blueprint(shop_routes)
