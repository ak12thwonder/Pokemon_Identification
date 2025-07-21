from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

router = APIRouter()

# Load the model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models',
'pokemon_resnet_model.keras')
model = load_model(MODEL_PATH)

# Get class names from the folder structure
IMAGES_DIR = os.path.join('data', 'processed', 'pokemon_images_255_class')
class_names = sorted([d for d in os.listdir(IMAGES_DIR) if os.path.isdir(os.path.join(IMAGES_DIR, d))])

def preprocess_image(image_bytes):
    img = Image.open(image_bytes).convert('RGB')
    img = img.resize((128, 128))
    arr = np.array(img)  # Do NOT divide by 255 here!
    arr = np.expand_dims(arr, axis=0)
    return arr

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        img_array = preprocess_image(file.file)
        preds = model.predict(img_array)
        pred_idx = np.argmax(preds, axis=1)[0]
        species = class_names[pred_idx]
        return JSONResponse(content={"species": species})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")