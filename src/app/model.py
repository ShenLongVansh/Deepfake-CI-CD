import os
from transformers import pipeline

MODEL_PATH = os.getenv("MODEL_PATH", "/opt/models/deepfake")

classifier = None
MODEL_MODE = "mock"

if os.path.exists(MODEL_PATH):
    try:
        classifier = pipeline(
            "image-classification",
            model=MODEL_PATH,
            device="cpu"
        )
        MODEL_MODE = "local"
        print("✅ Loaded local deepfake model")
    except Exception as e:
        print("❌ Failed to load model:", e)
else:
    print("⚠️ Model path not found, using mock mode")
