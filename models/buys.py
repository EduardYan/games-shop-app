"""
Model for a data
in the database.
"""

from helpers.db import db

class Buy(db.Model):

  # Columns
  id = db.Column(db.Integer, primary_key = True)
  game_name = db.Column(db.String(50))

  def __init__(self, game_name:str) -> None:
    # Values
    self.game_name = game_name