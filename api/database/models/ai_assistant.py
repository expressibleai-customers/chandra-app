from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, CheckConstraint
from sqlalchemy.sql import func
from ..database import Base


class AIAssistant(Base):
    __tablename__ = "ai_assistants"


    id = Column(
        Integer,

        primary_key=True,


        nullable=False,




    )

    name = Column(
        Text,


        nullable=False,




    )

    relevant = Column(
        Text,





    )

    helpful_responses = Column(
        Text,





    )

    created_at = Column(
        DateTime,


        nullable=False,



        server_default=CURRENT_TIMESTAMP,


    )

    updated_at = Column(
        DateTime,


        nullable=False,



        server_default=CURRENT_TIMESTAMP,


        onupdate=func.now(),

    )
