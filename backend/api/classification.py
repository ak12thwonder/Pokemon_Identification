from fastapi import APIRouter

router = APIRouter()

# Example endpoint
@router.post("/predict")
def predict():
    return {"message": "Prediction endpoint"}