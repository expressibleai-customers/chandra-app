from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class AIAssistantBase(BaseModel):
    """Base model for AIAssistant"""

    name: str = Field(..., description="Name")

    relevant: str = None = Field(..., description="Relevant")

    helpful_responses: str = None = Field(..., description="Helpful Responses")



class AIAssistantCreate(AIAssistantBase):
    """Model for creating AIAssistant"""
    pass


class AIAssistantUpdate(AIAssistantBase):
    """Model for updating AIAssistant"""

    name: Optional[str] = None

    relevant: Optional[str] = None

    helpful_responses: Optional[str] = None



class AIAssistant(AIAssistantBase):
    """Full AIAssistant model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True