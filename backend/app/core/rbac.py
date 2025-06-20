# Core module: rbac 
# Skeleton for RBAC
from fastapi import HTTPException

ROLES = {
    "admin": ["all"],
    "user": ["read", "launch_jobs"],
    "viewer": ["read"]
}

def check_permission(user, action):
    # Real implementation should fetch user roles from DB
    role = "admin" if user["email"].endswith("@admin.com") else "user"
    perms = ROLES.get(role, [])
    if action not in perms and "all" not in perms:
        raise HTTPException(status_code=403, detail="Forbidden")