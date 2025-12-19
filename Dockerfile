# STAGE 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Prevent Python from writing pyc files 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies into a temporary location
COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# STAGE 2: Final Runtime
FROM python:3.11-slim

WORKDIR /app

# Create a non-root user (trying to make it secure as well)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy only the compiled wheels from the builder stage
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install the wheels
RUN pip install --no-cache --no-index /wheels/* \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip

COPY src /app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Using python -m uvicorn is slightly safer for path resolution
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]