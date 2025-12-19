# CI/CD Pipeline for Model Processing (VoiceGuardAI)
🔗 Live Deployment: http://167.71.235.99:8000/

This project is part of **Task 11: CI/CD Pipeline for Deepfake Processing**, focused on building a **fully automated CI/CD pipeline** for an inference service.

The primary objective is to demonstrate **DevOps best practices**: automated testing, containerization, continuous integration, and continuous deployment — not model accuracy or frontend sophistication.

---

## 🚀 Current Project State (Final)

This repository contains a **FastAPI-based inference service** (currently using a mock detection layer) that is:

- Automatically tested on every code change
- Containerized using Docker
- Built and pushed via GitHub Actions
- Deployed automatically to a **DigitalOcean Droplet**
- Updated end-to-end with **zero manual deployment steps**

The system is intentionally designed so that a **real deepfake detection model can be integrated later without modifying the CI/CD pipeline**.

---

## ✅ What Is Implemented Today

### 🧠 Inference API
- FastAPI backend exposing:
  - `GET /health` → runtime health check
  - `POST /predict` → mock inference via JSON input
  - `POST /predict-file` → mock inference via file upload
- A mock prediction layer is used to:
  - keep CI deterministic
  - avoid coupling infrastructure to model training
  - ensure deployment stability

---

### 🌐 Lightweight Web UI
- Simple HTML/CSS/JavaScript UI served by FastAPI
- Allows:
  - URL-based prediction
  - File upload & prediction
- UI exists **only for runtime validation and demonstration**
- No frontend frameworks used by design

---

### 🧪 Automated Testing
- PyTest-based API smoke tests
- Tests validate:
  - application startup
  - `/health` endpoint
  - inference endpoints
- Tests act as **CI quality gates**
- Deployment is blocked if tests fail

---

### 🐳 Containerization
- Fully Dockerized application
- Uses a slim Python base image
- Installs only runtime dependencies
- Clean, repeatable builds

---

### 🔁 CI/CD Pipeline (Fully Functional)
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
- **Frontend (demo only):** HTML, CSS, Vanilla JavaScript  

---

## 📁 Repository Structure

| Path                    | Description                         |
|-------------------------|-------------------------------------|
| `.github/workflows/`    | CI/CD pipeline definitions          |
| `docker/`               | Docker compose configuration        |
| `src/app/`              | FastAPI application                 |
| `tests/`                | API smoke tests                     |
| `requirements.txt`      | Runtime dependencies                |
| `requirements-dev.txt`  | Development & test dependencies     |
| `pyproject.toml`        | Python packaging configuration      |

---

## 🔮 Future Improvements (Planned, Not Implemented)

These are **intentional future extensions**, not missing features:

### 🔹 Model Integration
- Replace mock inference layer with a real deepfake detection model
- No CI/CD or deployment changes required

### 🔹 Observability
- Structured logging
- Request IDs
- Basic metrics (latency, error rate)

### 🔹 Security & Validation
- Input validation (file size, MIME types)
- Rate limiting
- Authentication for inference endpoints

### 🔹 Deployment Enhancements
- Image versioning & rollback strategy
- Blue/green or canary deployments
- Infrastructure-as-Code (Terraform)

These improvements can be added incrementally without architectural changes.

---

## 🎯 Scope & Design Philosophy

### In Scope
- CI/CD automation
- Deterministic testing
- Clean containerization
- Reliable deployments
- DevOps-first thinking

### Explicitly Out of Scope
- More recent model, for improved confidence scores
- Advanced frontend development
- Complex observability stacks (Prometheus, Grafana) as the project grows.

This aligns with the task guideline:

> *“Pipeline can be simple but complete. Focus on automation, not complexity.”*

---

## 🔍 Verification

- CI/CD runs are visible via **GitHub Actions**
- Live deployment URL included above
- API contract inspectable via `/docs`

---

## 📝 Notes

This README reflects the **final state of the project at submission time**.  
The repository is intentionally structured to support future growth without reworking the existing CI/CD pipeline.
