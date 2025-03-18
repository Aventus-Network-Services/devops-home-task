from sqlalchemy import Column, Integer, String, DateTime
import datetime
import os
import sys

# Import Base from the right location
from app.database import Base

class User(Base):
    __tablename__ = "users"
    # Add this parameter to allow the table to be redefined
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    city = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow) 
