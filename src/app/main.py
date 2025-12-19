from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, HttpUrl
from app.model import classifier, MODEL_MODE
from PIL import Image
import io
import requests
import time
from pathlib import Path
import random

app = FastAPI(title="VoiceGuardAI Inference API")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

class PredictURLRequest(BaseModel):
    image_url: HttpUrl

# Routes 

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": time.time(),
        "model_mode": MODEL_MODE
    }

@app.post("/predict")
def predict_from_url(req: PredictURLRequest):
    if MODEL_MODE != "local":
        raise HTTPException(status_code=503, detail="Model not loaded")

    try:
        response = requests.get(req.image_url, timeout=10)
        response.raise_for_status()

        image = Image.open(io.BytesIO(response.content)).convert("RGB")
        result = classifier(image, padding=True)

        return {
            "label": result[0]["label"],
            "confidence": round(result[0]["score"], 3),
            "mode": "real-model",
            "source": "url"
        }

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=400, detail="Unable to fetch image from URL")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#  -> Prediction routes

@app.post("/predict-file")
async def predict_file(file: UploadFile = File(...)):
    contents = await file.read()

    if MODEL_MODE == "local":
        try:
            image = Image.open(io.BytesIO(contents)).convert("RGB")
            result = classifier(image, padding=True)

            return {
                "label": result[0]["label"],
                "confidence": round(result[0]["score"], 3),
                "mode": "real-model",
                "filename": file.filename
            }

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # fallback mock (safety)
    return {
        "label": random.choice(["real", "fake"]),
        "confidence": round(random.uniform(0.75, 0.99), 2),
        "mode": "mock-model",
        "filename": file.filename
    }


# UI

@app.get("/", response_class=HTMLResponse)
def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return HTMLResponse("<h3>UI not found</h3>")
