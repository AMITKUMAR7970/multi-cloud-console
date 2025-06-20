# Pydantic model for k8s 
from sqlmodel import SQLModel, Field
from typing import Optional

class Cluster(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    kubeconfig_secret: Optional[str] = None
    cloud: Optional[str] = None
    owner_id: Optional[int] = None