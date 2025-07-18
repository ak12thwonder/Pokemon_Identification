from sqlalchemy import Column, Integer, String, Float
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
