from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class CommunityPlatformBase(BaseModel):
    """Base model for CommunityPlatform"""

    community_management: str = None = Field(..., description="Community Management")

    moderation_tools: str = None = Field(..., description="Moderation Tools")



class CommunityPlatformCreate(CommunityPlatformBase):
    """Model for creating CommunityPlatform"""
    pass


class CommunityPlatformUpdate(CommunityPlatformBase):
    """Model for updating CommunityPlatform"""

    community_management: Optional[str] = None

    moderation_tools: Optional[str] = None



class CommunityPlatform(CommunityPlatformBase):
    """Full CommunityPlatform model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True