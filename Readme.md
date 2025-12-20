# CI/CD Pipeline for Model Processing (VoiceGuardAI)  
🔗 Live Deployment: http://167.71.235.99:8000/

This project is part of **Task 11: CI/CD Pipeline for Deepfake Processing**, focused on building a **fully automated CI/CD pipeline** for an inference service.

The primary objective is to demonstrate **DevOps best practices** : automated testing, containerization, continuous integration, and continuous deployment — rather than model accuracy or frontend sophistication.

---

## 🚀 Project Overview (Final State)

This repository contains a **FastAPI-based inference service** with an integrated backend, frontend, and model interface that is:

- Automatically tested on every code change
- Containerized using Docker
- Built and pushed via GitHub Actions
- Deployed automatically to a **DigitalOcean Droplet**
- Updated end-to-end with **zero manual deployment steps**

The system is designed so that **model logic, infrastructure, and automation are cleanly decoupled**, enabling safe iteration without breaking CI/CD.

---

## ✅ What Is Implemented

### 🧠 Inference API
- FastAPI backend exposing:
  - `GET /health` → runtime health check
  - `POST /predict` → inference via structured JSON input
  - `POST /predict-file` → inference via file upload
- Inference layer is fully wired and validated through the API contract
- Model logic can be updated independently of the pipeline

---
### 🧩 Model Deployment & Runtime Integration

The deepfake detection model is deployed **outside the application container** on the DigitalOcean Droplet to allow independent model updates.

**Model location on droplet:**

```
/opt/models/deepfake

├── config.json
├── model.safetensors
└── preprocessor_config.json
```

**Integration approach:**
- The FastAPI service runs inside a Docker container
- The container accesses the model via a fixed filesystem path
- Model artifacts are **not baked into the Docker image**
- This allows:
  - updating or replacing the model without rebuilding images
  - keeping CI/CD pipelines deterministic
  - avoiding large model artifacts in the image registry

The inference API (`/predict`, `/predict-file`) is designed to remain stable regardless of model updates, ensuring that **CI/CD automation and deployment workflows remain unchanged**.

---

### 🔗 Model & Dataset References

The inference API is compatible with a real deepfake detection model and dataset used during development and validation:

- **Kaggle Images Dataset:** https://www.kaggle.com/code/dima806/deepfake-vs-real-faces-detection-vit/input
- **Hugging Face Model:** https://huggingface.co/dima806/deepfake_vs_real_image_detection

The model interface is already integrated into the backend.  
CI/CD automation, containerization, and deployment remain unchanged regardless of model updates.

---

### 🌐 Web UI (Runtime Validation)
- Lightweight HTML/CSS/JavaScript UI served directly by FastAPI
- Supports:
  - URL-based inference
  - File upload & inference
- UI is intentionally minimal and framework-free
- Exists **only for deployment validation and demo purposes**

---

### 🧪 Automated Testing
- PyTest-based API smoke tests
- Tests validate:
  - application startup
  - `/health` endpoint
  - inference endpoints
- Tests act as **CI quality gates**
- Deployment is **blocked** if tests fail

---

### 🐳 Containerization
- Fully Dockerized application
- Slim Python base image
- Only runtime dependencies included
- Clean, repeatable builds suitable for production

---

### 🔁 CI/CD Pipeline (Fully Automated)
- **GitHub Actions** workflow:
  - Runs tests on every push
  - Builds Docker image
  - Pushes image to Docker Hub
  - Deploys automatically to DigitalOcean via SSH
- No manual redeploys required
- CI failures prevent deployment

---

### ☁️ Deployment
- Hosted on **DigitalOcean**
- Service exposed on port `8000`
- Live endpoints:
  - `/` → Web UI
  - `/docs` → OpenAPI / Swagger documentation
  - `/health` → runtime health check

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn  
- **Testing:** PyTest, FastAPI TestClient  
- **Packaging:** `pyproject.toml`, requirements files  
- **Containerization:** Docker, Docker Compose  
- **CI/CD:** GitHub Actions  
- **Registry:** Docker Hub  
- **Deployment:** DigitalOcean (SSH-based continuous deployment)  
- **Frontend:** HTML, CSS, Vanilla JavaScript  

---

## 📁 Repository Structure

| Path                    | Description                         |
|-------------------------|-------------------------------------|
| `.github/workflows/`    | CI/CD pipeline definitions          |
| `docker/`               | Docker configuration                |
| `src/app/`              | FastAPI application                 |
| `tests/`                | API smoke tests                     |
| `requirements.txt`      | Runtime dependencies                |
| `requirements-dev.txt`  | Development & test dependencies     |
| `pyproject.toml`        | Python packaging configuration      |

---

## 🔮 Future Improvements (Optional Extensions)

These are **intentional enhancements**, not missing features:

### 🔹 Model Enhancements
- Improve accuracy and confidence calibration
- Support multiple model versions

### 🔹 Observability
- Structured logging
- Request tracing
- Basic metrics (latency, error rate)

### 🔹 Security
- File validation (size, MIME type)
- Rate limiting
- Auth-protected inference endpoints

### 🔹 Deployment Strategy
- Image versioning & rollback
- Blue/green or canary deployments
- Infrastructure-as-Code (Terraform)

All of the above can be added **without changing the existing CI/CD architecture**.

---

## 🎯 Scope & Design Philosophy

### In Scope
- CI/CD automation
- Deterministic testing
- Clean containerization
- Reliable deployments
- DevOps-first system design

### Explicitly Out of Scope
- Advanced frontend development
- Large-scale observability stacks
- Research-focused model experimentation

This aligns with the task guideline:

> *“Pipeline can be simple but complete. Focus on automation, not complexity.”*

---

## 🔍 Verification

- CI/CD runs visible via **GitHub Actions**
- Live deployment URL included above
- API contract inspectable via `/docs`

---

## 📝 Notes

This README reflects the **final state of the project at submission time**.  
The repository is structured to support future growth **without reworking the CI/CD pipeline**.
