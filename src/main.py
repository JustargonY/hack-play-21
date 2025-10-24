import uvicorn
import os

from fastapi import FastAPI
from src.routes.signal import signal_router

app = FastAPI(debug=True)
app.include_router(signal_router)

@app.get("/")
def emergency():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
