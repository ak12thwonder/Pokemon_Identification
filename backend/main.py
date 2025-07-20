from fastapi import FastAPI
from fastapi.responses import JSONResponse
from backend.api import stats, classification

app = FastAPI(
    title="Pokémon Identifier & Stats Viewer",
    description="API for Pokémon image classification and stats retrieval",
    version="1.0.0"
)

# Register the stats and classification API routers
app.include_router(stats.router)
app.include_router(classification.router)

@app.get("/")
def root():
    return JSONResponse(content={
        "message": "Welcome to the Pokémon Identifier & Stats Viewer API!",
        "usage": [
            "GET /stats/{species_name} - Get stats for a Pokémon species (e.g., /stats/Bulbasaur)",
            "POST /predict - Upload an image to get Pokémon species prediction"
        ],
        "docs": "/docs (Swagger UI)"
    })


