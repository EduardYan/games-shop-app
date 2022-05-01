"""
Model for a data
in the database.
"""

from helpers.db import db

class Buy(db.Model):

  # Columns
  id = db.Column(db.Integer, primary_key = True)
  game_name = db.Column(db.String(50))
  starts_price = db.Column(db.Integer)

  def __init__(self, game_name:str, starts_price:int) -> None:
    # Values
    self.game_name = game_name
    self.starts_price = starts_price