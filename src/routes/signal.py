from fastapi import APIRouter, BackgroundTasks
from ..models import EmergencySignal
from ..utils.notifications import send_sms, send_to_external_service, log_input_to_db
from ..utils.verification import verify_signal, verify_for_broadcasting
from ..utils.aggregator import record_aggregator, aggregator_count


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
    record_aggregator(signal.cell_rk, response.confidence)
    agg_count = aggregator_count(signal.cell_rk)
    if response.category != 'false' and response.confidence >= 0.8 or agg_count >= 3:
        background.add_task(send_to_external_service, signal, response)
        # if needed - broadcast to people nearby
        dis_response = await verify_for_broadcasting(signal, response)
        print(dis_response)
        if dis_response.confidence >= 0.8 or agg_count >= 5:
            print('it is massive emergency')
            background.add_task(send_sms, signal, response)
    else:
        print("verification failed")
        return {'message': 'Verification failed: confidence is too low'}

    return {'message': 'Signal processed: messages sent to needed agents'}
