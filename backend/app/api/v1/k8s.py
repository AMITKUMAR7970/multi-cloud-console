# FastAPI router for k8s 
from fastapi import APIRouter, Depends, HTTPException
from app.services.k8s import list_clusters, get_cluster_info
from app.core.security import get_current_user

router = APIRouter()

@router.get("/clusters")
def clusters(user=Depends(get_current_user)):
    try:
        return list_clusters(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/clusters/{cluster_id}")
def cluster_info(cluster_id: str, user=Depends(get_current_user)):
    try:
        return get_cluster_info(cluster_id, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))