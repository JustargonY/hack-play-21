import os

from logging import getLogger


logger = getLogger(__name__)

# --- OpenAI / LLM ---
SCW_SECRET_KEY = os.getenv("SCW_SECRET_KEY")
