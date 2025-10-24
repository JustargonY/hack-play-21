from ..models import EmergencySignal
from fastapi import BackgroundTasks


def verificate_signal(signal: EmergencySignal, background: BackgroundTasks):
    return True