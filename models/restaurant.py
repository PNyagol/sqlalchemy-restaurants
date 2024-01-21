from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
