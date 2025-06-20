from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from app.services.aws import list_ec2_instances
from app.services.azure import list_azure_vms
from app.services.gcp import list_gcp_instances
from app.services.terraform import start_terraform_apply
from app.models.cloud import Job
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()

@router.get("/aws/instances")
def aws_instances(user=Depends(get_current_user)):
    try:
        return list_ec2_instances(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/azure/vms")
def azure_vms(user=Depends(get_current_user)):
    try:
        return list_azure_vms(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/gcp/instances")
def gcp_instances(user=Depends(get_current_user)):
    try:
        return list_gcp_instances(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/terraform/apply")
def terraform_apply(
    module: str = Query(..., description="Terraform module name (e.g. aws, azure, gcp)"),
    background_tasks: BackgroundTasks = None,
    user=Depends(get_current_user),
    db=Depends(get_db)
):
    job = Job.create_job(db, user_id=user["id"], action="terraform-apply", cloud=module)
    background_tasks.add_task(start_terraform_apply, module, job.id, user["id"])
    return {"job_id": job.id, "status": "started"}