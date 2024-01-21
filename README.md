# SQLAlchemy Restaurants

This project demonstrates the use of SQLAlchemy for modeling a restaurant review domain. It includes three models: `Restaurant`, `Customer`, and `Review`. The relationships between these models are established to represent a typical scenario where a restaurant can have multiple reviews, a customer can leave multiple reviews, and a review belongs to both a restaurant and a customer.

## Project Structure
|-- sqlalchemy-restaurants/
| |-- alembic/
| | |-- versions/
| | | |-- [timestamp]_create_tables.py
| | |-- alembic.ini
| | |-- env.py
| |-- models/
| | |-- init.py
| | |-- base.py
| | |-- restaurant.py
| | |-- customer.py
| | |-- review.py
| |-- main.py
| |-- config.py
| |-- seed.py

- `alembic/`: Directory containing Alembic migration files.
- `models/`: Directory containing the SQLAlchemy models.
- `main.py`: Main module for application setup.
- `config.py`: Configuration file for the application.
- `seed.py`: Script to seed the database with sample data.

## Getting Started

1. Install dependencies: pip install -r requirements.txt

2. Initialize the database: python seed.py

3. Explore the models and relationships in the Python REPL: 
    python
    from models import Restaurant, Customer, Review
    from sqlalchemy import create_engine, inspect

    engine = create_engine('sqlite:///review.db')
    inspector = inspect(engine)

    print(inspector.get_table_names())

## Usage

Explore the provided methods in the models:

    Review.customer()
    Review.restaurant()
    Restaurant.reviews()
    Restaurant.customers()
    Customer.reviews()
    Customer.restaurants()
    Customer.full_name()
    Customer.favorite_restaurant()
    Customer.add_review(restaurant, rating)
    Customer.delete_reviews(restaurant)
    Review.full_review()
    Restaurant.fanciest()
    Restaurant.all_reviews()

Remember to run: python seed.py after any changes to update the database.

## Notes (continued)

- The project uses SQLite as the database.
- To create migration scripts for future changes, use Alembic: alembic revision --autogenerate -m "Description"
- the run: alembic upgrade head

## Lisence

- This project is lisenced by Peter Nyagol and was supervised by Edwinna Bikeri