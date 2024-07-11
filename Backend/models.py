from sqlalchemy import Boolean, Column, Integer, Float, String, DateTime, ForeignKey, Date, func
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    password = Column(String)


class Record(Base):
    __tablename__ = 'records'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    analysis = Column(String)
    date_recorded = Column(DateTime)