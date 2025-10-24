from fastapi import APIRouter, BackgroundTasks
from ..models import EmergencySignal, TestModel
from ..utils.notifications import send_sms, send_to_external_service
from ..utils.verification import verificate_signal

signal_router = APIRouter()

@signal_router.post("/signal", response_model=TestModel)
async def receive_signal(signal: EmergencySignal, background: BackgroundTasks):
    # TODO
    # check database if we have this cell
    # sql
    #
    # Record aggregation #TODO
    # possible record aggregation
    # record_aggregator(signal.cell_id, combined)
    # agg_count = aggregator_count(signal.cell_id)


    # validate data if it is emergency
    # if valid - report
    if verificate_signal(signal, background):
        background.add_task(send_to_external_service, signal)
        # if needed - broadcast to people nearby TODO
        background.add_task(send_sms, signal)

    return TestModel(id=signal.user)
