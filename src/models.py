import datetime

from pydantic import BaseModel
from typing import Optional


class EmergencySignal(BaseModel):
    user_id: str
    cell_rk: int
    lat: float = 53.4505555556
    lon: float = 14.5591666667
    timestamp: str = datetime.datetime.now()
    message: Optional[str] = None


class ExternalServicesMessage(BaseModel):
    lat: float
    lon: float
    message: str
    timestamp: str = datetime.datetime.now()
    em_type: str


class DisasterMessage(BaseModel):
    user_id: str
    cell_rk: int
    timestamp: str = datetime.datetime.now()
    message: str
    emergency_type: str


class LLMResponse(BaseModel):
    category: str
    confidence: float
    explanation: str
