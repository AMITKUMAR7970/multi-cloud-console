# FastAPI router for monitoring 
from fastapi import APIRouter, Depends, HTTPException
from app.services.prometheus import query_prometheus
from app.services.grafana import get_grafana_dashboards
from app.core.security import get_current_user

router = APIRouter()

@router.get("/prometheus/query")
def prometheus_query(q: str, user=Depends(get_current_user)):
    try:
        return query_prometheus(q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/grafana/dashboards")
def grafana_dashboards(user=Depends(get_current_user)):
    try:
        return get_grafana_dashboards()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))