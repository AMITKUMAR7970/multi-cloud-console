// WebSocket service stub 
export function connectJobLogStream(userId: string, jobId: number, onMessage: (msg: string) => void) {
  const ws = new WebSocket(`ws://localhost:8000/ws/jobs/${userId}/${jobId}/logs`);
  ws.onmessage = (event) => onMessage(event.data);
  return ws;
}