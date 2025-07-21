'''Fetching the data(Stats of the pokemon) from the API And saving as the output of the 
in the csv formate   '''


import requests
import pandas as pd
import os
import time

# Constants
POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'
OUTPUT_DIR = os.path.join('..', 'data', 'stats')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'pokemon_stats.csv')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_total_pokemon():
    url = f"{POKEAPI_URL}?limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to get total Pokémon count")
    return response.json()['count']

def fetch_pokemon_data(pokemon_id): 
    url = f"{POKEAPI_URL}{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for Pokémon ID {pokemon_id} (status code: {response.status_code})")
    data = response.json()
    # Extract relevant fields
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    types = [t['type']['name'] for t in data['types']]
    abilities = [a['ability']['name'] for a in data['abilities']]
    return {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'types': ','.join(types),
        'abilities': ','.join(abilities),
        'hp': stats.get('hp'),
        'attack': stats.get('attack'),
        'defense': stats.get('defense'),
        'special-attack': stats.get('special-attack'),
        'special-defense': stats.get('special-defense'),
        'speed': stats.get('speed'),
    }

def main():
    total_pokemon = get_total_pokemon()
    print(f"Total Pokémon: {total_pokemon}")
    pokemon_list = []
    try:
        for i in range(1, total_pokemon + 1):
            print(f"Fetching Pokémon ID {i}...")
            data = fetch_pokemon_data(i)
            if data:
                pokemon_list.append(data)
            time.sleep(0.2)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if pokemon_list:
            df = pd.DataFrame(pokemon_list)
            df.to_csv(OUTPUT_FILE, index=False)
            print(f"Saved stats for {len(df)} Pokémon to {OUTPUT_FILE}")

if __name__ == "__main__":
    main() 