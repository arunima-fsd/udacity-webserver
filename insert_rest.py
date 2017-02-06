from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def insertRestaurant(name):
    """Query to insert new restaurant"""
    restaurant = Restaurant(name= name)
    session.add(restaurant)
    session.commit()
