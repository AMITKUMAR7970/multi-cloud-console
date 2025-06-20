# FastAPI router for cost 
from fastapi import APIRouter, Depends, HTTPException
from app.services.cost import get_cloud_costs
from app.core.security import get_current_user

router = APIRouter()

@router.get("/")
def cloud_costs(user=Depends(get_current_user)):
    try:
        return get_cloud_costs(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))