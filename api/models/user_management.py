from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Literal
from datetime import datetime


class UserManagementBase(BaseModel):
    """Base model for UserManagement"""

    role: Literal["caregiver", "care_receiver", "care_provider", "business"] = Field(..., description="I am a")



class UserManagementCreate(UserManagementBase):
    """Model for creating UserManagement"""
    pass


class UserManagementUpdate(UserManagementBase):
    """Model for updating UserManagement"""

    role: Optional[str] = None



class UserManagement(UserManagementBase):
    """Full UserManagement model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True