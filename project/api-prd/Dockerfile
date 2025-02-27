FROM python:3.9-slim

# Install system dependencies for numerical and scientific Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    libatlas-base-dev \
    liblapack-dev \
    libopenblas-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY recommendation_api.py .
COPY als_model_v2.pkl .

EXPOSE 8000

CMD ["uvicorn", "recommendation_api:app", "--host", "0.0.0.0", "--port", "8000"]