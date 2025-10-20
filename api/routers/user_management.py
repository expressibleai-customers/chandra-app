from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.user_management import (
    UserManagement,
    UserManagementCreate,
    UserManagementUpdate
)
from ..database.models import UserManagement as DBUserManagement

router = APIRouter(
    prefix="/user_managements",
    tags=["user_managements"]
)


@router.post("/", response_model=UserManagement)
def create_user_management(
    item: UserManagementCreate,
    db: Session = Depends(get_db)
):
    """Create a new UserManagement"""
    db_item = DBUserManagement(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[UserManagement])
def list_user_managements(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all user_managements"""
    items = db.query(DBUserManagement).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=UserManagement)
def get_user_management(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific UserManagement"""
    item = db.query(DBUserManagement).filter(DBUserManagement.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="UserManagement not found")
    return item


@router.put("/{item_id}", response_model=UserManagement)
def update_user_management(
    item_id: int,
    item: UserManagementUpdate,
    db: Session = Depends(get_db)
):
    """Update a UserManagement"""
    db_item = db.query(DBUserManagement).filter(DBUserManagement.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="UserManagement not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_user_management(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete a UserManagement"""
    db_item = db.query(DBUserManagement).filter(DBUserManagement.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="UserManagement not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "UserManagement deleted successfully"}