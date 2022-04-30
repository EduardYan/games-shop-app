#!/usr/bin/env python3

"""
Principal file to execute for
execute the server.
"""


from app import app
from helpers.db import db
from helpers.config import CONFIG


if __name__ == '__main__':

 # Creating tables
	with app.app_context():
		db.create_all()

	# Running the server
	app.run(
		port = CONFIG['PORT'],
		host = '0.0.0.0',
		debug = CONFIG['DEBUG']
	)
