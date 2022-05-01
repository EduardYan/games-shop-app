"""
Routes for the server, used in 'app.py' file.
"""


from flask import (
	Blueprint,
	render_template,
	redirect,
	url_for,
	request,
	flash,
)
from models.buys import Buy
from helpers.db import db


# routes
shop_routes = Blueprint('shop', __name__)


@shop_routes.route('/')
def home():
	"""
	Principal route.
	render the index.html
	"""

	return render_template('index.html', page = 'Main')


@shop_routes.route('/buy', methods = ['POST'])
def buy_game():
	"""
	Route for manage the buy
	of a game.
	"""

	# getting to show
	game_name = request.form['game-name']
	starts_price = int(request.form['starts-price'])

	buy = Buy(game_name, starts_price)

	try:
		db.session.add(buy)
		db.session.commit()

		# Sending a message
		flash(f'You bought to {buy.game_name}')

		return redirect(url_for('shop.home'))

	except:
		print('\nSome error for save in the database\n')
		return redirect(url_for('shop.home'))


@shop_routes.route('/about')
def about():
	"""
	Route for render the about page.
	"""

	return render_template('about.html', page = 'About')
