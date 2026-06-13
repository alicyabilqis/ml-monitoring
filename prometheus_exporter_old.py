from prometheus_client import start_http_server, Gauge
import random, time

metrics = {
    'cpu_usage': Gauge('cpu_usage', 'CPU usage'),
    'memory_usage': Gauge('memory_usage', 'Memory usage'),
    'latency': Gauge('prediction_latency', 'Model prediction latency'),
    'request_count': Gauge('request_count', 'Total number of requests'),
    'error_rate': Gauge('error_rate', 'Rate of errors'),
    'disk_io': Gauge('disk_io', 'Disk I/O rate'),
    'gpu_usage': Gauge('gpu_usage', 'GPU usage %'),
    'inference_time': Gauge('inference_time', 'Time for one inference'),
    'throughput': Gauge('throughput', 'Requests per second'),
    'queue_size': Gauge('queue_size', 'Queue of waiting predictions'),
}

def generate_metrics():
    while True:
        for m in metrics.values():
            m.set(random.uniform(0, 100))
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    generate_metrics()
