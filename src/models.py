from pydantic import BaseModel
from typing import Optional


class EmergencySignal(BaseModel):
    user: str
    cell_id: str
    timestamp: float
    text: Optional[str] = None


class ExternalServicesMessage(BaseModel):
    user: str
    timestamp: float
    text: Optional[str] = None


class TestModel(BaseModel):
    id: str
