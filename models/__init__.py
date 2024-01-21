# models/__init__.py
from .base import Base
from .restaurant import Restaurant
from .customer import Customer
from .review import Review
from main import engine


Base.metadata.create_all(bind=engine)
