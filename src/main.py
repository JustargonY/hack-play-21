import uvicorn

from fastapi import FastAPI
from src.routes.signal import signal_router
from src.routes.db_routes import db_router
from src.routes.cells_routes import cells_router
from src.routes.ws_routes import ws_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)
app.include_router(signal_router)
app.include_router(db_router)
app.include_router(cells_router)
app.include_router(ws_router)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
