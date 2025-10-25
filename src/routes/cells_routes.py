from fastapi import APIRouter
from src.routes.ws_routes import broadcast_message

cells_router = APIRouter()

# Just to test from backend
@cells_router.post("/cells/{cell_rk}/alert")
async def trigger_alert(cell_rk: int):
    await broadcast_message({
        "type": "cell_update",
        "cell_rk": cell_rk,
        "status": "alert"
    })
    return {"cell_rk": cell_rk, "status": "alerted"}

@cells_router.post("/cells/{cell_rk}/clear")
async def clear_alert(cell_rk: int):
    await broadcast_message({
        "type": "cell_update",
        "cell_rk": cell_rk,
        "status": "normal"
    })
    return {"cell_rk": cell_rk, "status": "cleared"}