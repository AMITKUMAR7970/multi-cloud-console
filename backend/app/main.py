from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import cloud, k8s, monitoring, cost, notifications, auth
from app.websocket import notify

app = FastAPI(
    title="Hybrid Cloud Manager",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(cloud.router, prefix="/api/v1/cloud", tags=["cloud"])
app.include_router(k8s.router, prefix="/api/v1/k8s", tags=["k8s"])
app.include_router(monitoring.router, prefix="/api/v1/monitoring", tags=["monitoring"])
app.include_router(cost.router, prefix="/api/v1/cost", tags=["cost"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["notifications"])
app.include_router(notify.router, prefix="/ws")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}