
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

COPY .env /app/.env

CMD ["gunicorn", "StockMarketPrediction.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]