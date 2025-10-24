from fastapi import APIRouter, BackgroundTasks
from ..models import EmergencySignal
from ..utils.notifications import send_sms, send_to_external_service, log_input_to_db
from ..utils.verification import verify_signal, verify_for_broadcasting


import datetime

signal_router = APIRouter()

@signal_router.post("/signal")
async def receive_signal(signal: EmergencySignal, background: BackgroundTasks):

    # write signal to db
    if signal.timestamp == '':
        signal.timestamp = datetime.datetime.now()
    log_input_to_db(signal)

    # validate data if it is emergency
    # if valid - report
    response = await verify_signal(signal)
    if response.category != 'false' and response.confidence >= 0.8:
        background.add_task(send_to_external_service, signal, response)
        # if needed - broadcast to people nearby
        if verify_for_broadcasting:
            background.add_task(send_sms, signal)
    else:
        print("verification failed")
        return {'message': 'Verification failed'}

    return {'message': 'Signal processed'}
