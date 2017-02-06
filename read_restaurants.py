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

    restaurants = session.query(Restaurant).all()
    return restaurants


def getRestaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    return restaurant

def modifyRestaurant(id, name):
    restaurant = getRestaurant(id)
    restaurant.name = name
    print restaurant.id
    print restaurant.name
    session.add(restaurant)
    session.commit()