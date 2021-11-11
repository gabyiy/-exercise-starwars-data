import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
      

class Character(Base):
    __tablename__='character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(30), nullable=False)
    favorite = relationship("Favorite")

class Planet(Base):
    __tablename__='planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer, nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer)  
    favorite = relationship("Favorite")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')