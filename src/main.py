import uvicorn

from fastapi import FastAPI
from src.routes.signal import signal_router
from src.config import connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)
app.include_router(signal_router)

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

@app.get("/")
def emergency():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # cursor = connection.cursor()
    #
    # query = "SELECT * FROM messages_em;"
    # cursor.execute(query)
    #
    # results = cursor.fetchall()
    # column_names = [desc[0] for desc in cursor.description]
    # print(column_names)
    # print(results)
