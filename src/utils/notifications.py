import psycopg2

from ..models import EmergencySignal, ExternalServicesMessage, LLMResponse
from ..config import logger
from openai import OpenAI
from src.config import SCW_SECRET_KEY

import time


async def send_to_external_service(signal: EmergencySignal, response: LLMResponse):
    message = ExternalServicesMessage(
        user=signal.user_id,
        timestamp=time.time(),
        text=signal.text,
    )
    print(message)
    return {"message": message}

async def send_sms(signal: EmergencySignal):
    logger.info(f"Sent SMS: {signal.text}")
    print(signal.text)
    return {"message": signal.text}


def generate_message_for_external_service(signal: EmergencySignal, llm_response: LLMResponse):
    client = OpenAI(
        base_url="https://api.scaleway.ai/1bd896b3-3aab-4161-98b5-b3d525511efd/v1",
        api_key=SCW_SECRET_KEY,
    )

    prompt = (
        "You are an assistant that classifies emergency messages.\n"
        "Respond as JSON with fields: category, confidence (0-1), explanation.\n"
        f"Message: '{signal.text}'\n"
        "Categories: medical, fire, flood, earthquake, violence, accident, false, ambiguous, other."
        "If there no emergency at all category must be false"
    )

    response = client.chat.completions.create(
        model="gemma-3-27b-it",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=1,
        top_p=0.95,
        presence_penalty=0,
    )

def log_input_to_db(signal: EmergencySignal, connection):
    try:
        cursor = connection.cursor()

        query = ("insert into messages_incoming (user_id, cell_rk, start_dttm, text)\n"
                 f'values (\"{signal.user_id}\", {signal.cell_id}, {signal.timestamp}, \"{signal.text})\");')

        query = """
                INSERT INTO messages_incoming
                VALUES (%s, %s, %s, %s) 
                RETURNING user_id, cell_id, timestamp, text \
                """
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
