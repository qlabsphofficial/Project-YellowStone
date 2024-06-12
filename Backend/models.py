from sqlalchemy import Boolean, Column, Integer, Float, String, DateTime, ForeignKey, Date, func
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    email = Column(String)
    contact_no = Column(String)
    address = Column(String)
    profile_picture = Column(String)

    resume = relationship('Resume', back_populates='user')
    owner_notifs = relationship('Notification', back_populates='notif_owner')
