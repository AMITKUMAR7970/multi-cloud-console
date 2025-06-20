# Service logic for prometheus 
import requests
import os

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")

def query_prometheus(query: str):
    r = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": query})
    r.raise_for_status()
    return r.json()["data"]