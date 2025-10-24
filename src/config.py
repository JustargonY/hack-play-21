import os
import psycopg2

from logging import getLogger
from dotenv import load_dotenv
from openai import OpenAI


logger = getLogger(__name__)
load_dotenv()

# --- OpenAI / LLM ---
SCW_SECRET_KEY = os.getenv("SCW_SECRET_KEY")
SCW_ACCESS_KEY = os.getenv("SCW_ACCESS_KEY")

# --- DB connection ---
SCW_DB_USER = os.getenv("SCW_DB_USER")
SCW_DB_PASSWORD = os.getenv("SCW_DB_PASSWORD")
SCW_DB_NAME = os.getenv("SCW_DB_NAME")
SCW_DB_HOST = os.getenv("SCW_DB_HOST")
SCW_DB_PORT = os.getenv("SCW_DB_PORT")

connection = psycopg2.connect(
    host=SCW_DB_HOST,
    port=SCW_DB_PORT,
    database=SCW_DB_NAME,
    user=SCW_DB_USER,
    password=SCW_DB_PASSWORD,
)
