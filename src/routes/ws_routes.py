from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

ws_router = APIRouter()
active_connections = []

async def broadcast_message(message: dict):
    disconnected = []
    for ws in active_connections:
        try:
            await ws.send_text(json.dumps(message))
        except Exception:
            disconnected.append(ws)
    for ws in disconnected:
        active_connections.remove(ws)

@ws_router.websocket("/api/ws/cells")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # keep alive
    except WebSocketDisconnect:
        active_connections.remove(websocket)
