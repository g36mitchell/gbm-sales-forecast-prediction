# gbm-sales-forecast-prediction
UT AIML Model Deployment Project - Flask API Backend + Streamlit Frontend (Dockerized)

## Local setup

The pinned dependencies target Python 3.11. Codespaces may default to a newer
Python version, which can make pip build `pandas` from source instead of using
its wheel. Use Python 3.11 for local installation:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

The version constraint uses two equals signs: `pandas==2.2.2`. The Dockerfiles
already use Python 3.11, so Docker-based setup does not require this workaround.

## Docker deployment in Codespaces

Run these commands from the repository root. Build commands create images; run
commands create the containers.

```bash
docker network create gbm-network

docker build -f backend/Dockerfile -t gbm-backend .
docker run -d \
	--name gbm-sales-backend \
	--network gbm-network \
	-p 7860:7860 \
	gbm-backend

docker build -f frontend/Dockerfile -t gbm-frontend frontend
docker run -d \
	--name gbm-sales-frontend \
	--network gbm-network \
	--add-host host.docker.internal:host-gateway \
	-p 8501:8501 \
	-e BACKEND_URL=http://host.docker.internal:7860 \
	gbm-frontend
```

The `BACKEND_URL` value is supplied when the frontend container starts, not
baked into the frontend image. In this Codespaces Docker setup,
`host.docker.internal` reaches the backend through the published host port.
Make ports `7860` and `8501` public in the Codespaces Ports view to obtain the
backend and frontend HTTPS URLs.
