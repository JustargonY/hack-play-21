import uvicorn
import os

from fastapi import FastAPI
from src.routes.signal import signal_router
from src.config import connection

app = FastAPI(debug=True)
app.include_router(signal_router)

@app.get("/")
def emergency():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # cursor = connection.cursor()
    #
    # query = "SELECT * FROM messages_incoming;"
    # cursor.execute(query)
    #
    # results = cursor.fetchall()
    # column_names = [desc[0] for desc in cursor.description]
    # print(column_names)
