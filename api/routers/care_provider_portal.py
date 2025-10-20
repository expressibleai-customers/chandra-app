from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.care_provider_portal import (
    CareProviderPortal,
    CareProviderPortalCreate,
    CareProviderPortalUpdate
)
from ..database.models import CareProviderPortal as DBCareProviderPortal

router = APIRouter(
    prefix="/care_provider_portals",
    tags=["care_provider_portals"]
)


@router.post("/", response_model=CareProviderPortal)
def create_care_provider_portal(
    item: CareProviderPortalCreate,
    db: Session = Depends(get_db)
):
    """Create a new CareProviderPortal"""
    db_item = DBCareProviderPortal(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[CareProviderPortal])
def list_care_provider_portals(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all care_provider_portals"""
    items = db.query(DBCareProviderPortal).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=CareProviderPortal)
def get_care_provider_portal(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific CareProviderPortal"""
    item = db.query(DBCareProviderPortal).filter(DBCareProviderPortal.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="CareProviderPortal not found")
    return item


@router.put("/{item_id}", response_model=CareProviderPortal)
def update_care_provider_portal(
    item_id: int,
    item: CareProviderPortalUpdate,
    db: Session = Depends(get_db)
):
    """Update a CareProviderPortal"""
    db_item = db.query(DBCareProviderPortal).filter(DBCareProviderPortal.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="CareProviderPortal not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_care_provider_portal(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete a CareProviderPortal"""
    db_item = db.query(DBCareProviderPortal).filter(DBCareProviderPortal.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="CareProviderPortal not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "CareProviderPortal deleted successfully"}