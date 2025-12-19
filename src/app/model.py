import os
from transformers import pipeline

MODEL_PATH = os.getenv("MODEL_PATH")

if MODEL_PATH and os.path.exists(MODEL_PATH):
    classifier = pipeline(
        "image-classification",
        model=MODEL_PATH,
        device="cpu"
    )
    MODEL_MODE = "local"
else:
    classifier = None
    MODEL_MODE = "mock"
