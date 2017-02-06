from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def deleteRestaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    session.delete(restaurant)
    session.commit()


