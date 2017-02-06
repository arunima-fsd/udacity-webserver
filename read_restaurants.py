from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def getRestaurants():
    """Query to get all the restaurants ordered by their name"""

    restaurants = session.query(Restaurant).order_by(Restaurant.name)
    return restaurants