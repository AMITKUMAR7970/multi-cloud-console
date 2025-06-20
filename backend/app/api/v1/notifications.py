# FastAPI router for notifications 
from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

# This is a stub. Real implementation would push/pull notifications from a DB or queue
@router.get("/")
def notifications(user=Depends(get_current_user)):
    return [{
        "id": 1,
        "type": "job",
        "message": "Terraform apply completed.",
        "read": False
    }]