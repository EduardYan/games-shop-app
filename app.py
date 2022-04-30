"""
This file have the server code.

Execute the file 'main.py' for the server.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.shop import shop_routes
from helpers.config import CONFIG


# Creating the server
app = Flask(__name__)

# Settings
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{CONFIG["DB_PATH"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
SQLAlchemy(app)

# Using routes
app.register_blueprint(shop_routes)
