# Service logic for grafana 
import requests
import os

GRAFANA_URL = os.getenv("GRAFANA_URL", "http://grafana:3000")
GRAFANA_API_KEY = os.getenv("GRAFANA_API_KEY", "")

def get_grafana_dashboards():
    headers = {"Authorization": f"Bearer {GRAFANA_API_KEY}"}
    r = requests.get(f"{GRAFANA_URL}/api/search", headers=headers)
    r.raise_for_status()
    return r.json()