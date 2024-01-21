from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///review.db')
Session = sessionmaker(bind=engine)
session = Session()


restaurant1 = Restaurant(name='Tasty Grill', price=2)
restaurant2 = Restaurant(name='Fancy Bistro', price=4)

customer1 = Customer(first_name='Peter', last_name='Nyagol')
customer2 = Customer(first_name='Edwina', last_name='Bikeri')

review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)


session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()


session.close()
