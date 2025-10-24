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


# def generate_message_for_external_service(signal: EmergencySignal, llm_response:):
#     client = OpenAI(
#         base_url="https://api.scaleway.ai/1bd896b3-3aab-4161-98b5-b3d525511efd/v1",
#         api_key=SCW_SECRET_KEY,
#     )
#
#     prompt = (
#         "You are an assistant that classifies emergency messages.\n"
#         "Respond as JSON with fields: category, confidence (0-1), explanation.\n"
#         f"Message: '{text}'\n"
#         "Categories: medical, fire, flood, earthquake, violence, accident, false, ambiguous, other."
#         "If there no emergency at all category must be false"
#     )
#
#     response = client.chat.completions.create(
#         model="gemma-3-27b-it",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=512,
#         temperature=1,
#         top_p=0.95,
#         presence_penalty=0,
#     )

def log_to_db(signal: EmergencySignal):
    pass
