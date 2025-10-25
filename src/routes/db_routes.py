from fastapi import APIRouter
from src.config import connection


db_router = APIRouter()

@db_router.get("/messages_incoming")
async def get_messages_incoming():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_incoming order by timestamp desc limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results

@db_router.get("/messages_em")
async def get_messages_em():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_em order by timestamp desc limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results

@db_router.get("/messages_sent")
async def get_messages_sent():
    cursor = connection.cursor()

    query = "SELECT * FROM messages_sent order by timestamp desc limit(10);"
    cursor.execute(query)

    results = cursor.fetchall()
    return results
