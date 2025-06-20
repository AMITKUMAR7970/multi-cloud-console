# Core module: config 
import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")
    GRAFANA_URL = os.getenv("GRAFANA_URL", "http://grafana:3000")
    GRAFANA_API_KEY = os.getenv("GRAFANA_API_KEY", "")
    SECRET_KEY = os.getenv("SECRET_KEY", "REPLACE_WITH_SECRET")

settings = Settings()