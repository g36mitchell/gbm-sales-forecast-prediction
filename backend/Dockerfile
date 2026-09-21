FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/app.py .
COPY backend/superkart_model.joblib .

EXPOSE 7860

CMD ["gunicorn", "-w", "4", "app:sales_prediction_api", "--bind", "0.0.0.0:7860"]
