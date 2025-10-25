from fastapi import APIRouter, BackgroundTasks
from src.config import connection


db_router = APIRouter()

@db_router.get("/messages_incoming")
async def get_messages_incoming():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_em limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results

@db_router.get("/messages_em")
async def get_messages_em():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_em limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results

@db_router.get("/messages_sent")
async def get_messages_sent():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_sent limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results
