from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class CareProviderPortalBase(BaseModel):
    """Base model for CareProviderPortal"""

    caregivers: str = None = Field(..., description="Caregivers")

    care_receivers: str = None = Field(..., description="Care Receivers")



class CareProviderPortalCreate(CareProviderPortalBase):
    """Model for creating CareProviderPortal"""
    pass


class CareProviderPortalUpdate(CareProviderPortalBase):
    """Model for updating CareProviderPortal"""

    caregivers: Optional[str] = None

    care_receivers: Optional[str] = None



class CareProviderPortal(CareProviderPortalBase):
    """Full CareProviderPortal model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True