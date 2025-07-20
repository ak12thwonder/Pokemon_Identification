from fastapi import APIRouter, HTTPException
import pandas as pd
import os

router = APIRouter()

# Load stats CSV once at startup
stats_path = os.path.join("data", "stats", "pokemon_stats.csv")
stats_df = pd.read_csv(stats_path)

@router.get("/stats/{species_name}")
def get_pokemon_stats(species_name: str):
    row = stats_df[stats_df['name'].str.lower() == species_name.lower()]
    if row.empty:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    return row.iloc[0].to_dict()