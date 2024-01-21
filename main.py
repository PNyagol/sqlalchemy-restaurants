from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

engine = create_engine('sqlite:///review.db')
Session = sessionmaker(bind=engine)
session = Session()

all_restaurants = session.query(Restaurant).all()
for restaurant in all_restaurants:
    print(f"Restaurant Name: {restaurant.name}, Price: {restaurant.price}")

session.close()
