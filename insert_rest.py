from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurant1 = Restaurant(name = "Picnix")
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name = "Cow boy")
session.add(restaurant1)
session.commit()

restaurant3 = Restaurant(name = "Kasba")
session.add(restaurant1)
session.commit()

restaurant4 = Restaurant(name = "bake and shake")
session.add(restaurant1)
session.commit()

restaurant5 = Restaurant(name = "China Town")
session.add(restaurant1)
session.commit()