FROM python:3.11-slim

WORKDIR /app

# függőségek
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# projekt másolása
COPY . .

# port
EXPOSE 8000

# indulás
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
