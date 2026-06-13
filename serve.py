from fastapi import FastAPI
from pydantic import BaseModel

from prometheus_client import (
    Counter,
    Gauge,
    start_http_server
)

import psutil
import time

app = FastAPI()

# Prometheus Port
start_http_server(8000)

# Metrics
REQUEST_COUNT = Counter(
    "request_count_total",
    "Total requests"
)

ERROR_COUNT = Counter(
    "error_count_total",
    "Total errors"
)

PREDICTION_COUNT = Counter(
    "prediction_count_total",
    "Total predictions"
)

LATENCY = Gauge(
    "prediction_latency_seconds",
    "Prediction latency"
)

CPU_USAGE = Gauge(
    "cpu_usage_percent",
    "CPU usage"
)

RAM_USAGE = Gauge(
    "ram_usage_percent",
    "RAM usage"
)

DISK_USAGE = Gauge(
    "disk_usage_percent",
    "Disk usage"
)

UPTIME = Gauge(
    "app_uptime_seconds",
    "Application uptime"
)

THROUGHPUT = Gauge(
    "throughput",
    "Requests processed"
)

QUEUE_SIZE = Gauge(
    "queue_size",
    "Queue size"
)

CONFIDENCE = Gauge(
    "confidence_score",
    "Prediction confidence"
)

APP_START = time.time()

# Input
class Input(BaseModel):
    example: str

# Root
@app.get("/")
def root():
    return {"status": "Model ready"}
    
# Inference
@app.post("/infer")
def infer(input: Input):

    REQUEST_COUNT.inc()

    start = time.time()

    try:

        result = {
            "prediction":
            f"Processed: {input.example}"
        }

        latency = time.time() - start

        LATENCY.set(latency)

        CPU_USAGE.set(
            psutil.cpu_percent()
        )

        RAM_USAGE.set(
            psutil.virtual_memory().percent
        )

        DISK_USAGE.set(
            psutil.disk_usage("/").percent
        )

        UPTIME.set(
            time.time() - APP_START
        )

        THROUGHPUT.set(
            REQUEST_COUNT._value.get()
        )

        QUEUE_SIZE.set(0)

        CONFIDENCE.set(0.95)

        PREDICTION_COUNT.inc()

        return result

    except Exception:

        ERROR_COUNT.inc()

        raise
