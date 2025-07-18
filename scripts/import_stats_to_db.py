import pandas as pd
from backend.database.models import PokemonStats
from backend.database.session import SessionLocal

# Load CSV
df = pd.read_csv('data/stats/pokemon_stats.csv')

# Rename columns to match model if needed
df = df.rename(columns={
    'special-attack': 'special_attack',
    'special-defense': 'special_defense'
})

session = SessionLocal()
try:
    for _, row in df.iterrows():
        pokemon = PokemonStats(
            name=row['name'],
            height=row['height'],
            weight=row['weight'],
            types=row['types'],
            abilities=row['abilities'],
            hp=row['hp'],
            attack=row['attack'],
            defense=row['defense'],
            special_attack=row['special_attack'],
            special_defense=row['special_defense'],
            speed=row['speed']
        )
        session.add(pokemon)
    session.commit()
finally:
    session.close()
