from pydantic import BaseModel
from typing import Optional


class EmergencySignal(BaseModel):
    user_id: str
    cell_id: int
    timestamp: float
    text: Optional[str] = None


class ExternalServicesMessage(BaseModel):
    user: str
    timestamp: float
    text: Optional[str] = None


class LLMResponse(BaseModel):
    category: str
    confidence: float
    explanation: str
