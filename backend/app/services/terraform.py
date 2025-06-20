# Service logic for terraform 
import asyncio
import subprocess
from app.websocket.notify import broadcast_job_update
from app.models.cloud import Job
from app.db.session import get_db

async def start_terraform_apply(module, job_id, user_id):
    tf_dir = f"infra/terraform/{module}"
    db = next(get_db())
    try:
        process = await asyncio.create_subprocess_exec(
            "terraform", "init",
            cwd=tf_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )
        async for line in process.stdout:
            text = line.decode()
            await broadcast_job_update(user_id, job_id, text)
            Job.append_log(db, job_id, text)
        await process.wait()

        process = await asyncio.create_subprocess_exec(
            "terraform", "apply", "-auto-approve",
            cwd=tf_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT
        )
        async for line in process.stdout:
            text = line.decode()
            await broadcast_job_update(user_id, job_id, text)
            Job.append_log(db, job_id, text)
        await process.wait()
        Job.set_status(db, job_id, "success" if process.returncode == 0 else "failure")
        await broadcast_job_update(user_id, job_id, f"\nJob finished with code {process.returncode}\n")
    except Exception as e:
        Job.append_log(db, job_id, f"\nError: {e}\n")
        Job.set_status(db, job_id, "failure")
        await broadcast_job_update(user_id, job_id, f"\nError: {e}\n")