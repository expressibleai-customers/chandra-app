from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class ResourceManagementBase(BaseModel):
    """Base model for ResourceManagement"""

    filtering: str = None = Field(..., description="Filtering")

    categorization: str = None = Field(..., description="Categorization")

    content_management_capabilities: str = None = Field(..., description="Content Management Capabilities")



class ResourceManagementCreate(ResourceManagementBase):
    """Model for creating ResourceManagement"""
    pass


class ResourceManagementUpdate(ResourceManagementBase):
    """Model for updating ResourceManagement"""

    filtering: Optional[str] = None

    categorization: Optional[str] = None

    content_management_capabilities: Optional[str] = None



class ResourceManagement(ResourceManagementBase):
    """Full ResourceManagement model"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True