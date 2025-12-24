import time
import random
from prometheus_client import start_http_server, Counter, Gauge, Histogram

# DEFINISI 10 METRIKS (WAJIB UNTUK ADVANCE)
PREDICTIONS = Counter('ml_predictions_total', 'Total prediksi')
HEART_DISEASE = Counter('ml_heart_disease_detected_total', 'Kasus sakit jantung')
NORMAL_HEART = Counter('ml_normal_heart_total', 'Kasus jantung normal')
ACCURACY = Gauge('ml_model_accuracy', 'Skor akurasi model')
LATENCY = Histogram('ml_inference_latency_seconds', 'Waktu proses')
CPU = Gauge('ml_cpu_usage_percent', 'Penggunaan CPU')
RAM = Gauge('ml_memory_usage_mb', 'Penggunaan RAM')
USERS = Gauge('ml_active_users', 'User aktif')
ERRORS = Counter('ml_processing_errors', 'Total error data')
VERSION = Gauge('ml_model_version', 'Versi model')

def update_metrics():
    PREDICTIONS.inc()
    if random.random() > 0.5:
        HEART_DISEASE.inc()
    else:
        NORMAL_HEART.inc()
    ACCURACY.set(random.uniform(0.88, 0.99))
    LATENCY.observe(random.uniform(0.05, 0.2))
    CPU.set(random.uniform(15, 55))
    RAM.set(random.uniform(150, 400))
    USERS.set(random.randint(1, 12))
    VERSION.set(1.0)
    if random.random() > 0.98:
        ERRORS.inc()

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter aktif di http://localhost:8000")
    while True:
        update_metrics()
        time.sleep(5)