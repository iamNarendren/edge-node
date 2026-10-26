"""Edge node simulation: filter temperature readings locally."""
import json, random, time

THRESHOLD = 35.0

def generate_readings(n, seed=42):
    random.seed(seed)
    return [{"sensor": i % 8, "temp": round(random.uniform(20, 45), 2)} for i in range(n)]

def run_edge_node(n, threshold=THRESHOLD):
    readings = generate_readings(n)

    start = time.perf_counter()
    alerts = [r for r in readings if r["temp"] > threshold]   # local filtering
    elapsed = time.perf_counter() - start

    raw_bytes = len(json.dumps(readings).encode())      # send everything to cloud
    edge_bytes = len(json.dumps(alerts).encode())       # send only alerts

    return {
        "n": n,
        "threshold": threshold,
        "time_s": elapsed,
        "alerts": len(alerts),
        "filtered_pct": 100 * (n - len(alerts)) / n,
        "raw_bytes": raw_bytes,
        "edge_bytes": edge_bytes,
        "saved_pct": 100 * (raw_bytes - edge_bytes) / raw_bytes,
        "max_temp": max(r["temp"] for r in readings),
    }
