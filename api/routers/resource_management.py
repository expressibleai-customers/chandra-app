from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.resource_management import (
    ResourceManagement,
    ResourceManagementCreate,
    ResourceManagementUpdate
)
from ..database.models import ResourceManagement as DBResourceManagement

router = APIRouter(
    prefix="/resource_managements",
    tags=["resource_managements"]
)


@router.post("/", response_model=ResourceManagement)
def create_resource_management(
    item: ResourceManagementCreate,
    db: Session = Depends(get_db)
):
    """Create a new ResourceManagement"""
    db_item = DBResourceManagement(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[ResourceManagement])
def list_resource_managements(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all resource_managements"""
    items = db.query(DBResourceManagement).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=ResourceManagement)
def get_resource_management(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific ResourceManagement"""
    item = db.query(DBResourceManagement).filter(DBResourceManagement.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="ResourceManagement not found")
    return item


@router.put("/{item_id}", response_model=ResourceManagement)
def update_resource_management(
    item_id: int,
    item: ResourceManagementUpdate,
    db: Session = Depends(get_db)
):
    """Update a ResourceManagement"""
    db_item = db.query(DBResourceManagement).filter(DBResourceManagement.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="ResourceManagement not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_resource_management(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete a ResourceManagement"""
    db_item = db.query(DBResourceManagement).filter(DBResourceManagement.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="ResourceManagement not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "ResourceManagement deleted successfully"}