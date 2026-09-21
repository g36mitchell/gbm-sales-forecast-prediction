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
