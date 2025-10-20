from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.ai_assistant import (
    AIAssistant,
    AIAssistantCreate,
    AIAssistantUpdate
)
from ..database.models import AIAssistant as DBAIAssistant

router = APIRouter(
    prefix="/ai_assistants",
    tags=["ai_assistants"]
)


@router.post("/", response_model=AIAssistant)
def create_ai_assistant(
    item: AIAssistantCreate,
    db: Session = Depends(get_db)
):
    """Create a new AIAssistant"""
    db_item = DBAIAssistant(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[AIAssistant])
def list_ai_assistants(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all ai_assistants"""
    items = db.query(DBAIAssistant).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=AIAssistant)
def get_ai_assistant(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific AIAssistant"""
    item = db.query(DBAIAssistant).filter(DBAIAssistant.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="AIAssistant not found")
    return item


@router.put("/{item_id}", response_model=AIAssistant)
def update_ai_assistant(
    item_id: int,
    item: AIAssistantUpdate,
    db: Session = Depends(get_db)
):
    """Update a AIAssistant"""
    db_item = db.query(DBAIAssistant).filter(DBAIAssistant.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="AIAssistant not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_ai_assistant(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete a AIAssistant"""
    db_item = db.query(DBAIAssistant).filter(DBAIAssistant.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="AIAssistant not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "AIAssistant deleted successfully"}