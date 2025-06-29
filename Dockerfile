FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pydantic

EXPOSE 5000

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "5000"]
