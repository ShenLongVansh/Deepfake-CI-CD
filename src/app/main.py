from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
import time
from pathlib import Path

app = FastAPI(title="VoiceGuardAI Mock Inference")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class PredictRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok", "timestamp": time.time()}

@app.post("/predict")
def predict(data: dict):
    if not data:
        raise HTTPException(
            status_code=400,
            detail="Request body cannot be empty"
        )

    return {
        "label": random.choice(["real", "fake"]),
        "confidence": round(random.uniform(0.8, 0.99), 2),
        "input": data
    }


# will add error handling for empty input later after model integration

@app.post("/predict-file")
async def predict_file(file: UploadFile = File(...)):
    return {
        "label": random.choice(["real", "fake"]),
        "confidence": round(random.uniform(0.75, 0.99), 2),
        "filename": file.filename
    }

@app.get("/", response_class=HTMLResponse)
def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return HTMLResponse("<h3>UI not found</h3>")
