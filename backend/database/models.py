from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PokemonStats(Base):
    __tablename__ = 'pokemon_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(String)
    abilities = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    special_attack = Column(Integer)
    special_defense = Column(Integer)
    speed = Column(Integer)

class Prediction(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    species = Column(String, nullable=False)
    verified = Column(String, default='not_verified')  # 'correct', 'wrong', 'not_verified'
    correct_species = Column(String, nullable=True)    # Only filled if verified == 'wrong'
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
