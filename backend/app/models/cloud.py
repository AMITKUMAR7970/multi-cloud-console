# Pydantic model for cloud 
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    cloud: str
    action: str
    status: str = "pending"
    log: str = ""
    started_at: datetime = Field(default_factory=datetime.utcnow)
    finished_at: Optional[datetime] = None

    @classmethod
    def create_job(cls, db, user_id, action, cloud):
        job = cls(user_id=user_id, cloud=cloud, action=action, status="running")
        db.add(job)
        db.commit()
        db.refresh(job)
        return job

    @classmethod
    def append_log(cls, db, job_id, line):
        job = db.get(cls, job_id)
        job.log += line
        db.add(job)
        db.commit()
        return job

    @classmethod
    def set_status(cls, db, job_id, status):
        job = db.get(cls, job_id)
        job.status = status
        if status in ("success", "failure"):
            job.finished_at = datetime.utcnow()
        db.add(job)
        db.commit()
        return job