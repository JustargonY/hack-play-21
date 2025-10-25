import uvicorn

from fastapi import FastAPI
from src.routes.signal import signal_router
from src.routes.db_routes import db_router
from src.config import connection
from src.models import EmergencySignal
from fastapi.middleware.cors import CORSMiddleware
from src.utils.helpers import get_users_to_send_message

app = FastAPI(debug=True)
app.include_router(signal_router)
app.include_router(db_router)

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

    # signal = EmergencySignal(
    #     user_id='xxx',
    #     cell_rk=1198824411,
    #     message='xd',
    # )
    #
    # for i in get_users_to_send_message(signal, connection):
    #     print(i)

    # cursor = connection.cursor()
    #
    # query = "SELECT * FROM messages_em;"
    # cursor.execute(query)
    #
    # results = cursor.fetchall()
    # column_names = [desc[0] for desc in cursor.description]
    # print(column_names)
    # print(results)
