import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)  
    address = Column(String(50), nullable=False) 
    phone = Column(String(50), nullable=False) 
    date = Column(Date(), unique=True, nullable=False)

    favs = relationship("Fav", back_populates="user")
    characters = relationship("Character", back_populates="user")


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  
    description = Column(String(200), nullable=True)

    favs = relationship("Fav", back_populates="planet")
    characters = relationship("Character", back_populates="planet")
     

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  
    description = Column(String(200), nullable=True) 

    favs = relationship("Fav", back_populates="character")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="characters")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet", back_populates="characters")


class Fav(Base):
    __tablename__ = 'fav'
    
    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    id_character = Column(Integer, ForeignKey('character.id'), primary_key=True)
    id_planet = Column(Integer, ForeignKey('planet.id'), primary_key=True)

    user = relationship("User", back_populates="favs")
    character = relationship("Character", back_populates="favs")
    planet = relationship("Planet", back_populates="favs")

render_er(Base, 'diagram.png')