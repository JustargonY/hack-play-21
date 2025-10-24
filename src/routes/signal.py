from fastapi import APIRouter, BackgroundTasks
from ..models import EmergencySignal
from ..utils.notifications import send_sms, send_to_external_service, log_input_to_db
from ..utils.verification import verificate_signal
from ..config import connection

signal_router = APIRouter()

@signal_router.post("/signal")
async def receive_signal(signal: EmergencySignal, background: BackgroundTasks):

    # write signal to db
    # log_input_to_db(signal, connection)

    # validate data if it is emergency
    # if valid - report
    response = await verificate_signal(signal)
    if response.category != 'false' and response.confidence >= 0.8:
        background.add_task(send_to_external_service, signal, response)
        # if needed - broadcast to people nearby TODO
        background.add_task(send_sms, signal)
    else:
        print("verification failed")
        return {'message': 'Verification failed'}

    return {'message': 'Signal processed'}
