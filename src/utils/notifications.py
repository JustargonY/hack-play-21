from ..models import EmergencySignal, TestModel, ExternalServicesMessage
from ..config import logger

import time

async def send_to_external_service(signal: EmergencySignal):
    message = ExternalServicesMessage(
        user=signal.user,
        timestamp=time.time(),
        text=signal.text,
    )
    print(message)
    return {"message": message}

async def send_sms(signal: EmergencySignal):
    logger.info(f"Sent SMS: {signal.text}")
    print(signal.text)
    return {"message": signal.text}

def log_to_db(signal: EmergencySignal):
    pass
