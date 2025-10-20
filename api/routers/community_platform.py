from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.community_platform import (
    CommunityPlatform,
    CommunityPlatformCreate,
    CommunityPlatformUpdate
)
from ..database.models import CommunityPlatform as DBCommunityPlatform

router = APIRouter(
    prefix="/community_platforms",
    tags=["community_platforms"]
)


@router.post("/", response_model=CommunityPlatform)
def create_community_platform(
    item: CommunityPlatformCreate,
    db: Session = Depends(get_db)
):
    """Create a new CommunityPlatform"""
    db_item = DBCommunityPlatform(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[CommunityPlatform])
def list_community_platforms(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all community_platforms"""
    items = db.query(DBCommunityPlatform).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=CommunityPlatform)
def get_community_platform(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific CommunityPlatform"""
    item = db.query(DBCommunityPlatform).filter(DBCommunityPlatform.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="CommunityPlatform not found")
    return item


@router.put("/{item_id}", response_model=CommunityPlatform)
def update_community_platform(
    item_id: int,
    item: CommunityPlatformUpdate,
    db: Session = Depends(get_db)
):
    """Update a CommunityPlatform"""
    db_item = db.query(DBCommunityPlatform).filter(DBCommunityPlatform.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="CommunityPlatform not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_community_platform(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete a CommunityPlatform"""
    db_item = db.query(DBCommunityPlatform).filter(DBCommunityPlatform.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="CommunityPlatform not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "CommunityPlatform deleted successfully"}