FROM python:3.11-slim

WORKDIR /app

# Pehle requirements copy karo aur install karo (cache ke liye)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki ka code copy karo
COPY . .

# Server ko 8000 port pe chalane ka command
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]