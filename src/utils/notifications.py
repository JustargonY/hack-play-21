from ..models import EmergencySignal, ExternalServicesMessage, LLMResponse, DisasterMessage
from ..config import logger
from openai import OpenAI
from src.config import SCW_SECRET_KEY, connection
import json

import datetime


async def send_to_external_service(signal: EmergencySignal, response: LLMResponse):
    llm_message = await generate_message_for_external_service(signal, response)
    print(llm_message)
    print(datetime.datetime.now())
    message = ExternalServicesMessage(
        lat=signal.lat,
        lon=signal.lon,
        message=llm_message['message'],
        em_type = llm_message['category'],
    )
    log_message_for_external_service_to_db(message)
    return {"message": message}

async def send_sms(signal: EmergencySignal):
    logger.info(f"Sent SMS: {signal.message}")
    return {"message": signal.message}


async def generate_message_for_external_service(signal: EmergencySignal, llm_response: LLMResponse):
    client = OpenAI(
        base_url="https://api.scaleway.ai/1bd896b3-3aab-4161-98b5-b3d525511efd/v1",
        api_key=SCW_SECRET_KEY,
    )

    prompt = (
        "You are an assistant that reports emergency messages.\n"
        f"You have message text from the user : '{signal.message}'\n"
        f"Also you have message text from another model that verifies this message and you have explanation why it is an emergency: '{llm_response.explanation}'\n"
        f"And category: '{llm_response.category}'\n"
        f"And level of confidence: '{llm_response.confidence}'\n"
        "You need to generate official message for public services describing the emergency situation.\n"
        "Respond as JSON with fields: category, message, confidence (0-1).\n"
        "Do not ask any questions, you just need to write a report for public services.\n"
        "Also remember that location is already given to the services"
    )

    response = client.chat.completions.create(
        model="gemma-3-27b-it",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=1,
        top_p=0.95,
        presence_penalty=0,
    )

    content = response.choices[0].message.content.replace('```json', '').replace('```', '').strip()
    parsed = json.loads(content)
    return parsed


def log_input_to_db(signal: EmergencySignal):
    try:
        cursor = connection.cursor()
        query = """
                INSERT INTO messages_incoming
                VALUES (%s, %s, %s, %s, %s, %s) 
                RETURNING user_id, lon, lat, timestamp, cell_id, message
                """
        cursor.execute(query, (
            signal.user_id,
            signal.lon,
            signal.lat,
            signal.timestamp,
            signal.cell_rk,
            signal.message
        ))
        result = cursor.fetchone()
        connection.commit()
        print('written to database')
    except Exception as error:
        print(error)


def log_message_for_external_service_to_db(signal: ExternalServicesMessage):
    try:
        cursor = connection.cursor()
        query = """
                INSERT INTO messages_emergency
                VALUES (%s, %s, %s, %s) RETURNING user_id, lat, lon, message, timestamp, emergency_type
                """
        cursor.execute(query, (
            signal.user_id,
            signal.lat,
            signal.lon,
            signal.message,
            signal.timestamp,
            signal.emergency_type,
        ))
        result = cursor.fetchone()
        connection.commit()
        print('written to database')
    except Exception as error:
        print(error)


def get_users_to_send_message(signal: ExternalServicesMessage, connection):
    cell_rk = signal.cell_id
    try:
        cursor = connection.cursor()
        query = ("SELECT user_id FROM user_locations_hackplay_sample"
                 f"where cell_rk = {cell_rk};")
        cursor.execute(query)
    except Exception as error:
        print(error)


def log_message_for_publicity_to_db(message: DisasterMessage, connection):
    pass
