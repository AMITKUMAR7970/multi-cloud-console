# WebSocket notify logic 
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List

router = APIRouter()
connections: Dict[str, Dict[int, List[WebSocket]]] = {}  # user_id: {job_id: [ws, ...]}

@router.websocket("/jobs/{user_id}/{job_id}/logs")
async def ws_job_logs(ws: WebSocket, user_id: str, job_id: int):
    await ws.accept()
    job_id = int(job_id)
    user_conns = connections.setdefault(user_id, {})
    job_conns = user_conns.setdefault(job_id, [])
    job_conns.append(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        job_conns.remove(ws)

async def broadcast_job_update(user_id: str, job_id: int, msg: str):
    for ws in connections.get(user_id, {}).get(job_id, []):
        await ws.send_text(msg)